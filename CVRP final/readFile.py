import sys

def read_file():

    '''
    Salva cada linha do arquivo em uma lista  (ln 12)
    Le o arquivo e salva numa lista de string (ln 14 - ln 19)
    Separa a lista de string em listas específicas (ln 20 - ln 36)
	
    '''


    listaStrings = []  
                      
    file_name = sys.argv[1]
    with open(file_name, "r") as arq1:
        for linha in arq1:
            listaStrings.append(linha.strip())              

    listaDetalhada = []

    for linha in listaStrings:    
        listaDetalhada.append(linha.split())
        
    listaDados = []
    listaDemanda = []
    listaGrafo = []

    for i in range(0, 4):
        listaDados.append(listaDetalhada[i])
    
    for i in range(4, len(listaDados)+ int(listaDados[1][1])):
        listaDemanda.append(listaDetalhada[i])

    for i in range(len(listaDados)+len(listaDemanda)+2, len(listaDetalhada)-1):
        listaGrafo.append(listaDetalhada[i])

    
    return (listaDados, listaDemanda, listaGrafo)

def imprimirDadosDoArquivo(Dados, Demanda, Rotas):        
    print("imprimindo Dados:")
    for linha in Dados:
        print (linha)

    print("imprimindo Demanda:")
    n = 1
    for linha in Demanda:
        print ("{} - {}".format(n, linha))
        n+= 1

    print("imprimindo Rotas:")
    n = 1
    for linha in Rotas:
        print ("{} - {}".format(n, linha))
        n +=1
    
    

