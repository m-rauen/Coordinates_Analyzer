import numpy as np
 
#TODO: atomic labels -> dictionary❔  
#TODO: code function RMSD() 
    
def RMSD(matrix1, matrix2): 
    result = np.zeros((len(matrix1),3))
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    print(result)
    
def Kabsch(matrix1, matrix2): 
    result = np.zeros((len(matrix1),3))
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    print(result)
    
def fullCalculation(matrix1, matrix2): 
    result = np.zeros((len(matrix1),3))
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    print(result)
        
       
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    