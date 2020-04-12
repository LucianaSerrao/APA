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
instances = ["P-n16-k8", "P-n19-k2", "P-n20-k2", "P-n23-k8", "P-n45-k5", "P-n50-k10", "P-n51-k10", "P-n55-k7"]
custoOtimo = [450, 212, 216, 529, 510, 696, 741, 568]

def main(file, index):
    #SALVA O ARQUIVO EM UMA LISTA
    auxFile = read_file(file+'.txt')

    #SEPARA DOS DADOS DOS ARQUIVOS EM LISTAS ESPECÍFICAS
    data = auxFile[0]
    places = auxFile[1]
    route = auxFile[2]


    #variaveis de controle
    distance = 0
    car = 0
    resto = deliveryCount(places)

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

    Address = []  
    addressCost = []
    initialHeurisTime = time.time()

    while(resto > 0):     
        car += 1                                                                                   
        carPosition = [0, 0]                                
        capacity = int(data[2][1])                   
        carCost = 0
        adressPerCar = [0]    
        while(capacity > 0):                                                                      
            lastPosition = deepcopy(carPosition)                                                       
            carPosition = searchNearest(route, carPosition, places, capacity)                   
            if(carPosition[1] > 0):                                                                    
                capacity = attCapacity(places, carPosition[1], capacity)                     
                adressPerCar.append(deepcopy(carPosition[1]))
                distance = addDistance(distance, carPosition, route)                                        
                attDemand(places, carPosition[1])                                      
                aux = deepcopy(carPosition)
                carPosition[0] = aux[1]
                carPosition[1] = aux[0]
                #print(carPosition)                                                                                 
                carCost += int(route[lastPosition[0]][lastPosition[1]])
            else:                                                                                    
                distance += int(route[lastPosition[0]][lastPosition[1]])                          
                carCost += int(route[lastPosition[0]][lastPosition[1]])
                break
        resto = deliveryCount(places)                                                    
        adressPerCar.append(0)            
        addressCost.append(deepcopy(carCost))
        Address.append(deepcopy(adressPerCar))


    """                 CALCULO DE DADOS PARA RELATÓRIO FINAL               """
    finalHeurisTime = time.time()
    heurisCost = calcTotalCost(Address, route)
    vndInitialTime = time.time()
    bestRoute = vnd(Address, route)
    vndFinalTime = time.time()
    
    vndCost = calcTotalCost(bestRoute, route)
    
    #tHeuristica = finalHeurisTime -initialHeurisTime
    #tVND = vndFinalTime - vndInitialTime
    
    gapHeuristica = ((heurisCost - custoOtimo[index])/custoOtimo[index])*100
    gapVND = ((vndCost - custoOtimo[index])/custoOtimo[index])*100

    return [instances[i], str(custoOtimo[index]), str(heurisCost), str(round(finalHeurisTime -initialHeurisTime, 4)), str(round(gapHeuristica, 4)), str(vndCost), str(round(vndFinalTime - vndInitialTime, 4)), str(round(gapVND, 4))]

file2 = csv.writer(open("tabela.csv", "w"))
file2.writerow(["nome", "ótimo", "valor ", "tempo", "gap", "valor", "tempo", "gap"])

for i in range(0, len(instances)):       
    file2.writerow(main(instances[i], i))