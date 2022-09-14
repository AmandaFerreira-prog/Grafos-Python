from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        listadeadjacencias = []
        for x in self.A:
            listadeadjacencias.append(f'{self.A[x].getV1()}-{self.A[x].getV2()}')

        listadeocorrencias = []
        vertices = self.N.copy()
        for x in vertices:
            if f'{x}-{x}' in listadeadjacencias:
                print('False')
            for v in vertices:
                if v == x:
                    continue
                if f'{x}-{v}' not in listadeadjacencias and f'{v}-{x}' not in listadeadjacencias:
                    if f'{x}-{v}' not in listadeocorrencias and f'{v}-{x}' not in listadeocorrencias:
                        listadeocorrencias.append(f'{x}-{v}')
        return listadeocorrencias

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
            if self.A[a].getV1()==self.A[a].getV2():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        grau = 0
        if not self.existeVertice(V):
           raise VerticeInvalidoException(V)
        else:
            for x in self.A:
                if self.A[x].getV1() == self.A[x].getV2() and self.A[x].getV2() == V:
                    grau += 2
                else:
                    if self.A[x].getV1() == V or self.A[x].getV2() == V:
                        grau += 1
            return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        V1=''
        V2=''
        for x in self.A:
            V1 = self.A[x].getV1()
            V2 = self.A[x].getV2()
            for c in self.A:
                if c == x:
                    continue
                else:
                    if self.A[c].getV1() == V1 and self.A[c].getV2() == V2:
                        return True
                        break
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        arestas = []
        if not self.existeVertice(V):
           raise VerticeInvalidoException(V)
        else:
            for x in self.A:
                if self.A[x].getV1() == self.A[x].getV2():
                    if self.A[x].getV2()==V:
                        arestas.append(x)
                        continue
                if self.A[x].getV1() == V or self.A[x].getV2() == V:
                    arestas.append(x)
            return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        listadeadjacencias = []
        for x in self.A:
            listadeadjacencias.append(f'{self.A[x].getV1()}-{self.A[x].getV2()}')
        vertices = self.N
        cont = 0
        for v in vertices:
            if f'{v}-{v}' in listadeadjacencias:
                return False
            for x in vertices:
                if x == v:
                    continue
                adjacencia1 = f'{v}-{x}'
                adjacencia2 = f'{x}-{v}'
                if adjacencia1 not in listadeadjacencias and adjacencia2 not in listadeadjacencias:
                    return False
        return True

    def dfs(self,V=''):
        '''
        Cria um novo grafo apenas com as arestas que fazem parte da árvore DFS
        :param V: Vértice que será usado como raiz
        :return: um grafo da árvore DFS
        '''
        dfs=MeuGrafo(deepcopy(self.N))
        visitados = []
        fila = []
        arestas = []
        fila.append(V)
        for x in self.A:
            arestas.append(x)

        while fila:
            atual = fila.pop(0)
            visitados.append(atual)
            ADJ = self.arestas_sobre_vertice(atual)
            for x in ADJ:
                ultimo = ADJ[-1]
                v1 = self.A[x].getV1()
                v2 = self.A[x].getV2()
                if v1 in visitados and v2 in visitados:
                    if x == arestas[-1]:
                        break
                    if len(ADJ) == 1:
                        if v1 != atual:
                            fila.append(v1)
                        if v2 != atual:
                            fila.append(v2)
                    if not fila and x == ultimo:
                        if v1 != atual:
                            fila.append(v1)
                        if v2 != atual:
                            fila.append(v2)
                    continue
                if v1 == v2:
                    continue
                if v1 != atual:
                    fila.append(v1)
                    if v1 not in visitados:
                        visitados.append(v1)
                        dfs.adicionaAresta(x, v1, v2)
                        break
                if v2 != atual:
                    fila.append(v2)
                    if v2 not in visitados:
                        visitados.append(v2)
                        dfs.adicionaAresta(x, v1, v2)
                        break
        return dfs

    def bfs(self,V=''):
        '''
        Cria um novo grafo apenas com as arestas que fazem parte da árvore BFS
        :param V: Vértice que será usado como raiz
        :return: um grafo da árvore BFS
        '''
        vertices=deepcopy(self.N)
        bfs=MeuGrafo(vertices)

        listadeadjacencias = []
        for x in self.A:
            listadeadjacencias.append(f'{self.A[x].getV1()}-{self.A[x].getV2()}')

        visitado = []
        fila = []
        visitado.append(V)
        fila.append(V)
        cont = 0
        while fila:
            V = fila.pop(0)

            for n in vertices:
                if f'{V}-{n}' in listadeadjacencias or f'{n}-{V}' in listadeadjacencias:
                    if n not in visitado:
                        cont += 1
                        bfs.adicionaAresta(f'a{cont}', f'{V}', f'{n}')
                        visitado.append(n)
                        fila.append(n)
        return bfs

    def ha_ciclo(self):
        '''
        Verifica se há algum ciclo no grafo
        :return:Uma lista com os vértices e arestas que compõem o ciclo se houver, se não existir nenhum ciclo retorna False
        '''
        fila = []
        ciclo = []

        for v in self.N:
            fila.append(v)
            visitado = []
            arestas_visitadas = []
            ciclo.clear()
            while fila:
                V = fila.pop(0)
                visitado.append(V)
                adj = self.arestas_sobre_vertice(V)
                if len(adj) <= 0:
                    break
                for a in adj:
                    arestas_visitadas.append(a)
                    v1 = self.A[a].getV1()
                    v2 = self.A[a].getV2()
                    if v1 == v2 and v1 == v:
                        ciclo.append(v1)
                        ciclo.append(a)
                        ciclo.append(v2)
                        break
                    if v1 != V:
                        if v1 not in visitado:
                            adj2 = self.arestas_sobre_vertice(v1)
                            if len(adj2) == 1 and adj2[0] == a:
                                continue
                            continua = False
                            visitado.append(v1)
                            for b in adj2:
                                if b not in arestas_visitadas:
                                    if self.A[b].getV1() not in visitado:
                                        continua = True
                                    if self.A[b].getV1() == v:
                                        continua = True
                                    if self.A[b].getV2() not in visitado:
                                        continua = True
                                    if self.A[b].getV2() == v:
                                        continua = True
                            if continua:
                                fila.append(v1)
                                if len(ciclo) == 0:
                                    ciclo.append(V)
                                    ciclo.append(a)
                                    ciclo.append(v1)
                                    break
                                else:
                                    if a not in ciclo:
                                        ciclo.append(a)
                                        ciclo.append(v1)
                                    break
                        else:
                            if v1 == v:
                                if len(ciclo) == 0:
                                    ciclo.append(V)
                                    ciclo.append(a)
                                    ciclo.append(v1)
                                    break
                                else:
                                    if a not in ciclo:
                                        ciclo.append(a)
                                        ciclo.append(v1)
                                        break
                            if a == adj[-1] and fila == []:
                                if len(adj)==1:
                                    break
                                fila.append(v1)
                                continue
                            continue
                    if v2 != V:
                        if v2 not in visitado:
                            adj3 = self.arestas_sobre_vertice(v2)
                            if len(adj3) == 1 and adj3[0] == a:
                                continue
                            continua_2 = False
                            visitado.append(v2)
                            for i in adj3:
                                if i not in arestas_visitadas:
                                    if self.A[i].getV1() not in visitado:
                                        continua_2 = True
                                    if self.A[i].getV1() == v:
                                        continua_2 = True
                                    if self.A[i].getV2() not in visitado:
                                        continua_2 = True
                                    if self.A[i].getV2() == v:
                                        continua_2 = True
                            if continua_2:
                                fila.append(v2)
                                if len(ciclo) == 0:
                                    ciclo.append(V)
                                    ciclo.append(a)
                                    ciclo.append(v2)
                                    break
                                else:
                                    if a not in ciclo:
                                        ciclo.append(a)
                                        ciclo.append(v2)
                                        break
                        else:
                            if v2 == v:
                                if len(ciclo) == 0:
                                    ciclo.append(V)
                                    ciclo.append(a)
                                    ciclo.append(v2)
                                    break
                                else:
                                    if a not in ciclo:
                                        ciclo.append(a)
                                        ciclo.append(v2)
                                        break
                            if a == adj[-1] and fila == []:
                                if len(adj)==1:
                                    break
                                fila.append(v2)
                                continue
                            continue
            if len(ciclo)>1 and ciclo[-1]==v:
                break
        if ciclo==[]:
            return False
        return ciclo

    def caminho(self,n):
        '''
        Verifica se há um caminho de tamanho N.
        :param n:Comprimento do caminho
        :return:Uma lista com os vértices e arestas que compõem o caminho
        '''
        fila = []
        caminho = []

        for v in self.N:
            fila.append(v)
            visitado = []
            caminho.clear()
            comprimento = 0
            while fila:
                V = fila.pop(0)
                visitado.append(V)
                adj = self.arestas_sobre_vertice(V)
                if len(adj) <= 0:
                    break
                for a in adj:
                    v1 = self.A[a].getV1()
                    v2 = self.A[a].getV2()
                    if v1 != V:
                        if v1 not in visitado:
                            adj2 = self.arestas_sobre_vertice(v1)
                            continua = False
                            visitado.append(v1)
                            if comprimento + 1 == n:
                                if len(caminho) <= 0:
                                    comprimento += 1
                                    caminho.append(V)
                                    caminho.append(a)
                                    caminho.append(v1)
                                else:
                                    comprimento += 1
                                    caminho.append(a)
                                    caminho.append(v1)
                                break
                            else:
                                for b in adj2:
                                    if self.A[b].getV1() != v1 and self.A[b].getV1() not in visitado:
                                        continua = True
                                    if self.A[b].getV2() != v1 and self.A[b].getV2() not in visitado:
                                        continua = True
                                if continua:
                                    fila.append(v1)
                                    if len(caminho) == 0:
                                        comprimento += 1
                                        caminho.append(V)
                                        caminho.append(a)
                                        caminho.append(v1)
                                    else:
                                        comprimento += 1
                                        caminho.append(a)
                                        caminho.append(v1)
                                    break
                        else:
                            if comprimento + 1 == n and a not in caminho and v1 not in caminho:
                                if len(caminho) <= 0:
                                    comprimento += 1
                                    caminho.append(V)
                                    caminho.append(a)
                                    caminho.append(v1)
                                else:
                                    comprimento += 1
                                    caminho.append(a)
                                    caminho.append(v1)
                                break
                            else:
                                continue
                    if v2 != V:
                        if v2 not in visitado:
                            adj3 = self.arestas_sobre_vertice(v2)
                            continua_v2 = False
                            visitado.append(v2)
                            if comprimento + 1 == n:
                                if len(caminho) <= 0:
                                    comprimento += 1
                                    caminho.append(V)
                                    caminho.append(a)
                                    caminho.append(v2)
                                else:
                                    comprimento += 1
                                    caminho.append(a)
                                    caminho.append(v2)
                                break
                            else:
                                for i in adj3:
                                    if self.A[i].getV1() != v2 and self.A[i].getV1() not in visitado:
                                        continua_v2 = True
                                    if self.A[i].getV2() != v2 and self.A[i].getV2() not in visitado:
                                        continua_v2 = True
                                if continua_v2:
                                    fila.append(v2)
                                    if len(caminho) == 0:
                                        comprimento += 1
                                        caminho.append(V)
                                        caminho.append(a)
                                        caminho.append(v2)
                                    else:
                                        comprimento += 1
                                        caminho.append(a)
                                        caminho.append(v2)
                                    break
                        else:
                            if comprimento + 1 == n and a not in caminho and v2 not in caminho:
                                if len(caminho) <= 0:
                                    comprimento += 1
                                    caminho.append(V)
                                    caminho.append(a)
                                    caminho.append(v2)
                                else:
                                    comprimento += 1
                                    caminho.append(a)
                                    caminho.append(v2)
                                break
                            else:
                                continue
            if comprimento==n:
                break
            if v==self.N[-1] and comprimento!=n:
                caminho.clear()
        return caminho

    def conexo(self):
        '''
        Verifica se o grafo é conexo ou não
        :return: Um valor booleano que indica se o grafo é conexo ou não.
        '''
        for x in self.N:
            adj=self.arestas_sobre_vertice(x)
            if not adj:
                return False
                break
        return True

    def caminho_euleriano(self):
        '''
        Verifica se há um caminho euleriano e mostra qual é o caminho
        :return: Um valor boleano que identifica se há um caminho euleriano
        '''
        v_impares=0
        ultimo_impar=0
        caminho=[]
        if not self.conexo():
            '''o grafo nao é conexo, tente com outro!'''
            return False

        for v in self.N:
            g=self.grau(v)
            if self.grau(v)%2!=0:
                v_impares+=1
                ultimo_impar=v

        if v_impares==0:
            return self.print_euler(self.N[0],caminho)
        elif v_impares==2:
            return self.print_euler(ultimo_impar,caminho)
        else:
            '''Caminho de Euler não existe no grafo'''
            return False

    def print_euler(self,V='',caminho=[]):
        '''
        Retorna uma lista com o caminho euleriano
        :param V: Vertice que irá iniciar o caminho
        :return: lista no formato [V1,A1,V2,A2,...] com os vértices e arestas que compõem o caminho euleriano
        '''
        grafo_copia=deepcopy(self)
        adj_v=self.arestas_sobre_vertice(V)
        if len(adj_v)==0:
            return caminho
        elif len(adj_v)==1:
            if self.A[adj_v[0]].getV1()!=V:
                vertice_seguinte=self.A[adj_v[0]].getV1()
            else:
                vertice_seguinte = self.A[adj_v[0]].getV2()
            if adj_v[0] in caminho:
                grafo_copia.print_euler(vertice_seguinte, caminho)
            if caminho and caminho[-1] != V:
                caminho.append(V)
            if caminho == []:
                caminho.append(V)
            caminho.append(adj_v[0])
            caminho.append(vertice_seguinte)
            grafo_copia.removeAresta(adj_v[0])
            grafo_copia.print_euler(vertice_seguinte,caminho)
            return caminho
        else:
            for a in adj_v:
                if a in caminho:
                    continue
                v_1=self.A[a].getV1()
                v_2=self.A[a].getV2()
                if self.eh_ponte(a) is False:
                    grafo_copia.removeAresta(a)
                    if caminho and caminho[-1]!=V:
                        caminho.append(V)
                    if caminho==[]:
                        caminho.append(V)
                    caminho.append(a)
                    if v_1!=V:
                        vertice2=v_1
                        caminho.append(vertice2)
                        grafo_copia.print_euler(vertice2,caminho)
                    else:
                        vertice2=v_2
                        caminho.append(vertice2)
                        grafo_copia.print_euler(vertice2,caminho)
            return caminho


    def eh_ponte(self,a=''):
        '''
        Verifica se a aresta é uma ponte
        :param a: Rótulo da aresta a ser verificada
        :param v: V inicial, nao sera usado apenas para diferenciar do segundo vértice
        :return: Um valor booleano para identificar se é uma ponte ou não
        '''
        grafo_copia=deepcopy(self)
        v1=self.A[a].getV1()
        v2=self.A[a].getV2()
        grafo_copia.removeAresta(a)
        if grafo_copia.conexo():
            grafo_copia.adicionaAresta(a,v1,v2)
            return False
        else:
            grafo_copia.adicionaAresta(a,v1,v2)
            return True

    def Prim(self):
        '''
        Retorna a arvore geradora minima
        :return: Um novo grafo, sendo a árvore geradora minima do grafo passado.
        '''
        if not self.conexo():
            return "Grafo não possui árvore geradora mínima ,pois não é CONEXO!"
        grafo2=MeuGrafo()
        v=self.N[0]
        while True:
            if not grafo2.N:
                vertices=[self.N[0]]
            else:
                vertices=grafo2.N
            v_2 = ''
            peso_min = 0
            aresta = ''
            for ver in vertices:
                adj=self.arestas_sobre_vertice(ver)
                for a in adj:
                    v1=self.A[a].getV1()
                    v2=self.A[a].getV2()
                    if v1!=ver:
                        v_atual=v1
                    else:
                        v_atual=v2
                    peso_aresta=self.A[a].getPeso()
                    if v_atual not in grafo2.N:
                        if peso_min==0:
                            peso_min=peso_aresta
                            v_2=v_atual
                            aresta=a
                        else:
                            if peso_aresta<peso_min:
                                peso_min=peso_aresta
                                v_2=v_atual
                                aresta = a
            if v_2=='':
                break
            if v not in grafo2.N :
                grafo2.adicionaVertice(v)
            if v_2 not in grafo2.N:
                grafo2.adicionaVertice(v_2)
            grafo2.adicionaAresta(self.A[aresta].getRotulo(),self.A[aresta].getV1(),self.A[aresta].getV2(),self.A[aresta].getPeso())
            if v==self.N[-1] and len(self.N)==len(grafo2.N):
                break
            v=v_2

        return grafo2

    def Prim_modificado(self):
        '''
        Retorna a arvore geradora minima
        :return: Um novo grafo, sendo a árvore geradora minima do grafo passado.
        '''
        if not self.conexo():
            return "Grafo não possui árvore geradora mínima ,pois não é CONEXO!"
        grafo2=MeuGrafo()
        v=''
        menor_peso=0
        for a in self.A:
            if self.A[a].getPeso()<menor_peso or menor_peso==0:
                menor_peso=self.A[a].getPeso()
                v=self.A[a].getV1()

        grafo2.adicionaVertice(v)
        while True:
            v_2 = ''
            peso_min = 0
            aresta = ''
            for ver in grafo2.N:
                adj=self.arestas_sobre_vertice(ver)
                for a in adj:
                    v1=self.A[a].getV1()
                    v2=self.A[a].getV2()
                    if v1!=ver:
                        v_atual=v1
                    else:
                        v_atual=v2
                    peso_aresta=self.A[a].getPeso()
                    if v_atual not in grafo2.N:
                        if peso_min==0:
                            peso_min=peso_aresta
                            v_2=v_atual
                            aresta=a
                        else:
                            if peso_aresta<peso_min:
                                peso_min=peso_aresta
                                v_2=v_atual
                                aresta = a
            if v_2=='':
                break
            if v not in grafo2.N :
                grafo2.adicionaVertice(v)
            if v_2 not in grafo2.N:
                grafo2.adicionaVertice(v_2)
            grafo2.adicionaAresta(self.A[aresta].getRotulo(),self.A[aresta].getV1(),self.A[aresta].getV2(),self.A[aresta].getPeso())
            if v==self.N[-1] and len(self.N)==len(grafo2.N):
                break
            v=v_2

        return grafo2

    def Kruskall(self):
        '''
        Gera a árvore geradora minima do grafo
        :return: um subgrafo que representa a arvore geradora
        '''
        fila_pesos=[]
        for a in self.A:
            peso=self.A[a].getPeso()
            fila_pesos.append(peso)
        fila_pesos.sort()
        arestas_prioridades=[]
        for p in fila_pesos:
            for a in self.A:
                if self.A[a].getPeso()==p and self.A[a] not in arestas_prioridades:
                    arestas_prioridades.append(self.A[a])
                    break
        vertices=deepcopy(self.N)
        grafo2=MeuGrafo(vertices)
        for aresta in arestas_prioridades:
            v1=aresta.getV1()
            v2=aresta.getV2()
            if v1!=v2:
                grafo2.adicionaAresta(aresta.getRotulo(),v1,v2,aresta.getPeso())
                if grafo2.verificar_ciclos():
                    grafo2.removeAresta(aresta.getRotulo())
            else:
                continue
        return grafo2

    def Kruskall_modificado(self):
        '''
        Gera a árvore geradora minima do grafo
        :return: um subgrafo que representa a arvore geradora
        '''
        if not self.conexo():
            return "Grafo não possui árvore geradora mínima ,pois não é CONEXO!"
        pesos=[]
        vertices = deepcopy(self.N)
        grafo2=MeuGrafo(vertices)
        for a in self.A:
            pesos.append(self.A[a].getPeso())
        pesos_visitados=[]
        while True:
            j = 0
            menor = 0
            c=0
            for p in pesos:
                if p=='-':
                    c+=1
                    continue
                if p <menor or menor==0:
                    menor=p
                    j=c
                c+=1
            pesos_visitados.append(pesos[j])
            pesos[j]='-'
            cont=0
            for a in self.A:
                if cont==j:
                    grafo2.adicionaAresta(self.A[a].getRotulo(),self.A[a].getV1(),self.A[a].getV2(),self.A[a].getPeso())
                    if grafo2.verificar_ciclos():
                        grafo2.removeAresta(self.A[a].getRotulo())
                    break
                cont+=1
            check=False
            for p in pesos:
                if p!='-':
                    check=True
            if check:
                continue
            else:
                break
        return grafo2

    def verificar_ciclos(self):
        '''
        Verifica se há ciclo no grafo
        :return: Um valor booleano para informar se há ciclo ou não
        '''
        if self.eh_completo():
            return True
        nodos_visitados = []
        nodos_restantes = [self.N[0]]

        while nodos_restantes:
            nodo_atual = nodos_restantes.pop()
            nodos_visitados.append(nodo_atual)

            for vizinho in self.vizinho(nodo_atual):
                if vizinho in nodos_visitados:
                    if vizinho==nodos_visitados[-2]:
                        continue
                    else:
                        if len(self.vizinho(nodos_visitados[-2]))==1:
                            continue
                        return True
                nodos_restantes.append(vizinho)
        return False

    def vizinho(self,V=''):
        '''
        Verifica quais os vértices vizinhos ao vértice passado como parâmetro
        :param V: Vértice a ser analisado
        :return: Uma lista com os vizinhos de V
        '''
        vizinhos=[]
        for x in self.A:
            v1=self.A[x].getV1()
            v2 = self.A[x].getV2()
            if (v1!=V and v2!=V) or (v1==v2 and v2==V):
                continue
            else:
                if v1!=V:
                    vizinhos.append(v1)
                else:
                    vizinhos.append(v2)
        return vizinhos

    def eh_ciclico(self):
        if len(self.A) > len(self.N) - 1:
            return True
        else:
            return False




