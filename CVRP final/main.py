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

#salva o arquivo em uma lista
arq = ler_arquivo()

#separa os dados dos arquivos em listas específicas
dados = arq[0]
casas = arq[1]
rotas = arq[2]

#variaveis de controle
distancia = 0
carro = 0

#imprimirDadosDoArquivo(dados, casas, rotas)
resto = contarEntregas(casas)
print ("\n============================================")
print("             FALTAM {} ENTREGAS".format(resto))
("============================================\n")

'''         
Entrega de pacotes

Contem todas as rotas encontradas pelo vizinho mais proximo // para todos os carros (ln 56)

Enquanto houver casa com demanda: adiciona mais um carro, reseta a posição de saída do carro, pega a capacidade direto do arquivo; (ln 59 - ln 62)

Enquanto o carro tiver capacidade: salva a ultima posição do carro, caso não haja mais casa compatível; procura a posição da casa mais próxima,
se houver casa mais proxima, diminui a capacidade do carro de acordo com a demanda que a casa solicitou. (ln 65 - ln 69)

Soma a distância total percorrida e informa que a casa não precisa de mais entrega e marca a rota como já percorrida (ln 71 - ln 76)

Se não houver casa mais próxima, soma a distância de volta para a empresa (ln 78 - ln 79)

Informa quantos produtos ainda faltam ser entregues (ln 82)


'''

Enderecos = []  
custoEnderecos = []

while(resto > 0):     
    carro += 1                                                                                   
    posCarro = [0, 0]                                
    capacidade = int(dados[2][1])                   
    custoPorCarro = 0
    EnderecosPorCarro = [0]    
    while(capacidade > 0):                                                                      
        ultimaPosicao = deepcopy(posCarro)                                                       
        posCarro = procurarCasaMaisProxima(rotas, posCarro, casas, capacidade)                   
        if(posCarro[1] >= 0):                                                                    
            capacidade = atualizarCapacidade(casas, posCarro[1], capacidade)                     
            EnderecosPorCarro.append(deepcopy(posCarro[1]))
            distancia = somarDistancia(distancia, posCarro, rotas)                                        
            demanda = atualizarDemanda(casas, posCarro[1])                                      
            aux = deepcopy(posCarro)
            posCarro[0] = aux[1]
            posCarro[1] = aux[0]
            #print(posCarro)                                                                                 
            custoPorCarro += int(rotas[ultimaPosicao[0]][ultimaPosicao[1]])
        else:                                                                                    
            distancia += int(rotas[ultimaPosicao[0]][ultimaPosicao[1]])                          
            custoPorCarro += int(rotas[ultimaPosicao[0]][ultimaPosicao[1]])
            break
    resto = contarEntregas(casas)                                                    
    EnderecosPorCarro.append(0)            
    custoEnderecos.append(deepcopy(custoPorCarro))
    Enderecos.append(deepcopy(EnderecosPorCarro))

melhorTrajeto = vnd(Enderecos, rotas)

print(melhorTrajeto)
