 o def ler_arquivo():
    listaStrings = []  #salva cada linha do arquivo em uma lista
    #===============================================================================
    #                  LER O ARQUIVO E SALVA EM UMA LISTA DE STRINGS
    arq1 = open(r"C:.txt", "r")#colocar o caminho do arquivo aqui

    for linha in arq1:
        listaStrings.append(linha.strip())

    arq1.close()
    #================================================================================
    #               SEPARA A LISTA DE STRING EM LISTAS LISTAS ESPECÍFICAS

    listaDetalhada = []     #contem uma lista apenas com os dados finais

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

