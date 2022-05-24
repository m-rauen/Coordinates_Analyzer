import numpy as np
from sklearn.metrics import mean_squared_error
from cli.out import output_singleResult

#TODO: atomic labels -> dictionary;❔
#TODO: code function calculateRMSD();✅ 
#TODO: code function calculateKabsch();

def calculateRMSD(matrix1, matrix2): 
    result = round(mean_squared_error(matrix1, matrix2, squared=False), 4)
    # result_rmsd = str(result)
    # if result_rmsd.isnumeric() == True:
    #     print(result_rmsd)
    # elif result_rmsd.isnumeric() == False:
    #     print('bugou')
    # else: 
    #     print('caralho qq deu')
    # teste_de_lista = []
    # if teste_de_lista == []:
    #     print('sepa vai dar boa')
    # else:
    #     print('sepa n vai dar boa')
    output_singleResult(result)
    
def calculateKabsch(matrix1, matrix2): 
    result = np.zeros((len(matrix1),3))
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    print(result)
    

        
       
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    