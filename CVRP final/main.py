from readFile import *
from functions import *
from copy import deepcopy
import time
import csv
'''         
ALGORITMO    
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


'''         VARIÁVEIS GLOBAIS            '''
instancias = ["P-n16-k8", "P-n19-k2", "P-n20-k2", "P-n23-k8", "P-n45-k5", "P-n50-k10", "P-n51-k10", "P-n55-k7"]
custoOtimo = [450, 212, 216, 529, 510, 696, 741, 568]



#separa os dados dos arquivos em listas específicas
dados, rotas, casas = read_file()

#variaveis de controle
distancia = 0
carro = 0
resto = contarEntregas(casas)

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
heuristicaTInicio = time.time()

while(resto > 0):     
    carro += 1                                                                                   
    posCarro = [0, 0]                                
    capacidade = int(dados[2][1])                   
    custoPorCarro = 0
    EnderecosPorCarro = [0]    
    while(capacidade > 0):                                                                      
        ultimaPosicao = deepcopy(posCarro)                                                       
        posCarro = procurarCasaMaisProxima(rotas, posCarro, casas, capacidade)                   
        if(posCarro[1] > 0):                                                                    
            capacidade = atualizarCapacidade(casas, posCarro[1], capacidade)                     
            EnderecosPorCarro.append(deepcopy(posCarro[1]))
            distancia = somarDistancia(distancia, posCarro, rotas)                                        
            atualizarDemanda(casas, posCarro[1])                                      
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


"""                 CALCULO DE DADOS PARA RELATÓRIO FINAL               """
    heuristicaTFinal = time.time()
    custoHeuristica = calcularCustoTotal(Enderecos, rotas)
    VndTInicio = time.time()
    melhorTrajeto = vnd(Enderecos, rotas)
    VndTFinal = time.time()
    custoVND = calcularCustoTotal(melhorTrajeto, rotas)
    tHeuristica = heuristicaTFinal - heuristicaTInicio
    tVND = VndTFinal - VndTInicio
    gapHeuristica = ((custoHeuristica - custoOtimo[indice])/custoOtimo[indice])*100
    gapVND = ((custoVND - custoOtimo[indice])/custoOtimo[indice])*100

    return [instancias[i], str(custoOtimo[indice]), str(custoHeuristica), str(round(tHeuristica, 4)), str(round(gapHeuristica, 4)), str(custoVND), str(round(tVND, 4)), str(round(gapVND, 4))]

arquivo = csv.writer(open("relatorio2.csv", "w"))
arquivo.writerow(["nome", "ótimo", "valor solução", "tempo", "gap", "valor solução", "tempo", "gap"])

for i in range(0, len(instancias)):       
    arquivo.writerow(algoritmo(instancias[i], i))