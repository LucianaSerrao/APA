import math
from copy import deepcopy

def contarEntregas(demanda):
    resto = 0
    for casas in demanda:
        if (int(casas[1])>0):
            resto += int(casas[1])
    return resto

def procurarCasaMaisProxima(grafo, posCarro, casa, capacidade):

	'''
	Analisa o grafo a partir da linha em que o carro se encontra (ln 23)
	Procura a casa mais próxima que não seja ela mesma (ln 24)
	Verifica se a demanda da casa é menor que a capacidade do veículo e se é maior que zero (ln 25)
	Salva a distância da casa mais próxima (ln 26)
	Salva a posição da coluna em que o carro se encontra (ln 27)

    	'''    
    casaMaisProxima = math.inf                                                                      
    contador = 0                
    for i in grafo[posCarro[0]]:                                
        if ((int(i) > 0 ) and (int(i) < casaMaisProxima)):                                  
            if(int(casa[contador][1]) <= capacidade and int(casa[contador][1]) > 0):                     
                casaMaisProxima = int(i)                                                    
                posCarro[1] = contador 
                                                     
        contador += 1
    if(casaMaisProxima == float("inf")):
        posCarro[1] = -1        
    return posCarro

def somarDistancia(distanciaAtual, endereco, rota):
    x = endereco[0]
    y = endereco[1]
    distanciaAtual += int(rota[x][y])
    return distanciaAtual

def atualizarRota(endereco, rota):  
    x = int(endereco[0])
    y = int(endereco[1])
    rota[x][y] = 0    
    return rota

def atualizarDemanda(casa, endereco):    
    casa[endereco][1] = 0    
    return casa

def atualizarCapacidade(casa, endereco, capacidade):
    capacidade -= int(casa[endereco][1])       
    return capacidade

def calcularRota(solucao, rota):
    valor = 0  
    n = 0  
    m = 1
    posCarro = [0, 0]
    destino = [n, solucao[m]]
    for i in solucao:
        valor += somarDistancia(valor, destino, rota)
        print("o Valor é {}".format(valor))
        posCarro = [m,m]
        m += 1
        destino = [solucao[m-1], solucao[m]]        
    return valor


def calcularCusto(solucao, rota):

''' Calcula o custo da rota de um carro '''

    custo = 0
    for i in range(1,len(solucao)):
        custo += int(rota[solucao[i-1]][solucao[i]])
    return custo


def calcularCustoTotal(listaSolucao, rota):

''' Calcula o custo para todos os carros '''

    custoTotal = 0
    for lista in listaSolucao:
        custoTotal += calcularCusto(lista, rota)
    return custoTotal
    

def opt2(solucao, custofinal, rota):

''' Pega 2 casas e coloca na melhor posição possível do vetor '''

    melhorCusto = custofinal
    melhorSolucao = deepcopy(solucao)
    if(len(solucao)>4):
        for index in range (2, len(solucao)-1):
            copiasolucao = deepcopy(solucao)
            casaAnalisada = deepcopy([copiasolucao[index-1], copiasolucao[index]])
            del copiasolucao[index]
            del copiasolucao[index-1]
            for n in range(index, len(copiasolucao)-1):            
                copiasolucao.insert(n, casaAnalisada[1])
                copiasolucao.insert(n, casaAnalisada[0])
                resultadoParcial = calcularCusto(copiasolucao, rota)   
                if(resultadoParcial < melhorCusto):
                    melhorCusto = resultadoParcial 
                    melhorSolucao = deepcopy(copiasolucao)
                del copiasolucao[n+1]
                del copiasolucao[n]
    return melhorSolucao



def reinsertion(solucao, custofinal, rota):

''' Pega uma casa e a coloca na melhor posição possível do vetor '''

    melhorCusto = custofinal
    melhorSolucao = deepcopy(solucao)
    if(len(solucao)>3):
        for index in range (1, len(solucao)-1):
            copiasolucao = deepcopy(solucao)
            casaAnalisada = deepcopy(copiasolucao[index])
            del copiasolucao[index]        
            for n in range(index, len(copiasolucao)-1):                        
                copiasolucao.insert(n+1, casaAnalisada)
                resultadoParcial = calcularCusto(copiasolucao, rota)   
                if(resultadoParcial < melhorCusto):
                    melhorCusto = resultadoParcial 
                    melhorSolucao = deepcopy(copiasolucao)            
                del copiasolucao[n+1]
    return melhorSolucao


def swap(solucao, custofinal, rota): 

''' Retorna o melhor swap possível da rota '''
      
    melhorCusto = custofinal
    melhorSolucao = deepcopy(solucao)

    if(len(solucao)>3):
        for index in range (1, len(solucao)-2):
            copiasolucao = deepcopy(solucao)
            for n in range(index+1, len(copiasolucao)-1):  
                copiasolucao = deepcopy(solucao)          
                copiasolucao = swapPositions(copiasolucao, index, n)
                resultadoParcial = calcularCusto(copiasolucao, rota)   
                if(resultadoParcial < melhorCusto):
                    melhorCusto = resultadoParcial 
                    melhorSolucao = deepcopy(copiasolucao)            
    return melhorSolucao

def swapPositions(list, pos1, pos2):      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def swapGeral(listaSolucao, rota):

''' Funções para aplicar as paradas na lista completa de todos os carros '''

    listaAtualizada = []
    for lista in listaSolucao:
        listaAtualizada.append(swap(lista, calcularCusto(lista, rota), rota))
    return listaAtualizada

def opt2Geral(listaSolucao, rota): 
    listaAtualizada = []
    for lista in listaSolucao:
        listaAtualizada.append(opt2(lista, calcularCusto(lista, rota), rota))
    return listaAtualizada

def reinsertionGeral(listaSolucao, rota):
    listaAtualizada = []
    for lista in listaSolucao:
        listaAtualizada.append(reinsertion(lista, calcularCusto(lista, rota), rota))
    return listaAtualizada

def vnd(listaSolucao, rota): 

'''
 Roda primeiro um reinsertion, repete até não melhorar mais, e depois sobe pra um swap, depois opt2 || volta pro reinsertion sempre que melhorar

'''

    listaAuxiliar = deepcopy(listaSolucao)
    custoInicial = calcularCustoTotal(listaSolucao, rota)
    custoFinal = 0
    k = 1
    while(k <= 3):
        if(k == 1):
            listaAuxiliar = reinsertionGeral(listaAuxiliar, rota)            
        elif(k == 2):
            listaAuxiliar = swapGeral(listaAuxiliar, rota)    
        elif(k == 3):
            listaAuxiliar = opt2Geral(listaAuxiliar, rota)    
        custoFinal = calcularCustoTotal(listaAuxiliar, rota)
        if(custoFinal < custoInicial):
            k = 1
            print("otimização encontrada em {}".format(k))
            print("antes {} depois {}".format(custoInicial, custoFinal))
            custoInicial = custoFinal            
        else:            
            k += 1
            print("alterando k= {}".format(k))
    return listaAuxiliar
