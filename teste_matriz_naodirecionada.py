from meu_grafo_matriz_adjacencia_nao_dir import *

grafoDirecionado2=MeuGrafo(['A','B','C','D','E','F','G'])
grafoDirecionado2.adicionaAresta('a1','A','B')
grafoDirecionado2.adicionaAresta('a2','A','C')
grafoDirecionado2.adicionaAresta('a3','B','D')
grafoDirecionado2.adicionaAresta('a4','D','A')
grafoDirecionado2.adicionaAresta('a5','C','D')
grafoDirecionado2.adicionaAresta('a6','C','F')
grafoDirecionado2.adicionaAresta('a7','D','F')
grafoDirecionado2.adicionaAresta('a8','D','E')
grafoDirecionado2.adicionaAresta('a9','E','G')
grafoDirecionado2.adicionaAresta('a10','F','G')

grafoDirecionado3=MeuGrafo(['A','B','C','D','E','F','G'])
grafoDirecionado3.adicionaAresta('a1','A','B')
grafoDirecionado3.adicionaAresta('a2','B','C')
grafoDirecionado3.adicionaAresta('a3','A','D')
grafoDirecionado3.adicionaAresta('a4','D','E')
grafoDirecionado3.adicionaAresta('a5','E','F')
grafoDirecionado3.adicionaAresta('a6','E','G')
grafoDirecionado3.adicionaAresta('a7','B','G')
grafoDirecionado3.adicionaAresta('a8','F','G')
grafoDirecionado3.adicionaAresta('a9','C','G')
grafoDirecionado3.adicionaAresta('a10','D','G')