import numpy as np
 
#TODO: atomic labels -> dictionary 
#TODO: check if .xyz files have a pattern✅ 
#TODO: code function RMSD() 

def separator(list1 = [], list2 = []): 
    atom1 = []
    atom2 = []
    coord1 = []
    coord2 = []
    
    for atoms1_pointer in list1:
        if atoms1_pointer.isalpha() == True:
            atom1.append(atoms1_pointer)
        elif atoms1_pointer.isalpha() == False:
            coord1.append(atoms1_pointer)
            
    for atoms2_pointer in list2:
        if atoms2_pointer.isalpha() == True:
            atom2.append(atoms2_pointer)
        elif atoms2_pointer.isalpha() == False:
            coord2.append(atoms2_pointer)
     
    
    return atom1, coord1, atom2, coord2

def formatXYZ(arr1 = [], arr2 = []):
    #Receive array w/ atoms and array w/ coordinates 
    atoms1, coords1, atoms2, coords2 = separator(arr1, arr2)
    
    #Convert to float and transform array to matrix 
    mtx1 = np.array(coords1, dtype='float64')
    mtx2 = np.array(coords2, dtype='float64')
    matrix1 = np.asmatrix(mtx1)
    matrix2 = np.asmatrix(mtx2)
    
    #Create the shape and generate both matrices
    row_mtx1 = len(atoms1)
    row_mtx2 = len(atoms2)
    shape_mtx1 = (row_mtx1, 3)
    shape_mtx2 = (row_mtx2, 3) 
    matrix1 = mtx1.reshape(shape_mtx1)
    matrix2 = mtx2.reshape(shape_mtx2)
    
    #Create an empty matrix is necessary for proceed w/ the calculations 
    #Since Kabsch returns a matrix (rotational matrix), we need to have and empty matrix to acomodate the results being passed
    result = np.zeros((len(matrix1),3))
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    print(result) 
    
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
    
def full(matrix1, matrix2): 
    result = np.zeros((len(matrix1),3))
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    print(result)
        
       
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    