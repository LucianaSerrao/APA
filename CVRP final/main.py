from lerArquivos import *
from funcoes import *
from copy import deepcopy

'''         ALGORITMO    
    1. PROCURAR DESTINO
        1.1 PROCURA CASA MAIS PRÓXIMA
        1.2 VER SE É COMPATÍVEL COM A CAPACIDADE RESTANTE DO CARRO
            1.2.1 SE FOR FAZ A ENTREGA
            1.2.2 SE NÃO FOR PROCURA A PRÓXIMA CASA
            1.2.3 SE NO FIM NÃO HOUVER MAIS CASA COMPATÍVEL VOLTA PARA A EMPRESA SOMANDO A DISTÂNCIA
    2. FAZER ENTREGA
        2.1 DIMINUIR CAPACIDADE DO CARRO
        2.2 COLOCA A DEMANDA DA CASA PARA ZERO
        2.3 SOMAR DISTÂNCIA PERCORRIDA
    3. REPETIR
'''

#SALVA O ARQUIVO EM UMA LISTA
arq = ler_arquivo()

#SEPARA DOS DADOS DOS ARQUIVOS EM LISTAS ESPECÍFICAS
dados = arq[0]
casas = arq[1]
rotas = arq[2]

#VARIÁVEIS DE CONTROLE
distancia = 0
carro = 0
#imprimirDadosDoArquivo(dados, casas, rotas)
resto = contarEntregas(casas)
print ("\n============================================")
print("             FALTAM {} ENTREGAS".format(resto))
("============================================\n")

"""          # INICIO DO CÓDIGO DE ENTREGA DE PACOTES                """

Enderecos = []  #Contem todas as rotas encontradas pelo vizinho mais próximo || para todos os carros
custoEnderecos = []

while(resto > 0):  #ENQUANTO HOUVER CASA COM DEMANDA    
    carro += 1                                                                                   #ADICIONA +1 CARRO
    posCarro = [0, 0]                               #RESETA A POSIÇÃO DE SAIDA DO CARRO 
    capacidade = int(dados[2][1])                   #PEGA A CAPACIDADE DIRETO DO ARQUIVO
    custoPorCarro = 0
    EnderecosPorCarro = [0]    
    while(capacidade > 0):                                                                      #ENQUANTO O CARRO TIVER CAPACIDADE
        ultimaPosicao = deepcopy(posCarro)                                                       #SALVA A ÚLTIMA POSIÇÃO DO CARRO, CASO NÃO HAJA MAIS CASA COMPATÍVEL
        posCarro = procurarCasaMaisProxima(rotas, posCarro, casas, capacidade)                   #PROCURA A POSIÇÃO DA CASA MAIS PRÓXIMA
        if(posCarro[1] >= 0):                                                                    #SE POSITIVO HÁ UMA CASA MAIS PRÓXIMA
            capacidade = atualizarCapacidade(casas, posCarro[1], capacidade)                     #DIMINUI A CAPACIDADE DO CARRO DE ACORDO COM O QUE A CASA SOLICITOU
            EnderecosPorCarro.append(deepcopy(posCarro[1]))
            distancia = somarDistancia(distancia, posCarro, rotas)                               #SOMA A DISTÂNCIA TOTAL PERCORRIDA          
            demanda = atualizarDemanda(casas, posCarro[1])                                       #INFORMA QUE A CASA NÃO PRECISA DE MAIS ENTREGA
            aux = deepcopy(posCarro)
            posCarro[0] = aux[1]
            posCarro[1] = aux[0]
            #print(posCarro)                                                                                 #MARCA A ROTA COMO JÁ PERCORRIDA
            custoPorCarro += int(rotas[ultimaPosicao[0]][ultimaPosicao[1]])
        else:                                                                                    #SE NEGATIVO NÃO HÁ MAIS CASA COMPATÍVEL
            distancia += int(rotas[ultimaPosicao[0]][ultimaPosicao[1]])                          #SOMA A DISTÂNCIA DE VOLTA PARA A EMPRESA
            custoPorCarro += int(rotas[ultimaPosicao[0]][ultimaPosicao[1]])
            break
    resto = contarEntregas(casas)                                                    #INFORMA QUANTOS PRODUTOS AINDA FALTAM SER ENTREGUES
    EnderecosPorCarro.append(0)            
    custoEnderecos.append(deepcopy(custoPorCarro))
    Enderecos.append(deepcopy(EnderecosPorCarro))

melhorTrajeto = vnd(Enderecos, rotas)

print(melhorTrajeto)
