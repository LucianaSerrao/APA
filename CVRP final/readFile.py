import sys

def read_file(file_name):

    '''
    Saves each line of the file in a list (ln 12)
    Read the file and save it to a string list (ln 14 - ln 19)
    Separates the string list into specific lists (ln 20 - ln 36)
	
    '''


    stringList = []  
                      
    #file_name = sys.argv[1]
    with open(file_name, "r") as arq1:
        for line in arq1:
            stringList.append(line.strip())              

    detailedList = []

    for line in stringList:    
        detailedList.append(line.split())
        
    dataList = []
    demandList = []
    graphList = []

    for i in range(0, 4):
        dataList.append(detailedList[i])
    
    for i in range(4, len(dataList)+ int(dataList[1][1])):
        demandList.append(detailedList[i])

    for i in range(len(dataList)+len(demandList)+2, len(detailedList)-1):
        graphList.append(detailedList[i])

    
    return (dataList, demandList, graphList)

 
    

