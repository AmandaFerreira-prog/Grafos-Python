from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo_matriz_adjacencia_dir import *

grafoDirecionado2=MeuGrafo(['A','B','C','D','E','F','G'])
grafoDirecionado2.adicionaAresta('a1','A','B',2)
grafoDirecionado2.adicionaAresta('a2','A','C',1)
grafoDirecionado2.adicionaAresta('a3','B','D',1)
grafoDirecionado2.adicionaAresta('a4','D','A',3)
grafoDirecionado2.adicionaAresta('a5','C','D',4)
grafoDirecionado2.adicionaAresta('a6','C','F',5)
grafoDirecionado2.adicionaAresta('a7','D','F',2)
grafoDirecionado2.adicionaAresta('a8','D','E',2)
grafoDirecionado2.adicionaAresta('a9','E','G',10)
grafoDirecionado2.adicionaAresta('a10','F','G',7)

grafoDirecionado3=MeuGrafo(['A','B','C','D','E','F','G'])
grafoDirecionado3.adicionaAresta('a1','A','B',1)
grafoDirecionado3.adicionaAresta('a2','B','C',2)
grafoDirecionado3.adicionaAresta('a3','A','D',3)
grafoDirecionado3.adicionaAresta('a4','D','E',2)
grafoDirecionado3.adicionaAresta('a5','E','F',4)
grafoDirecionado3.adicionaAresta('a6','E','G',1)
grafoDirecionado3.adicionaAresta('a7','B','G',5)
grafoDirecionado3.adicionaAresta('a8','F','G',3)
grafoDirecionado3.adicionaAresta('a9','C','G',2)
grafoDirecionado3.adicionaAresta('a10','D','G',3)

print(grafoDirecionado3.Prim())

