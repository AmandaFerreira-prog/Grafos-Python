import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'E', 'C')
        self.g_p.adicionaAresta('a4', 'C', 'P')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'C', 'M')
        self.g_p.adicionaAresta('a7', 'C', 'T')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        #Grafo 2 da paraiba

        self.g_p2 = MeuGrafo(['C', 'E', 'P', 'M', 'T'])
        self.g_p2.adicionaAresta('a2', 'C', 'E')
        self.g_p2.adicionaAresta('a3', 'E', 'C')
        self.g_p2.adicionaAresta('a4', 'C', 'P')
        self.g_p2.adicionaAresta('a5', 'P', 'C')
        self.g_p2.adicionaAresta('a6', 'C', 'M')
        self.g_p2.adicionaAresta('a7', 'C', 'T')
        self.g_p2.adicionaAresta('a8', 'M', 'T')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'C', 'P')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'C', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'C', 'M')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        #Grafos Direcionados
        self.grafoDirecionado=MeuGrafo(['A','B','C','D'])
        self.grafoDirecionado.adicionaAresta('a1','A','B')
        self.grafoDirecionado.adicionaAresta('a2','A','C')
        self.grafoDirecionado.adicionaAresta('a3','C','A')
        self.grafoDirecionado.adicionaAresta('a4','B','C')
        self.grafoDirecionado.adicionaAresta('a5','C','D')

        #Grafos testes para a arvore DFS
        self.gp_DFS_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_DFS_J.adicionaAresta('a1', 'J', 'C')
        self.gp_DFS_J.adicionaAresta('a2', 'C', 'E')
        self.gp_DFS_J.adicionaAresta('a4', 'C', 'P')
        self.gp_DFS_J.adicionaAresta('a6', 'C', 'M')
        self.gp_DFS_J.adicionaAresta('a8', 'M', 'T')
        self.gp_DFS_J.adicionaAresta('a9', 'T', 'Z')

        self.gp_DFS_C = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_DFS_C.adicionaAresta('a1', 'J', 'C')
        self.gp_DFS_C.adicionaAresta('a2', 'C', 'E')
        self.gp_DFS_C.adicionaAresta('a4', 'C', 'P')
        self.gp_DFS_C.adicionaAresta('a6', 'C', 'M')
        self.gp_DFS_C.adicionaAresta('a8', 'M', 'T')
        self.gp_DFS_C.adicionaAresta('a9', 'T', 'Z')

        self.gp_DFS_E = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_DFS_E.adicionaAresta('a2', 'C', 'E')
        self.gp_DFS_E.adicionaAresta('a1', 'J', 'C')
        self.gp_DFS_E.adicionaAresta('a4', 'C', 'P')
        self.gp_DFS_E.adicionaAresta('a6', 'C', 'M')
        self.gp_DFS_E.adicionaAresta('a8', 'M', 'T')
        self.gp_DFS_E.adicionaAresta('a9', 'T', 'Z')

        self.gp_DFS_P = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_DFS_P.adicionaAresta('a4', 'C', 'P')
        self.gp_DFS_P.adicionaAresta('a1', 'J', 'C')
        self.gp_DFS_P.adicionaAresta('a2', 'C', 'E')
        self.gp_DFS_P.adicionaAresta('a6', 'C', 'M')
        self.gp_DFS_P.adicionaAresta('a8', 'M', 'T')
        self.gp_DFS_P.adicionaAresta('a9', 'T', 'Z')

        self.gp_DFS_M = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_DFS_M.adicionaAresta('a6', 'C', 'M')
        self.gp_DFS_M.adicionaAresta('a1', 'J', 'C')
        self.gp_DFS_M.adicionaAresta('a2', 'C', 'E')
        self.gp_DFS_M.adicionaAresta('a4', 'C', 'P')
        self.gp_DFS_M.adicionaAresta('a7', 'C', 'T')
        self.gp_DFS_M.adicionaAresta('a9', 'T', 'Z')

        self.gp_DFS_T = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_DFS_T.adicionaAresta('a7', 'C', 'T')
        self.gp_DFS_T.adicionaAresta('a1', 'J', 'C')
        self.gp_DFS_T.adicionaAresta('a2', 'C', 'E')
        self.gp_DFS_T.adicionaAresta('a4', 'C', 'P')
        self.gp_DFS_T.adicionaAresta('a6', 'C', 'M')
        self.gp_DFS_T.adicionaAresta('a9', 'T', 'Z')

        self.gp_DFS_Z = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_DFS_Z.adicionaAresta('a9', 'T', 'Z')
        self.gp_DFS_Z.adicionaAresta('a7', 'C', 'T')
        self.gp_DFS_Z.adicionaAresta('a1', 'J', 'C')
        self.gp_DFS_Z.adicionaAresta('a2', 'C', 'E')
        self.gp_DFS_Z.adicionaAresta('a4', 'C', 'P')
        self.gp_DFS_Z.adicionaAresta('a6', 'C', 'M')

        # Grafos testes para a arvore BFS
        self.gp_BFS_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_BFS_J.adicionaAresta('a1', 'J', 'C')
        self.gp_BFS_J.adicionaAresta('a2', 'C', 'E')
        self.gp_BFS_J.adicionaAresta('a3', 'C', 'P')
        self.gp_BFS_J.adicionaAresta('a4', 'C', 'M')
        self.gp_BFS_J.adicionaAresta('a5', 'C', 'T')
        self.gp_BFS_J.adicionaAresta('a6', 'T', 'Z')

        self.gp_BFS_C = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_BFS_C.adicionaAresta('a1', 'C', 'J')
        self.gp_BFS_C.adicionaAresta('a2', 'C', 'E')
        self.gp_BFS_C.adicionaAresta('a3', 'C', 'P')
        self.gp_BFS_C.adicionaAresta('a4', 'C', 'M')
        self.gp_BFS_C.adicionaAresta('a5', 'C', 'T')
        self.gp_BFS_C.adicionaAresta('a6', 'T', 'Z')

        self.gp_BFS_E = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_BFS_E.adicionaAresta('a1', 'E', 'C')
        self.gp_BFS_E.adicionaAresta('a2', 'C', 'J')
        self.gp_BFS_E.adicionaAresta('a3', 'C', 'P')
        self.gp_BFS_E.adicionaAresta('a4', 'C', 'M')
        self.gp_BFS_E.adicionaAresta('a5', 'C', 'T')
        self.gp_BFS_E.adicionaAresta('a6', 'T', 'Z')

        self.gp_BFS_P = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_BFS_P.adicionaAresta('a1', 'P', 'C')
        self.gp_BFS_P.adicionaAresta('a2', 'C', 'J')
        self.gp_BFS_P.adicionaAresta('a3', 'C', 'E')
        self.gp_BFS_P.adicionaAresta('a4', 'C', 'M')
        self.gp_BFS_P.adicionaAresta('a5', 'C', 'T')
        self.gp_BFS_P.adicionaAresta('a6', 'T', 'Z')

        self.gp_BFS_M = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_BFS_M.adicionaAresta('a1', 'M', 'C')
        self.gp_BFS_M.adicionaAresta('a2', 'M', 'T')
        self.gp_BFS_M.adicionaAresta('a3', 'C', 'J')
        self.gp_BFS_M.adicionaAresta('a4', 'C', 'E')
        self.gp_BFS_M.adicionaAresta('a5', 'C', 'P')
        self.gp_BFS_M.adicionaAresta('a6', 'T', 'Z')

        self.gp_BFS_T = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_BFS_T.adicionaAresta('a1', 'T', 'C')
        self.gp_BFS_T.adicionaAresta('a2', 'T', 'M')
        self.gp_BFS_T.adicionaAresta('a3', 'T', 'Z')
        self.gp_BFS_T.adicionaAresta('a4', 'C', 'J')
        self.gp_BFS_T.adicionaAresta('a5', 'C', 'E')
        self.gp_BFS_T.adicionaAresta('a6', 'C', 'P')

        self.gp_BFS_Z = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.gp_BFS_Z.adicionaAresta('a1', 'Z', 'T')
        self.gp_BFS_Z.adicionaAresta('a2', 'T', 'C')
        self.gp_BFS_Z.adicionaAresta('a3', 'T', 'M')
        self.gp_BFS_Z.adicionaAresta('a4', 'C', 'J')
        self.gp_BFS_Z.adicionaAresta('a5', 'C', 'E')
        self.gp_BFS_Z.adicionaAresta('a6', 'C', 'P')

        self.grafodeeuler= MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafodeeuler.adicionaAresta('a1', 'A', 'B')
        self.grafodeeuler.adicionaAresta('a2', 'A', 'C')
        self.grafodeeuler.adicionaAresta('a3', 'A', 'D')
        self.grafodeeuler.adicionaAresta('a4', 'A', 'F')
        self.grafodeeuler.adicionaAresta('a5', 'B', 'C')
        self.grafodeeuler.adicionaAresta('a6', 'B', 'E')
        self.grafodeeuler.adicionaAresta('a7', 'B', 'G')
        self.grafodeeuler.adicionaAresta('a8', 'E', 'F')
        self.grafodeeuler.adicionaAresta('a9', 'F', 'G')

        #grafos com pesos
        self.grafo3 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafo3.adicionaAresta('a1', 'A', 'B', 1)
        self.grafo3.adicionaAresta('a2', 'B', 'C', 2)
        self.grafo3.adicionaAresta('a3', 'A', 'D', 3)
        self.grafo3.adicionaAresta('a4', 'D', 'E', 2)
        self.grafo3.adicionaAresta('a5', 'E', 'F', 4)
        self.grafo3.adicionaAresta('a6', 'E', 'G', 1)
        self.grafo3.adicionaAresta('a7', 'B', 'G', 5)
        self.grafo3.adicionaAresta('a8', 'F', 'G', 3)
        self.grafo3.adicionaAresta('a9', 'C', 'G', 2)
        self.grafo3.adicionaAresta('a10', 'D', 'G', 3)

        self.grafo5 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        self.grafo5.adicionaAresta('a1', 'A', 'B', 9)
        self.grafo5.adicionaAresta('a2', 'B', 'C', 6)
        self.grafo5.adicionaAresta('a3', 'A', 'G', 4)
        self.grafo5.adicionaAresta('a4', 'D', 'E', 14)
        self.grafo5.adicionaAresta('a5', 'F', 'E', 2)
        self.grafo5.adicionaAresta('a6', 'C', 'E', 12)
        self.grafo5.adicionaAresta('a7', 'B', 'G', 10)
        self.grafo5.adicionaAresta('a8', 'G', 'F', 1)
        self.grafo5.adicionaAresta('a9', 'C', 'F', 8)
        self.grafo5.adicionaAresta('a10', 'D', 'C', 8)
        self.grafo5.adicionaAresta('a11', 'H', 'F', 2)
        self.grafo5.adicionaAresta('a12', 'B', 'H', 7)

        self.paraiba_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.paraiba_sem_paralelas.adicionaAresta('a1', 'J', 'C', 1)
        self.paraiba_sem_paralelas.adicionaAresta('a2', 'C', 'E', 2)
        self.paraiba_sem_paralelas.adicionaAresta('a3', 'C', 'P', 1)
        self.paraiba_sem_paralelas.adicionaAresta('a4', 'C', 'T', 2)
        self.paraiba_sem_paralelas.adicionaAresta('a5', 'C', 'M', 4)
        self.paraiba_sem_paralelas.adicionaAresta('a6', 'M', 'T', 5)
        self.paraiba_sem_paralelas.adicionaAresta('a7', 'T', 'Z', 7)

        self.pb_completo = MeuGrafo(['J', 'C', 'E', 'P'])
        self.pb_completo.adicionaAresta('a1', 'J', 'C', 6)
        self.pb_completo.adicionaAresta('a2', 'J', 'E', 4)
        self.pb_completo.adicionaAresta('a3', 'J', 'P', 7)
        self.pb_completo.adicionaAresta('a4', 'E', 'C', 1)
        self.pb_completo.adicionaAresta('a5', 'P', 'C', 2)
        self.pb_completo.adicionaAresta('a6', 'P', 'E', 3)

        self.grafoDirecionado_peso = MeuGrafo(['A', 'B', 'C', 'D'])
        self.grafoDirecionado_peso.adicionaAresta('a1', 'A', 'B', 2)
        self.grafoDirecionado_peso.adicionaAresta('a2', 'A', 'C', 3)
        self.grafoDirecionado_peso.adicionaAresta('a3', 'C', 'A', 4)
        self.grafoDirecionado_peso.adicionaAresta('a4', 'B', 'C', 5)
        self.grafoDirecionado_peso.adicionaAresta('a5', 'C', 'D', 7)

        self.paraiba_peso = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.paraiba_peso.adicionaAresta('a1', 'J', 'C', 1)
        self.paraiba_peso.adicionaAresta('a2', 'C', 'E', 3)
        self.paraiba_peso.adicionaAresta('a3', 'C', 'E', 5)
        self.paraiba_peso.adicionaAresta('a4', 'P', 'C', 7)
        self.paraiba_peso.adicionaAresta('a5', 'P', 'C', 2)
        self.paraiba_peso.adicionaAresta('a6', 'T', 'C', 5)
        self.paraiba_peso.adicionaAresta('a7', 'M', 'C', 4)
        self.paraiba_peso.adicionaAresta('a8', 'M', 'T', 4)
        self.paraiba_peso.adicionaAresta('a9', 'T', 'Z', 3)

        #Grafos resultantes do algoritmo de PRIM
        self.grafo3_prim = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafo3_prim.adicionaAresta('a1', 'A', 'B', 1)
        self.grafo3_prim.adicionaAresta('a2', 'B', 'C', 2)
        self.grafo3_prim.adicionaAresta('a9', 'C', 'G', 2)
        self.grafo3_prim.adicionaAresta('a6', 'E', 'G', 1)
        self.grafo3_prim.adicionaAresta('a4', 'D', 'E', 2)
        self.grafo3_prim.adicionaAresta('a8', 'F', 'G', 3)

        self.grafo5_prim = MeuGrafo(['G','F', 'E', 'H', 'A', 'B', 'C', 'D'])
        self.grafo5_prim.adicionaAresta('a8', 'G', 'F', 1)
        self.grafo5_prim.adicionaAresta('a5', 'F', 'E', 2)
        self.grafo5_prim.adicionaAresta('a11', 'H', 'F', 2)
        self.grafo5_prim.adicionaAresta('a3', 'A', 'G', 4)
        self.grafo5_prim.adicionaAresta('a12', 'B', 'H', 7)
        self.grafo5_prim.adicionaAresta('a2', 'B', 'C', 6)
        self.grafo5_prim.adicionaAresta('a10', 'D', 'C', 8)

        self.paraiba_sem_paralelas_prim = MeuGrafo(['J', 'C', 'P', 'E', 'T', 'M', 'Z'])
        self.paraiba_sem_paralelas_prim.adicionaAresta('a1', 'J', 'C', 1)
        self.paraiba_sem_paralelas_prim.adicionaAresta('a3', 'C', 'P', 1)
        self.paraiba_sem_paralelas_prim.adicionaAresta('a2', 'C', 'E', 2)
        self.paraiba_sem_paralelas_prim.adicionaAresta('a4', 'C', 'T', 2)
        self.paraiba_sem_paralelas_prim.adicionaAresta('a5', 'C', 'M', 4)
        self.paraiba_sem_paralelas_prim.adicionaAresta('a7', 'T', 'Z', 7)

        self.pb_completo_prim = MeuGrafo(['E', 'C', 'P', 'J'])
        self.pb_completo_prim.adicionaAresta('a4', 'E', 'C', 1)
        self.pb_completo_prim.adicionaAresta('a5', 'P', 'C', 2)
        self.pb_completo_prim.adicionaAresta('a2', 'J', 'E', 4)

        self.grafoDirecionado_prim = MeuGrafo(['A', 'B', 'C', 'D'])
        self.grafoDirecionado_prim.adicionaAresta('a1', 'A', 'B', 2)
        self.grafoDirecionado_prim.adicionaAresta('a2', 'A', 'C', 3)
        self.grafoDirecionado_prim.adicionaAresta('a5', 'C', 'D', 7)

        #Grafos resultantes do algoritmo de Kruskall modificado
        self.grafo5_kruskall = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        self.grafo5_kruskall.adicionaAresta('a8', 'G', 'F', 1)
        self.grafo5_kruskall.adicionaAresta('a5', 'F', 'E', 2)
        self.grafo5_kruskall.adicionaAresta('a11', 'H', 'F', 2)
        self.grafo5_kruskall.adicionaAresta('a3', 'A', 'G', 4)
        self.grafo5_kruskall.adicionaAresta('a12', 'B', 'H', 7)
        self.grafo5_kruskall.adicionaAresta('a2', 'B', 'C', 6)
        self.grafo5_kruskall.adicionaAresta('a10', 'D', 'C', 8)

        self.paraiba_kruskall = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.paraiba_kruskall.adicionaAresta('a1', 'J', 'C', 1)
        self.paraiba_kruskall.adicionaAresta('a5', 'P', 'C', 2)
        self.paraiba_kruskall.adicionaAresta('a2', 'C', 'E', 3)
        self.paraiba_kruskall.adicionaAresta('a9', 'T', 'Z', 3)
        self.paraiba_kruskall.adicionaAresta('a7', 'M', 'C', 4)
        self.paraiba_kruskall.adicionaAresta('a8', 'M', 'T', 4)

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a6', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_p.dfs('J'),self.gp_DFS_J)
        self.assertEqual(self.g_p.dfs('C'), self.gp_DFS_C)
        self.assertEqual(self.g_p.dfs('E'), self.gp_DFS_E)
        self.assertEqual(self.g_p.dfs('P'), self.gp_DFS_P)
        self.assertEqual(self.g_p.dfs('M'), self.gp_DFS_M)
        self.assertEqual(self.g_p.dfs('T'), self.gp_DFS_T)
        self.assertEqual(self.g_p.dfs('Z'), self.gp_DFS_Z)

    def test_bfs(self):
        self.assertEqual(self.g_p.bfs('J'),self.gp_BFS_J)
        self.assertEqual(self.g_p.bfs('C'), self.gp_BFS_C)
        self.assertEqual(self.g_p.bfs('E'), self.gp_BFS_E)
        self.assertEqual(self.g_p.bfs('P'), self.gp_BFS_P)
        self.assertEqual(self.g_p.bfs('M'), self.gp_BFS_M)
        self.assertEqual(self.g_p.bfs('T'), self.gp_BFS_T)
        self.assertEqual(self.g_p.bfs('Z'), self.gp_BFS_Z)

    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue((self.g_p_sem_paralelas.conexo()))
        self.assertTrue((self.g_c.conexo()))
        self.assertTrue((self.g_c2.conexo()))
        self.assertFalse((self.g_c3.conexo()))
        self.assertFalse((self.g_l1.conexo()))
        self.assertFalse((self.g_l2.conexo()))
        self.assertFalse((self.g_l3.conexo()))
        self.assertTrue((self.g_l4.conexo()))
        self.assertTrue((self.g_l5.conexo()))
        self.assertFalse((self.g_d.conexo()))

    def test_ha_ciclo(self):
        self.assertEqual(self.g_p.ha_ciclo(), ['C','a2','E','a3','C'])
        self.assertEqual(self.g_p_sem_paralelas.ha_ciclo(), ['C', 'a4', 'T', 'a6', 'M', 'a5', 'C'])
        self.assertEqual(self.g_c.ha_ciclo(), ['J', 'a1', 'C', 'a4', 'E', 'a2', 'J'])
        self.assertEqual(self.g_l3.ha_ciclo(), ['C', 'a2', 'C'])
        self.assertFalse(self.g_d.ha_ciclo())

    def test_caminho(self):
        self.assertEqual(self.g_p.caminho(1),['J','a1','C'])
        self.assertEqual(self.g_p.caminho(2),['J', 'a1', 'C','a2','E'])
        self.assertEqual(self.g_p.caminho(3),['J','a1','C','a6','M','a8','T'])
        self.assertEqual(self.g_p.caminho(4),['J', 'a1', 'C','a6','M','a8','T','a9','Z'])
        self.assertEqual(self.g_p.caminho(5),[])
        self.assertEqual(self.g_c.caminho(2), ['J', 'a1', 'C','a4','E'])
        self.assertEqual(self.g_c.caminho(3), ['J','a1','C','a4','E','a6','P'])
        self.assertEqual(self.g_l1.caminho(1), ['A', 'a2', 'B'])
        self.assertEqual(self.g_l1.caminho(2), [])

    def test_caminho_euleriano(self):
        self.assertEqual(self.grafodeeuler.caminho_euleriano(), ['F', 'a4', 'A', 'a1', 'B', 'a5', 'C', 'a2', 'A', 'a3', 'D', 'B', 'a6', 'E', 'a8', 'F', 'a9', 'G', 'a7', 'B'])
        self.assertEqual(self.g_p.caminho_euleriano(),'Caminho de Euler não existe no grafo')
        self.assertEqual(self.g_l1.caminho_euleriano(),'o grafo nao é conexo, tente com outro!')
        self.assertEqual(self.g_l2.caminho_euleriano(),'o grafo nao é conexo, tente com outro!')
        self.assertEqual(self.g_l3.caminho_euleriano(),'o grafo nao é conexo, tente com outro!')
        self.assertEqual(self.g_p_sem_paralelas.caminho_euleriano(),'Caminho de Euler não existe no grafo')
        self.assertEqual(self.g_d.caminho_euleriano(),'o grafo nao é conexo, tente com outro!')
        self.assertEqual(self.g_c.caminho_euleriano(),'Caminho de Euler não existe no grafo')
        self.assertEqual(self.g_l4.caminho_euleriano(),['D', 'a1', 'D'])
        self.assertEqual(self.g_p2.caminho_euleriano(),['C', 'a2', 'E', 'a3', 'C', 'a4', 'P', 'a5', 'C', 'a6', 'M', 'a8', 'T', 'a7', 'C'])


    def test_Prim_modificado(self):
        self.assertEqual(self.grafo3.Prim_modificado(), self.grafo3_prim)
        self.assertEqual(self.grafo5.Prim_modificado(), self.grafo5_prim)
        self.assertEqual(self.paraiba_sem_paralelas.Prim_modificado(), self.paraiba_sem_paralelas_prim)
        self.assertEqual(self.pb_completo.Prim_modificado(), self.pb_completo_prim)
        self.assertEqual(self.g_d.Prim_modificado(), "Grafo não possui árvore geradora mínima ,pois não é CONEXO!")
        self.assertEqual(self.grafoDirecionado_peso.Prim_modificado(), self.grafoDirecionado_prim)

    def test_Kruskall_modificado(self):
        self.assertEqual(self.grafo3.Kruskall_modificado(), self.grafo3_prim)
        self.assertEqual(self.grafo5.Kruskall_modificado(), self.grafo5_kruskall)
        self.assertEqual(self.paraiba_peso.Kruskall_modificado(), self.paraiba_kruskall)
        self.assertEqual(self.g_d.Kruskall_modificado(), "Grafo não possui árvore geradora mínima ,pois não é CONEXO!")
        self.assertEqual(self.grafoDirecionado_peso.Kruskall_modificado(), self.grafoDirecionado_prim)


















