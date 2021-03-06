import math
from copy import deepcopy

def deliveryCount(demand):
    resto = 0
    for places in demand:
        if (int(places[1])>0):
            resto += int(places[1])
    return resto

def searchNearest(graph, carPosition, place, capacity):

    '''
    Analyzes the graph from the line the car is on (ln 23)
    Search for the nearest place(ln 24)
    Checks whether the place's demand is less than the vehicle's capacity (ln 25)
    Saves the distance to the nearest place (ln 26)
    Saves the position of the column the car is in (ln 27)

    '''    
    nearest = math.inf                                                                      
    count = 0                
    for i in graph[carPosition[0]]:                                
        if ((int(i) > 0 ) and (int(i) < nearest)):                                  
            if(int(place[count][1]) <= capacity and int(place[count][1]) > 0):                     
                nearest = int(i)                                                    
                carPosition[1] = count 
                                                     
        count += 1
    if(nearest == float("inf")):
        carPosition[1] = -1        
    return carPosition

def addDistance(currentDistance, address, route):
    x = address[0]
    y = address[1]
    currentDistance += int(route[x][y])
    return currentDistance

# def attRoute(endereco, rota):  
    # x = int(endereco[0])
    # y = int(endereco[1])
    # rota[x][y] = 0    
    # return rota

def attDemand(place, address):    
    place[address][1] = 0    
    return place

def attCapacity(place, address, capacity):
    capacity -= int(place[address][1])       
    return capacity

def calcRoute(sol, route):
    totalSum = 0  
    j = 0  
    k = 1
    carPosition = [0, 0]
    destination = [j, sol[k]]
    for i in sol:
        totalSum += addDistance(totalSum, destination, route)
        print("o Valor é {}".format(totalSum))
        carPosition = [k,k]
        k += 1
        destination = [sol[k-1], sol[k]]        
    return totalSum

def calcCost(sol, route):  #tem que ser linear, olhar isso no marcone 

    ''' Calculates the cost of a car route '''

    cost = 0
    for i in range(1,len(sol)):
        cost += int(route[sol[i-1]][sol[i]])
        print(cost)
    return cost


def calcTotalCost(solList, route):

    ''' Calculates the cost for all cars '''

    totalCost = 0
    for lista in solList:
        totalCost += calcCost(lista, route)
    return totalCost
    

def opt2(sol, finalCost, route):

    ''' Take 2 places and trade them for the best possible positions of the vector '''

    bestCost = finalCost
    bestSolution = deepcopy(sol)
    if(len(sol)>4):
        for index in range (2, len(sol)-1):
            solutionCopy = deepcopy(sol)
            checked = deepcopy([solutionCopy[index-1], solutionCopy[index]])
            del solutionCopy[index]
            del solutionCopy[index-1]
            for i in range(1, len(solutionCopy)-1):            
                solutionCopy.insert(i, checked[1])
                solutionCopy.insert(i, checked[0])
                partial = calcCost(solutionCopy, route)   
                if(partial < bestCost):
                    bestCost = partial 
                    bestSolution = deepcopy(solutionCopy)
                del solutionCopy[i+1]
                del solutionCopy[i]
    return bestSolution



def reinsertion(sol, finalCost, route):

    ''' Trade a place for the best possible position of the vector '''

    bestCost = finalCost
    bestSolution = deepcopy(sol)
    if(len(sol)>3):
        for index in range (1, len(sol)-1):
            solutionCopy = deepcopy(sol)
            checked = deepcopy(solutionCopy[index])
            del solutionCopy[index]        
            for i in range(1, len(solutionCopy)-1):                        
                solutionCopy.insert(i, checked)
                partial = calcCost(solutionCopy, route)   
                if(partial < bestCost):
                    bestCost = partial 
                    bestSolution = deepcopy(solutionCopy)            
                del solutionCopy[i]
    return bestSolution


def swapPositions(list, pos1, pos2):      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def swap(sol, finalCost, route): 

    ''' Returns the best route swap '''
      
    bestCost = finalCost
    bestSolution = deepcopy(sol)
    solutionCopy = deepcopy(sol)

    if(len(sol)>3):
        for index in range (1, len(sol)-2):
            for i in range(index+1, len(solutionCopy)-1):  
                solutionCopy = deepcopy(sol)          
                solutionCopy = swapPositions(solutionCopy, index, i)
                partial = calcCost(solutionCopy, route)   
                if(partial < bestCost):
                    bestCost = partial 
                    bestSolution = deepcopy(solutionCopy)            
    return bestSolution



def swapGeral(solList, route):

    ''' Functions to apply stops to the complete list of cars '''

    currentList = []  #lista atualizada
    for lista in solList:
        currentList.append(swap(lista, calcCost(lista, route), route))
    return currentList

def opt2Geral(solList, route): #olhar o funcionamento porque nao ta realizando nenhum movimento
    currentList = []
    for lista in solList:
        currentList.append(opt2(lista, calcCost(lista, route), route))
    return currentList

def reinsertionGeral(solList, route):
    currentList = []
    for lista in solList:
        currentList.append(reinsertion(lista, calcCost(lista, route), route))
    return currentList

def vnd(solList, route): 

    '''
    Reinsertion, repeat until it can't get better and then swap it 
    opt2 
    reinsertion

    '''

    auxList = deepcopy(solList)
    initialCost = calcTotalCost(solList, route)
    i = 1
    while(i <= 3):
        if(i == 1):
            auxList = reinsertionGeral(auxList, route)            
        elif(i == 2):
            auxList = swapGeral(auxList, route)    
        elif(i == 3):
            auxList = opt2Geral(auxList, route)    
        finalCost = calcTotalCost(auxList, route)
        if(finalCost < initialCost):
            i = 1
            print("Optimization : {}".format(i))
            print("Before: {} After {}".format(initialCost, finalCost))
            initialCost = finalCost            
        else:            
            i += 1
            print(" i = {}".format(i))
    return auxList
