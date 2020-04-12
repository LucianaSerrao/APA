from readFile import *
from functions import *
from copy import deepcopy
import time
import csv




instances = ["P-n16-k8", "P-n19-k2", "P-n20-k2", "P-n23-k8", "P-n45-k5", "P-n50-k10", "P-n51-k10", "P-n55-k7"]
custoOtimo = [450, 212, 216, 529, 510, 696, 741, 568]

def main(file, index):
    
    '''
    Saves the file to a list and separates its data into specific lists.
    
    Package delivery

    Contains all routes found by the nearest neighbor // for all cars (ln 56)

    As long as there is a place with demand: add another car, reset the car's exit position, take the capacity straight from the file; (ln 59 - ln 62)

    As long as the car has capacity: save its last position, if there is no other compatible place;
                                     looks for the position of the nearest place, if there is a place closer, the capacity of the car decreases
                                     according to the demand that the place requested. (ln 65 - ln 69)

    Sums the total distance traveled and informs that the place does not need more delivery and marks the route as already checked. (ln 71 - ln 76)

    If there is no nearest place, add the distance back to the company. (ln 78 - ln 79)

    Tells you how many products are yet to be delivered (ln 82)   

    '''
    
    auxFile = read_file(file+'.txt')

    data = auxFile[0]
    places = auxFile[1]
    route = auxFile[2]


    distance = 0
    car = 0
    resto = deliveryCount(places)



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


    # CALCULO DE DADOS PARA TABELA                """
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