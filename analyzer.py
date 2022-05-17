#TODO: treat files and separate atomic labels from atomic coordinates✅  
#TODO: atomic coordinates -> matrix 
#TODO: atomic labels -> dictionary❔ 

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
     
    # print(atoms1, coords1)
    # print('\n')        
    # print(atoms2, coords2)
    return atom1, coord1, atom2, coord2

def readXYZ(arr1 = [], arr2 = []):
    #Receive array w/ atoms and array w/ coordinates 
    atoms1, coords1, atoms2, coords2 = separator(arr1, arr2) 
    
    
    
    # print(arr1) 
    # print('\n')
    # print(arr2)
    
    