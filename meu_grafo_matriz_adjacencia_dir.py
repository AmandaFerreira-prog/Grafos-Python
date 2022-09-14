from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

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
        pass

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

    def warshall(self):
        '''
        Gera a matriz de alcançabilidade do grafo
        :return:Matriz de alcançabilidade
        '''
        grafo_warshall = deepcopy(self)
        for i in range(len(grafo_warshall.M)):
            for j in range(len(grafo_warshall.M)):
                lista = []
                if grafo_warshall.M[j][i]!={}:
                    for k in range(len(grafo_warshall.M)):
                        if j<i:
                            z=j
                            u=i
                        else:
                            z=i
                            u = j
                        while z<=u:
                            if grafo_warshall.M[z][k]!={}:
                                lista.append(grafo_warshall.M[z][k])
                            z+=1
                        maximo=[]
                        for c in lista:
                            maxx=0
                            if c is lista[0]:
                                maximo=c
                                maxx=len(c)
                                continue
                            if len(c)>maxx:
                                maximo=c
                                maxx=len(c)
                        grafo_warshall.M[j][k]=maximo
        return grafo_warshall

    def dijkstra(self,vinicial,vfinal):
        '''
        Encontra o menor caminho de um ponto ao outro, utilizando seus próprios críterios
        :param vinicial:Vértice onde se inicia o caminho
        :param vfinal:Vertice onde acaba o caminho
        :return:O menor caminho do Vértice inicial ao Vértice final
        '''
        peso_caminhos=[]
        situacao_vertices=[]
        vertices_anteriores=[]
        caminho=[]
        w=vinicial
        for i in range(len(self.N)):
            peso_caminhos.append("-")
            situacao_vertices.append(0)
            vertices_anteriores.append("")
        peso_caminhos[self.N.index(vinicial)] = 0
        situacao_vertices[self.N.index(vinicial)] = 1
        while True:
            indiceatual = self.N.index(w)
            vertices_de_alcance=self.vertices_alcance(w)
            for v,a in vertices_de_alcance.items():
                ind=self.N.index(v)
                peso_aresta=self.M[indiceatual][ind].__getitem__(a).getPeso()
                if situacao_vertices[ind]==0:
                    if peso_caminhos[ind]=="-" or peso_caminhos[ind]>peso_caminhos[indiceatual]+peso_aresta:
                        peso_caminhos[ind]=peso_caminhos[indiceatual]+peso_aresta
                        vertices_anteriores[ind]=w
            min=0
            I=0
            for i,s in enumerate(situacao_vertices):
                if s==0 and peso_caminhos[i]!='-':
                    if i==0:
                        min=peso_caminhos[i]
                        I=i
                    else:
                        if peso_caminhos[i]<min or min==0:
                            min=peso_caminhos[i]
                            I=i
            situacao_vertices[I]=1
            w=self.N[I]
            caminho = []
            if w==vfinal:
                caminho.append(w)
                IND=I
                while True:
                    v_anterior=vertices_anteriores[IND]
                    caminho.append(v_anterior)
                    if v_anterior==self.N[0]:
                        break
                    IND=self.N.index(v_anterior)
                break
        return caminho

    def dijkstra_drone(self,vinicial,vfinal,carga_inicio,carga_maxima,pontos_recarga=list):
        '''
        Encontra o menor caminho de um ponto ao outro, utilizando seus próprios críterios
        :param vinicial:Vértice onde se inicia o caminho
        :param vfinal:Vertice onde acaba o caminho
        :param carga_inicio: Carga inicial do drone
        :param carga_maxima: Valor máximo de carga do Drone
        :param pontos_recarga: Lista contendo os vértices onde se pode recarregar o drone
        :return:O menor caminho do Vértice inicial ao Vértice final
        '''
        peso_caminhos=[]
        situacao_vertices=[]
        vertices_anteriores=[]
        caminho=[]
        carga_atual=carga_inicio
        w=vinicial
        for i in range(len(self.N)):
            peso_caminhos.append("-")
            situacao_vertices.append(0)
            vertices_anteriores.append("")
        peso_caminhos[self.N.index(vinicial)] = 0
        situacao_vertices[self.N.index(vinicial)] = 1
        while True:
            indiceatual = self.N.index(w)
            vertices_de_alcance=self.vertices_alcance(w)
            x=len(vertices_de_alcance.items())
            for v,a in vertices_de_alcance.items():
                x-=1
                ind=self.N.index(v)
                peso_aresta=self.M[indiceatual][ind].__getitem__(a).getPeso()
                if situacao_vertices[ind]==0:
                    if peso_caminhos[ind]=="-" or peso_caminhos[ind]>peso_caminhos[indiceatual]+peso_aresta:
                        if carga_atual-peso_aresta<1 and carga_atual>=peso_aresta:
                            if x==0 and v not in pontos_recarga:
                                carga_atual=0
                                break
                            elif x==0 and v in pontos_recarga:
                                carga_atual = carga_maxima
                                peso_caminhos[ind] = peso_caminhos[indiceatual] + peso_aresta
                                vertices_anteriores[ind] = w
                            else:
                                continue
                        else:
                            if v in pontos_recarga:
                                carga_atual=carga_maxima
                                peso_caminhos[ind] = peso_caminhos[indiceatual] + peso_aresta
                                vertices_anteriores[ind] = w
                            else:
                                carga_atual -=peso_aresta
                                peso_caminhos[ind] = peso_caminhos[indiceatual] + peso_aresta
                                vertices_anteriores[ind] = w

            min=0
            I=0
            for i,s in enumerate(situacao_vertices):
                if s==0 and peso_caminhos[i]!='-':
                    if i==0:
                        min=peso_caminhos[i]
                        I=i
                    else:
                        if peso_caminhos[i]<min or min==0:
                            min=peso_caminhos[i]
                            I=i
            situacao_vertices[I]=1
            w=self.N[I]
            caminho = []
            if carga_atual==0:
                return "Caminho inexistente"
            if w==vfinal:
                caminho.append(w)
                IND=I
                while True:
                    v_anterior=vertices_anteriores[IND]
                    caminho.append(v_anterior)
                    if v_anterior==self.N[0] or v_anterior=='':
                        if caminho[-1]=='': caminho.remove('')
                        break
                    IND=self.N.index(v_anterior)
                break
        return caminho


    def vertices_alcance(self,V=''):
        '''
        Retorna os vértices alcançados pelas arestas direcionadas do vértice passado como parãmetro
        :param V: Vértice a ser analisado
        :return: Uma lista com os vértices alcançados pelo vértice do parâmetro.
        '''
        vertices = {}
        indice = self.N.index(V)
        for c in range(len(self.M)):
            for a in self.M[indice][c] :
                if a=={}:
                    continue
                i=self.N[c]
                vertices[i]=a
        return vertices

    def fontes(self):
        '''
        Verifica quais vértices são fontes no grafo
        :return: Uma lista com os vérices fontes do grafo
        '''
        fontes=[]
        for v in self.N:
            indice=self.N.index(v)
            for n in range(len(self.N)):
                area=self.M[n][indice]
                if area!={}:
                    break
                if n==len(self.N)-1:
                    fontes.append(v)
        return fontes

    def ordenacao_topologica(self):
        '''
        Faz a ordenação topológica de um grafo
        :return: Uma lista com os vértices em ordem topológica
        '''
        grafo2=deepcopy(self)
        ordenacao=[]
        while grafo2.N:
            fontes=grafo2.fontes()
            for x in fontes:
                ordenacao.append(x)
            for v in fontes:
                grafo2.removeVertice(v)
        return ordenacao



