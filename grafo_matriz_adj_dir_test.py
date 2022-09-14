import unittest
from meu_grafo_matriz_adjacencia_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
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

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.g_e.adicionaAresta('1', 'A', 'B')
        self.g_e.adicionaAresta('2', 'A', 'C')
        self.g_e.adicionaAresta('3', 'C', 'A')
        self.g_e.adicionaAresta('4', 'C', 'B')
        self.g_e.adicionaAresta('10', 'C', 'B')
        self.g_e.adicionaAresta('5', 'C', 'D')
        self.g_e.adicionaAresta('6', 'D', 'D')
        self.g_e.adicionaAresta('7', 'D', 'B')
        self.g_e.adicionaAresta('8', 'D', 'E')
        self.g_e.adicionaAresta('9', 'E', 'A')
        self.g_e.adicionaAresta('11', 'E', 'B')

        # Matrizes para teste do algoritmo de Warshall

        self.g_p_m = self.constroi_matriz(self.g_p)
        self.g_p_m[0][1] = 1
        self.g_p_m[0][2] = 1
        self.g_p_m[1][2] = 1
        self.g_p_m[3][1] = 1
        self.g_p_m[3][2] = 1
        self.g_p_m[4][1] = 1
        self.g_p_m[4][2] = 1
        self.g_p_m[4][5] = 1
        self.g_p_m[4][6] = 1
        self.g_p_m[5][1] = 1
        self.g_p_m[5][2] = 1
        self.g_p_m[5][6] = 1

        self.g_e_m = self.constroi_matriz(self.g_e)
        for i in range(0, len(self.g_e_m)):
            self.g_e_m[0][i] = 1
            self.g_e_m[2][i] = 1
            self.g_e_m[3][i] = 1
            self.g_e_m[4][i] = 1

        # Grafos test de Warshall
        self.warshall_grafoDirecionado = MeuGrafo(['A', 'B', 'C', 'D'])
        self.warshall_grafoDirecionado = MeuGrafo(['A', 'B', 'C', 'D'])
        self.warshall_grafoDirecionado.adicionaAresta('a3', 'A', 'A')
        self.warshall_grafoDirecionado.adicionaAresta('a1', 'A', 'B')
        self.warshall_grafoDirecionado.adicionaAresta('a4', 'A', 'C')
        self.warshall_grafoDirecionado.adicionaAresta('a5', 'A', 'D')
        self.warshall_grafoDirecionado.adicionaAresta('a3', 'B', 'A')
        self.warshall_grafoDirecionado.adicionaAresta('a1', 'B', 'B')
        self.warshall_grafoDirecionado.adicionaAresta('a4', 'B', 'C')
        self.warshall_grafoDirecionado.adicionaAresta('a5', 'B', 'D')
        self.warshall_grafoDirecionado.adicionaAresta('a3', 'C', 'A')
        self.warshall_grafoDirecionado.adicionaAresta('a1', 'C', 'B')
        self.warshall_grafoDirecionado.adicionaAresta('a4', 'C', 'C')
        self.warshall_grafoDirecionado.adicionaAresta('a5', 'C', 'D')

        self.warshall_paraiba = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.warshall_paraiba.adicionaAresta('a5', 'J', 'C')
        self.warshall_paraiba.adicionaAresta('a2', 'J', 'E')
        self.warshall_paraiba.adicionaAresta('a4', 'J', 'P')
        self.warshall_paraiba.adicionaAresta('a6', 'J', 'M')
        self.warshall_paraiba.adicionaAresta('a8', 'J', 'T')
        self.warshall_paraiba.adicionaAresta('a9', 'J', 'Z')
        self.warshall_paraiba.adicionaAresta('a5', 'C', 'C')
        self.warshall_paraiba.adicionaAresta('a2', 'C', 'E')
        self.warshall_paraiba.adicionaAresta('a4', 'C', 'P')
        self.warshall_paraiba.adicionaAresta('a6', 'C', 'M')
        self.warshall_paraiba.adicionaAresta('a8', 'C', 'T')
        self.warshall_paraiba.adicionaAresta('a9', 'C', 'Z')
        self.warshall_paraiba.adicionaAresta('a5', 'E', 'C')
        self.warshall_paraiba.adicionaAresta('a2', 'E', 'E')
        self.warshall_paraiba.adicionaAresta('a4', 'E', 'P')
        self.warshall_paraiba.adicionaAresta('a6', 'E', 'M')
        self.warshall_paraiba.adicionaAresta('a8', 'E', 'T')
        self.warshall_paraiba.adicionaAresta('a9', 'E', 'Z')
        self.warshall_paraiba.adicionaAresta('a5', 'P', 'C')
        self.warshall_paraiba.adicionaAresta('a2', 'P', 'E')
        self.warshall_paraiba.adicionaAresta('a4', 'P', 'P')
        self.warshall_paraiba.adicionaAresta('a6', 'P', 'M')
        self.warshall_paraiba.adicionaAresta('a8', 'P', 'T')
        self.warshall_paraiba.adicionaAresta('a9', 'P', 'Z')
        self.warshall_paraiba.adicionaAresta('a8', 'M', 'T')
        self.warshall_paraiba.adicionaAresta('a9', 'M', 'Z')
        self.warshall_paraiba.adicionaAresta('a9', 'T', 'Z')

        self.warshall_paraiba_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a2', 'J', 'E')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a3', 'J', 'P')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a5', 'J', 'M')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a6', 'J', 'T')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a7', 'J', 'Z')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a3', 'C', 'P')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a5', 'C', 'M')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a6', 'C', 'T')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a7', 'C', 'Z')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a7', 'M', 'Z')
        self.warshall_paraiba_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        self.warshall_pb_completo = MeuGrafo(['J', 'C', 'E', 'P'])
        self.warshall_pb_completo.adicionaAresta('a5', 'J', 'C')
        self.warshall_pb_completo.adicionaAresta('a6', 'J', 'E')
        self.warshall_pb_completo.adicionaAresta('a4', 'J', 'P')
        self.warshall_pb_completo.adicionaAresta('a5', 'E', 'C')
        self.warshall_pb_completo.adicionaAresta('a6', 'E', 'E')
        self.warshall_pb_completo.adicionaAresta('a4', 'E', 'P')
        self.warshall_pb_completo.adicionaAresta('a5', 'P', 'C')
        self.warshall_pb_completo.adicionaAresta('a6', 'P', 'E')
        self.warshall_pb_completo.adicionaAresta('a4', 'P', 'P')

        self.grafoDirecionado2=MeuGrafo(['A','B','C','D','E','F','G'])
        self.grafoDirecionado2.adicionaAresta('a1','A','B',2)
        self.grafoDirecionado2.adicionaAresta('a2','A','C',1)
        self.grafoDirecionado2.adicionaAresta('a3','B','D',1)
        self.grafoDirecionado2.adicionaAresta('a4','D','A',3)
        self.grafoDirecionado2.adicionaAresta('a5','C','D',4)
        self.grafoDirecionado2.adicionaAresta('a6','C','F',5)
        self.grafoDirecionado2.adicionaAresta('a7','D','F',2)
        self.grafoDirecionado2.adicionaAresta('a8','D','E',2)
        self.grafoDirecionado2.adicionaAresta('a9','E','G',10)
        self.grafoDirecionado2.adicionaAresta('a10','F','G',7)

        #Grafos testes ordenação topologica:

        #Grafo da matriz curricular Eng da Computação
        self.eng_computacao=MeuGrafo(['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33', '34', '35', '36', '41', '42', '43', '44', '45',
                                      '51','52','53','54','55','61','62','63','64','65','71','72','73','74','75','81','82','83','84','85','91','92','93','94','101','102','103'])
        self.eng_computacao.adicionaAresta('a1', '11', '21')
        self.eng_computacao.adicionaAresta('a2', '14', '24')
        self.eng_computacao.adicionaAresta('a3', '15', '24')
        self.eng_computacao.adicionaAresta('a4', '14', '25')
        self.eng_computacao.adicionaAresta('a5', '15', '25')
        self.eng_computacao.adicionaAresta('a6', '16', '26')
        self.eng_computacao.adicionaAresta('a7', '21', '31')
        self.eng_computacao.adicionaAresta('a8', '24', '33')
        self.eng_computacao.adicionaAresta('a9', '14', '34')
        self.eng_computacao.adicionaAresta('a10', '15', '34')
        self.eng_computacao.adicionaAresta('a11', '14', '35')
        self.eng_computacao.adicionaAresta('a12', '15', '35')
        self.eng_computacao.adicionaAresta('a13', '26', '36')
        self.eng_computacao.adicionaAresta('a14', '21', '41')
        self.eng_computacao.adicionaAresta('a15', '24', '43')
        self.eng_computacao.adicionaAresta('a16', '24', '44')
        self.eng_computacao.adicionaAresta('a17', '36', '44')
        self.eng_computacao.adicionaAresta('a18', '36', '45')
        self.eng_computacao.adicionaAresta('a19', '31', '51')
        self.eng_computacao.adicionaAresta('a20', '31', '52')
        self.eng_computacao.adicionaAresta('a21', '24', '53')
        self.eng_computacao.adicionaAresta('a22', '24', '54')
        self.eng_computacao.adicionaAresta('a23', '36', '55')
        self.eng_computacao.adicionaAresta('a24', '44', '55')
        self.eng_computacao.adicionaAresta('a25', '51', '61')
        self.eng_computacao.adicionaAresta('a26', '43', '62')
        self.eng_computacao.adicionaAresta('a27', '34', '63')
        self.eng_computacao.adicionaAresta('a28', '35', '63')
        self.eng_computacao.adicionaAresta('a29', '31', '64')
        self.eng_computacao.adicionaAresta('a30', '55', '65')
        self.eng_computacao.adicionaAresta('a31', '24', '72')
        self.eng_computacao.adicionaAresta('a32', '63', '73')
        self.eng_computacao.adicionaAresta('a33', '52', '75')
        self.eng_computacao.adicionaAresta('a34', '64', '75')
        self.eng_computacao.adicionaAresta('a35', '34', '81')
        self.eng_computacao.adicionaAresta('a36', '35', '81')
        self.eng_computacao.adicionaAresta('a37', '54', '81')
        self.eng_computacao.adicionaAresta('a38', '73', '82')
        self.eng_computacao.adicionaAresta('a39', '74', '83')
        self.eng_computacao.adicionaAresta('a40', '61', '84')
        self.eng_computacao.adicionaAresta('a41', '64', '84')
        self.eng_computacao.adicionaAresta('a42', '75', '85')
        self.eng_computacao.adicionaAresta('a43', '83', '92')
        self.eng_computacao.adicionaAresta('a44', '44', '93')
        self.eng_computacao.adicionaAresta('a45', '45', '93')
        self.eng_computacao.adicionaAresta('a46', '61', '94')
        self.eng_computacao.adicionaAresta('a47', '75', '94')
        self.eng_computacao.adicionaAresta('a48', '92', '103')

        # Grafo da matriz curricular Construção de Edificios
        self.construcao_edificios = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17','18', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33', '34',
             '35', '36','37','38', '41', '42', '43', '44', '45','46','47','51', '52', '53', '54', '55','56','57','58', '61', '62', '63', '64', '65','66','67','68', '71', '72', '73'])
        self.construcao_edificios.adicionaAresta('a1', '15', '21')
        self.construcao_edificios.adicionaAresta('a2', '14', '23')
        self.construcao_edificios.adicionaAresta('a3', '11', '24')
        self.construcao_edificios.adicionaAresta('a4', '17', '24')
        self.construcao_edificios.adicionaAresta('a5', '15', '25')
        self.construcao_edificios.adicionaAresta('a6', '17', '26')
        self.construcao_edificios.adicionaAresta('a7', '17', '27')
        self.construcao_edificios.adicionaAresta('a8', '15', '32')
        self.construcao_edificios.adicionaAresta('a9', '21', '32')
        self.construcao_edificios.adicionaAresta('a10', '21', '33')
        self.construcao_edificios.adicionaAresta('a11', '25', '33')
        self.construcao_edificios.adicionaAresta('a12', '15', '44')
        self.construcao_edificios.adicionaAresta('a13', '11', '35')
        self.construcao_edificios.adicionaAresta('a14', '27', '35')
        self.construcao_edificios.adicionaAresta('a15', '26', '36')
        self.construcao_edificios.adicionaAresta('a16', '23', '37')
        self.construcao_edificios.adicionaAresta('a17', '24', '38')
        self.construcao_edificios.adicionaAresta('a18', '17', '41')
        self.construcao_edificios.adicionaAresta('a19', '21', '41')
        self.construcao_edificios.adicionaAresta('a20', '17', '42')
        self.construcao_edificios.adicionaAresta('a21', '21', '42')
        self.construcao_edificios.adicionaAresta('a22', '23', '43')
        self.construcao_edificios.adicionaAresta('a23', '24', '44')
        self.construcao_edificios.adicionaAresta('a24', '36', '45')
        self.construcao_edificios.adicionaAresta('a25', '37', '45')
        self.construcao_edificios.adicionaAresta('a26', '17', '46')
        self.construcao_edificios.adicionaAresta('a27', '32', '46')
        self.construcao_edificios.adicionaAresta('a28', '11', '47')
        self.construcao_edificios.adicionaAresta('a29', '37', '47')
        self.construcao_edificios.adicionaAresta('a30', '37', '51')
        self.construcao_edificios.adicionaAresta('a31', '43', '51')
        self.construcao_edificios.adicionaAresta('a32', '45', '51')
        self.construcao_edificios.adicionaAresta('a33', '46', '51')
        self.construcao_edificios.adicionaAresta('a34', '41', '52')
        self.construcao_edificios.adicionaAresta('a35', '42', '52')
        self.construcao_edificios.adicionaAresta('a36', '45', '52')
        self.construcao_edificios.adicionaAresta('a37', '46', '52')
        self.construcao_edificios.adicionaAresta('a38', '17', '53')
        self.construcao_edificios.adicionaAresta('a39', '32', '53')
        self.construcao_edificios.adicionaAresta('a40', '47', '54')
        self.construcao_edificios.adicionaAresta('a41', '17', '55')
        self.construcao_edificios.adicionaAresta('a42', '32', '55')
        self.construcao_edificios.adicionaAresta('a43', '46', '56')
        self.construcao_edificios.adicionaAresta('a44', '43', '57')
        self.construcao_edificios.adicionaAresta('a45', '31', '62')
        self.construcao_edificios.adicionaAresta('a46', '44', '62')
        self.construcao_edificios.adicionaAresta('a47', '22', '64')
        self.construcao_edificios.adicionaAresta('a48', '27', '64')
        self.construcao_edificios.adicionaAresta('a49', '33', '64')
        self.construcao_edificios.adicionaAresta('a50', '36', '64')
        self.construcao_edificios.adicionaAresta('a51', '47', '65')
        self.construcao_edificios.adicionaAresta('a52', '22', '66')
        self.construcao_edificios.adicionaAresta('a53', '31', '67')

        # Grafo da matriz curricular Fisica
        self.fisica = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17','21', '22', '23', '24', '25', '26', '27', '31', '32', '33',
             '34','35', '36', '37', '41', '42', '43', '44', '45', '46', '51', '52', '53', '54', '55', '56', '57',
             '61', '62', '63', '64', '65', '66', '68', '71', '72', '73','74','75','76','81','82','83','84','85','86'])
        self.fisica.adicionaAresta('a1', '11', '21')
        self.fisica.adicionaAresta('a2', '12', '21')
        self.fisica.adicionaAresta('a3', '11', '22')
        self.fisica.adicionaAresta('a4', '12', '22')
        self.fisica.adicionaAresta('a5', '12', '23')
        self.fisica.adicionaAresta('a6', '12', '24')
        self.fisica.adicionaAresta('a7', '14', '24')
        self.fisica.adicionaAresta('a8', '15', '25')
        self.fisica.adicionaAresta('a9', '21', '31')
        self.fisica.adicionaAresta('a10', '23', '31')
        self.fisica.adicionaAresta('a11', '21', '32')
        self.fisica.adicionaAresta('a12', '22', '32')
        self.fisica.adicionaAresta('a13', '23', '33')
        self.fisica.adicionaAresta('a14', '31', '41')
        self.fisica.adicionaAresta('a15', '31', '42')
        self.fisica.adicionaAresta('a16', '32', '42')
        self.fisica.adicionaAresta('a17', '33', '45')
        self.fisica.adicionaAresta('a18', '31', '46')
        self.fisica.adicionaAresta('a19', '41', '51')
        self.fisica.adicionaAresta('a20', '45', '51')
        self.fisica.adicionaAresta('a21', '41', '52')
        self.fisica.adicionaAresta('a22', '42', '52')
        self.fisica.adicionaAresta('a23', '45', '53')
        self.fisica.adicionaAresta('a24', '31', '54')
        self.fisica.adicionaAresta('a25', '43', '55')
        self.fisica.adicionaAresta('a26', '51', '61')
        self.fisica.adicionaAresta('a27', '51', '62')
        self.fisica.adicionaAresta('a28', '52', '62')
        self.fisica.adicionaAresta('a29', '21', '63')
        self.fisica.adicionaAresta('a30', '53', '63')
        self.fisica.adicionaAresta('a31', '51', '64')
        self.fisica.adicionaAresta('a32', '56', '66')
        self.fisica.adicionaAresta('a33', '61', '71')
        self.fisica.adicionaAresta('a34', '41', '72')
        self.fisica.adicionaAresta('a35', '45', '72')
        self.fisica.adicionaAresta('a36', '66', '73')
        self.fisica.adicionaAresta('a37', '31', '74')
        self.fisica.adicionaAresta('a38', '43', '74')
        self.fisica.adicionaAresta('a39', '65', '81')
        self.fisica.adicionaAresta('a40', '74', '82')
        self.fisica.adicionaAresta('a41', '73', '83')
        self.fisica.adicionaAresta('a42', '54', '84')
        self.fisica.adicionaAresta('a43', '71', '84')
        self.fisica.adicionaAresta('a44', '16', '85')
        self.fisica.adicionaAresta('a45', '25', '85')
        self.fisica.adicionaAresta('a46', '21', '57')
        self.fisica.adicionaAresta('a47', '43', '57')
        self.fisica.adicionaAresta('a48', '31', '68')
        self.fisica.adicionaAresta('a49', '57', '68')
        self.fisica.adicionaAresta('a50', '41', '76')
        self.fisica.adicionaAresta('a51', '68', '76')
        self.fisica.adicionaAresta('a52', '51', '86')
        self.fisica.adicionaAresta('a53', '76', '86')

        # Grafo da matriz curricular LETRAS
        self.letras = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33',
             '34', '35', '36', '37', '41', '42', '43', '44', '45', '46','47', '51', '52', '53', '54', '55', '56', '57',
             '61', '62', '63', '64', '65', '66','67', '68', '71', '72', '73', '74', '75', '76','77','78', '81', '82', '83', '84', '85',
             '86','87','88'])
        self.letras.adicionaAresta('a1', '11', '21')
        self.letras.adicionaAresta('a2', '11', '22')
        self.letras.adicionaAresta('a3', '12', '23')
        self.letras.adicionaAresta('a4', '12', '25')
        self.letras.adicionaAresta('a5', '17', '26')
        self.letras.adicionaAresta('a6', '21', '31')
        self.letras.adicionaAresta('a7', '21', '32')
        self.letras.adicionaAresta('a8', '21', '33')
        self.letras.adicionaAresta('a9', '24', '34')
        self.letras.adicionaAresta('a10', '25', '35')
        self.letras.adicionaAresta('a11', '31', '41')
        self.letras.adicionaAresta('a12', '33', '42')
        self.letras.adicionaAresta('a13', '25', '43')
        self.letras.adicionaAresta('a14', '25', '44')
        self.letras.adicionaAresta('a15', '36', '44')
        self.letras.adicionaAresta('a16', '23', '46')
        self.letras.adicionaAresta('a17', '35', '46')
        self.letras.adicionaAresta('a18', '37', '47')
        self.letras.adicionaAresta('a19', '31', '51')
        self.letras.adicionaAresta('a20', '35', '52')
        self.letras.adicionaAresta('a21', '13', '53')
        self.letras.adicionaAresta('a22', '45', '54')
        self.letras.adicionaAresta('a23', '35', '55')
        self.letras.adicionaAresta('a24', '22', '56')
        self.letras.adicionaAresta('a25', '37', '57')
        self.letras.adicionaAresta('a26', '31', '61')
        self.letras.adicionaAresta('a27', '31', '62')
        self.letras.adicionaAresta('a28', '35', '63')
        self.letras.adicionaAresta('a29', '54', '64')
        self.letras.adicionaAresta('a30', '37', '67')
        self.letras.adicionaAresta('a31', '54', '68')
        self.letras.adicionaAresta('a32', '31', '71')
        self.letras.adicionaAresta('a33', '31', '72')
        self.letras.adicionaAresta('a34', '31', '73')
        self.letras.adicionaAresta('a35', '64', '74')
        self.letras.adicionaAresta('a36', '35', '75')
        self.letras.adicionaAresta('a37', '45', '76')
        self.letras.adicionaAresta('a38', '27', '77')
        self.letras.adicionaAresta('a39', '53', '77')
        self.letras.adicionaAresta('a40', '64', '78')
        self.letras.adicionaAresta('a41', '68', '78')
        self.letras.adicionaAresta('a42', '17', '83')
        self.letras.adicionaAresta('a43', '74', '84')
        self.letras.adicionaAresta('a44', '77', '87')
        self.letras.adicionaAresta('a45', '74', '88')
        self.letras.adicionaAresta('a46', '78', '88')

        # Grafo da matriz curricular Matemática
        self.matematica = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33',
             '34', '35', '36', '41', '42', '43', '44', '45', '46','51', '52', '53', '54', '55', '56', '57',
             '61', '62', '63', '64', '65', '66', '67', '71', '72', '73', '74', '75', '76', '77','81', '82',
             '83', '84', '85','86', '87'])
        self.matematica.adicionaAresta('a1', '11', '21')
        self.matematica.adicionaAresta('a2', '11', '22')
        self.matematica.adicionaAresta('a3', '13', '22')
        self.matematica.adicionaAresta('a4', '16', '26')
        self.matematica.adicionaAresta('a5', '21', '31')
        self.matematica.adicionaAresta('a6', '22', '32')
        self.matematica.adicionaAresta('a7', '12', '33')
        self.matematica.adicionaAresta('a8', '12', '34')
        self.matematica.adicionaAresta('a9', '21', '41')
        self.matematica.adicionaAresta('a10', '23', '41')
        self.matematica.adicionaAresta('a11', '23', '42')
        self.matematica.adicionaAresta('a12', '32', '42')
        self.matematica.adicionaAresta('a13', '36', '43')
        self.matematica.adicionaAresta('a14', '34', '44')
        self.matematica.adicionaAresta('a15', '27', '45')
        self.matematica.adicionaAresta('a16', '33', '51')
        self.matematica.adicionaAresta('a17', '12', '52')
        self.matematica.adicionaAresta('a18', '32', '53')
        self.matematica.adicionaAresta('a19', '44', '54')
        self.matematica.adicionaAresta('a20', '44', '55')
        self.matematica.adicionaAresta('a21', '44', '57')
        self.matematica.adicionaAresta('a22', '51', '61')
        self.matematica.adicionaAresta('a23', '52', '62')
        self.matematica.adicionaAresta('a24', '32', '63')
        self.matematica.adicionaAresta('a25', '54', '64')
        self.matematica.adicionaAresta('a26', '46', '65')
        self.matematica.adicionaAresta('a27', '57', '67')
        self.matematica.adicionaAresta('a28', '42', '71')
        self.matematica.adicionaAresta('a29', '22', '72')
        self.matematica.adicionaAresta('a30', '41', '73')
        self.matematica.adicionaAresta('a31', '42', '73')
        self.matematica.adicionaAresta('a32', '64', '74')
        self.matematica.adicionaAresta('a33', '65', '75')
        self.matematica.adicionaAresta('a34', '67', '77')
        self.matematica.adicionaAresta('a35', '62', '81')
        self.matematica.adicionaAresta('a36', '75', '82')
        self.matematica.adicionaAresta('a37', '32', '83')
        self.matematica.adicionaAresta('a38', '74', '84')
        self.matematica.adicionaAresta('a39', '77', '87')

        # Grafo da matriz curricular Telemática
        self.telematica = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33',
             '34', '35','36','37', '41', '42', '43', '44', '45', '46','47', '51', '52', '53', '54', '55', '56', '57',
             '61', '62', '63', '64', '65', '66'])
        self.telematica.adicionaAresta('a1', '11', '21')
        self.telematica.adicionaAresta('a2', '12', '22')
        self.telematica.adicionaAresta('a3', '16', '22')
        self.telematica.adicionaAresta('a4', '12', '23')
        self.telematica.adicionaAresta('a5', '16', '23')
        self.telematica.adicionaAresta('a6', '13', '24')
        self.telematica.adicionaAresta('a7', '16', '26')
        self.telematica.adicionaAresta('a8', '21', '31')
        self.telematica.adicionaAresta('a9', '26', '32')
        self.telematica.adicionaAresta('a10', '22', '33')
        self.telematica.adicionaAresta('a11', '23', '33')
        self.telematica.adicionaAresta('a12', '26', '33')
        self.telematica.adicionaAresta('a13', '14', '34')
        self.telematica.adicionaAresta('a14', '25', '35')
        self.telematica.adicionaAresta('a15', '21', '36')
        self.telematica.adicionaAresta('a16', '24', '36')
        self.telematica.adicionaAresta('a17', '31', '41')
        self.telematica.adicionaAresta('a18', '31', '42')
        self.telematica.adicionaAresta('a19', '32', '43')
        self.telematica.adicionaAresta('a20', '32', '44')
        self.telematica.adicionaAresta('a21', '33', '44')
        self.telematica.adicionaAresta('a22', '33', '45')
        self.telematica.adicionaAresta('a23', '21', '46')
        self.telematica.adicionaAresta('a24', '34', '46')
        self.telematica.adicionaAresta('a25', '41', '51')
        self.telematica.adicionaAresta('a26', '41', '52')
        self.telematica.adicionaAresta('a27', '44', '53')
        self.telematica.adicionaAresta('a28', '44', '54')
        self.telematica.adicionaAresta('a29', '37', '55')
        self.telematica.adicionaAresta('a30', '41', '55')
        self.telematica.adicionaAresta('a31', '44', '55')
        self.telematica.adicionaAresta('a32', '42', '61')
        self.telematica.adicionaAresta('a33', '51', '61')
        self.telematica.adicionaAresta('a34', '53', '62')


    def constroi_matriz(self, g: MeuGrafo):
        ordem = len(g.N)
        m = list()
        for i in range(ordem):
            m.append(list())
            for j in range(ordem):
                m[i].append(0)
        return m

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

    def test_eq(self):
        g_p_eq = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        g_p_eq.adicionaAresta('a1', 'J', 'C')
        g_p_eq.adicionaAresta('a2', 'C', 'E')
        g_p_eq.adicionaAresta('a3', 'C', 'E')
        g_p_eq.adicionaAresta('a4', 'P', 'C')
        g_p_eq.adicionaAresta('a5', 'P', 'C')
        g_p_eq.adicionaAresta('a6', 'T', 'C')
        g_p_eq.adicionaAresta('a7', 'M', 'C')
        g_p_eq.adicionaAresta('a8', 'M', 'T')
        g_p_eq.adicionaAresta('a9', 'T', 'Z')

        g_p_neq = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        g_p_neq.adicionaAresta('a1', 'C', 'C')
        g_p_neq.adicionaAresta('a2', 'C', 'E')
        g_p_neq.adicionaAresta('a3', 'C', 'E')
        g_p_neq.adicionaAresta('a4', 'P', 'C')
        g_p_neq.adicionaAresta('a5', 'P', 'C')
        g_p_neq.adicionaAresta('a6', 'T', 'C')
        g_p_neq.adicionaAresta('a7', 'M', 'C')
        g_p_neq.adicionaAresta('a8', 'M', 'T')
        g_p_neq.adicionaAresta('a9', 'T', 'Z')

        g_p_neq2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])

        self.assertEqual(self.g_p, g_p_eq)
        self.assertNotEqual(self.g_p, g_p_neq)
        self.assertNotEqual(self.g_p, g_p_neq2)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(set(self.g_p.vertices_nao_adjacentes()), {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-J', 'C-T', 'C-Z', 'C-M', 'C-P', 'E-C', 'E-J', 'E-P',
                                                                   'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J',
                                                                   'T-M', 'T-E', 'T-P', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T'})


        self.assertEqual(set(self.g_c.vertices_nao_adjacentes()), {'C-J', 'C-E', 'C-P', 'E-J', 'E-P', 'P-J'})
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])
        self.assertEqual(set(self.g_e.vertices_nao_adjacentes()), {'A-D', 'A-E', 'B-A', 'B-C', 'B-D', 'B-E', 'C-E', 'D-C', 'D-A', 'E-D', 'E-C'})

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertTrue(self.g_e.ha_laco())

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
        self.assertEqual(self.g_e.grau('C'), 5)
        self.assertEqual(self.g_e.grau('D'), 5)

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
        self.assertTrue(self.g_e.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), {'a1'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), {'a7', 'a8'})
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), {'a1', 'a2', 'a3'})
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), {'asd'})
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')
        self.assertEqual(set(self.g_e.arestas_sobre_vertice('D')), {'5', '6', '7', '8'})

    def test_warshall(self):
        self.assertEqual(self.grafoDirecionado.warshall(), self.warshall_grafoDirecionado)
        self.assertEqual(self.g_p.warshall(), self.warshall_paraiba)
        self.assertEqual(self.g_p_sem_paralelas.warshall(), self.warshall_paraiba_sem_paralelas)
        self.assertEqual(self.g_c.warshall(), self.warshall_pb_completo)

    def test_dijkstra_drone(self):
        self.assertEqual(self.grafoDirecionado2.dijkstra_drone("A","G",1,10,["A","B","C","D","E","F","G"]),['G', 'F', 'D', 'B', 'A'])
        self.assertEqual(self.grafoDirecionado2.dijkstra_drone("A","G",1,3,["B","E"]),['G', 'F', 'D', 'B', 'A'])
        self.assertEqual(self.grafoDirecionado2.dijkstra_drone("A","G",2,5,["C","E"]),['G', 'F', 'C', 'A'])
        self.assertEqual(self.grafoDirecionado2.dijkstra_drone("A","D",5,10,["B","F"]),['D', 'B', 'A'])
        self.assertEqual(self.grafoDirecionado2.dijkstra_drone("A","G",3,5,["D","E"]),"Caminho inexistente")
        self.assertEqual(self.grafoDirecionado2.dijkstra_drone("A","G",2,7,["B","F"]),['G', 'F', 'C','A'])
        self.assertEqual(self.grafoDirecionado2.dijkstra_drone("B","G",2,3,["B","D"]),['G', 'F', 'D', 'B'])

    def test_ordenacao_topologica(self):
        self.assertEqual(self.eng_computacao.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '22', '23', '27', '32', '42', '71', '74', '91', '101', '102', '21', '24', '25', '26', '34', '35', '83', '31', '33', '36', '41', '43', '53', '54', '63', '72', '92', '44', '45', '51', '52', '62', '64', '73', '81', '103', '55', '61', '75', '82', '93', '65', '84', '85', '94'])
        self.assertEqual(self.construcao_edificios.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '18', '22', '31', '34', '58', '61', '63', '68', '71', '72', '73', '21', '23', '24', '25', '26', '27', '66', '67', '32', '33', '35', '36', '37', '38', '41', '42', '43', '44', '45', '46', '47', '53', '55', '57', '62', '64', '51', '52', '54', '56', '65'])
        self.assertEqual(self.fisica.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '26', '27', '34', '35', '36', '37', '43', '44', '56', '65', '75', '21', '22', '23', '24', '25', '55', '66', '81', '31', '32', '33', '57', '73', '85', '41', '42', '45', '46', '54', '68', '74', '83', '51', '52', '53', '72', '76', '82', '61', '62', '63', '64', '86', '71', '84'])
        self.assertEqual(self.letras.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '24', '27', '36', '37', '45', '65', '66', '81', '82', '85', '86', '21', '22', '23', '25', '26', '34', '47', '53', '54', '57', '67', '76', '83', '31', '32', '33', '35', '43', '44', '56', '64', '68', '77', '41', '42', '46', '51', '52', '55', '61', '62', '63', '71', '72', '73', '74', '75', '78', '87', '84', '88'])
        self.assertEqual(self.matematica.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '23', '24', '25', '27', '35', '36', '46', '56', '66', '76', '85', '86', '21', '22', '26', '33', '34', '43', '45', '52', '65', '31', '32', '41', '44', '51', '62', '72', '75', '42', '53', '54', '55', '57', '61', '63', '81', '82', '83', '64', '67', '71', '73', '74', '77', '84', '87'])
        self.assertEqual(self.telematica.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '25', '27', '37', '47', '56', '57', '63', '64', '65', '66', '21', '22', '23', '24', '26', '34', '35', '31', '32', '33', '36', '46', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62'])