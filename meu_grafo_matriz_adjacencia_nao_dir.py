from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        naoadj = []
        for v in self.N:
            i_v1 = self.N.index(v)
            for n in range(len(self.M)):
                v2 = self.N.index(self.N[n])
                if v2 == i_v1:
                    continue
                if f'{v}-{self.N[n]}' not in naoadj and f'{self.N[n]}-{v}' not in naoadj:
                    if v2 < i_v1:
                        linha1 = self.M[v2][i_v1]
                        if linha1 == '-' or linha1 == {}:
                            naoadj.append(f'{v}-{self.N[n]}')
                    if v2 >= i_v1:
                        linha2 = self.M[i_v1][v2]
                        if linha2 == '-' or linha2 == {}:
                            naoadj.append(f'{v}-{self.N[n]}')
        return naoadj


    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for n in range(len(self.M)):
            if len(self.M[n][n]) != 0:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existeVertice(V):
           raise VerticeInvalidoException(V)

        grau = 0
        indice = self.N.index(V)

        for n in range(len(self.M)):
            if n < indice:
                if self.M[n][indice] != '-' and self.M[n][indice] != {}:
                    grau += len(self.M[n][indice])
                    continue
            if n == indice:
                if len(self.M[n][n]) > 0:
                    grau += len(self.M[n][n])
                for e in self.M[n]:
                    if e != '-' and e != {}:
                        grau += len(e)
                break
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass
        for n in range(len(self.M)):
            for j in range(len(self.M)):
                if len(self.M[n][j]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existeVertice(V):
           raise VerticeInvalidoException(V)

        indice = self.N.index(V)
        arestas = []
        for n in range(len(self.M)):
            if n < indice:
                linha = self.M[n][indice]
                if linha == '-' or linha is False:
                    continue
                for a in self.M[n][indice]:
                    arestas.append(a)
            if n >= indice:
                linha = self.M[indice][n]
                if linha == '-' or linha is False:
                    continue
                for a in self.M[indice][n]:
                    arestas.append(a)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        tot=len(self.N)
        for v in self.N:
            grau = self.grau(v)
            if grau != tot - 1 :
                return False
        return True

