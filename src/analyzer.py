import numpy as np
from sklearn.metrics import mean_squared_error
from cli.out import output_singleResult

#TODO: atomic labels -> dictionary;❔
#TODO: code function calculateRMSD();✅ 
#TODO: code function calculateKabsch(); (offset rotated P ❔❔)

#------------------------------------
# if teste_de_lista == []:
#     print('sepa vai dar boa')
# else:
#     print('sepa n vai dar boa')
#------------------------------------

def calculateRMSD(matrix_P, matrix_Q): 
    rmsd = round(mean_squared_error(matrix_P, matrix_Q, squared=False), 4)
    print(rmsd)
    
def calculateKabsch(matrix_P, matrix_Q): 
    #Calculate centroids to align coordinates 
    centroid1 = np.mean(matrix_P, axis=0)
    centroid2 = np.mean(matrix_Q, axis=0) 
    
    #Center both matrices considering the centroid 
    trans_matrixP = matrix_P -  np.tile(centroid1, (3,1)) 
    trans_matrixQ = matrix_Q - np.tile(centroid2, (3,1))
    
    #Generate the covariance matrix
    matrix_H = np.transpose(trans_matrixQ) * trans_matrixP
    
    #Calculate de SVD of the covariance matrix
    matrix_U, matrix_S, matrix_Vh = np.linalg.svd(matrix_H) 
    
    #Check for right-handed orientantion in the coordinates system
    #Based on the answer, calculate the proper rotation matrix
    if np.linalg.det(matrix_Vh * (np.transpose(matrix_U))) < 0: 
        counter_identitiy = np.array([[1,0,0], [0,1,0], [0,0,-1]])
        matrix_R = (np.transpose(matrix_U)) * counter_identitiy * matrix_Vh
    else:   
        matrix_R = (np.transpose(matrix_U)) * matrix_Vh
        
    
    
    
    
    
    
    # result = np.zeros((len(matrix1),3))
    
    # for i in range(len(matrix1)):
    #     for j in range(len(matrix1[0])):
    #         result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    # print(result)
    

        
       
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    