import click as clk
import numpy as np
from src.analyzer import RMSD, Kabsch, full

#TODO: treat clk.option into Testing(); 
#TODO: options calling functions from 'analyzer.py' 

@clk.command()
@clk.argument('fname1', type=clk.File('r'))        
@clk.argument('fname2', type=clk.File('r'))

#⚠ 
#if the options are comments, then, it runs normally
#if the options are implemented here, then it don't run 
#I believe that I have to declare the options in the Testinbg() function

@clk.option('--full', nargs=2, type=clk.File(), help='Run and print full calculation (RMSD + Kabsch)')
@clk.option('--rmsd', nargs=2, type=clk.File(), help='Run  and print only RMSD calculation')
@clk.option('--kabsch', nargs=2, type=clk.File(), help='Run and print only Kabsch calculation')
#⚠ 

def inputFiles(fname1, fname2, rmsd, kabsch, full): 
    """
    COORDINATES ANALYZER\n

    Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.
   
    * Mathematical Methods *
    
    -> RMSD;\n
    -> Kabsch algorithm.
    """
    if rmsd: 
        line1, line2 = treatEntry(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separator(line1, line2) 
        f_matrix1, f_matrix2 = formatXYZ(coords1, coords2, atoms1, atoms2)
        RMSD(f_matrix1, f_matrix2)
    elif kabsch:
        line1, line2 = treatEntry(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separator(line1, line2) 
        f_matrix1, f_matrix2 = formatXYZ(coords1, coords2, atoms1, atoms2)
        Kabsch(f_matrix1, f_matrix2)
    elif full: 
        line1, line2 = treatEntry(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separator(line1, line2) 
        f_matrix1, f_matrix2 = formatXYZ(coords1, coords2, atoms1, atoms2)
        full(f_matrix1, f_matrix2)
        
def treatEntry(filename1, filename2):
    lines1 = [] 
    lines2 = []
    for first_pointer in filename1:
        for line in first_pointer.strip().split(): 
            lines1.append(line)
            
    for second_pointer in filename2: 
        for line in second_pointer.strip().split():
            lines2.append(line)

    #separator(lines1, lines2)
    return lines1, lines2

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
     
    #formatXYZ(coord1, coord2)
    return atom1, coord1, atom2, coord2


def formatXYZ(arr_coords1 = [], arr_coords2 = [], arr_atoms1 = [], arr_atoms2 = []):
    #Receive array w/ atoms and array w/ coordinates 
    #atoms1, coords1, atoms2, coords2 = separator(arr1, arr2)
    
    #Convert to float and transform array to matrix 
    mtx1 = np.array(arr_coords1, dtype='float64')
    mtx2 = np.array(arr_coords2, dtype='float64')
    matrix1 = np.asmatrix(mtx1)
    matrix2 = np.asmatrix(mtx2)
    
    #Create the shape and generate both matrices
    row_mtx1 = len(arr_atoms1)
    row_mtx2 = len(arr_atoms2)
    shape_mtx1 = (row_mtx1, 3)
    shape_mtx2 = (row_mtx2, 3) 
    matrix1 = mtx1.reshape(shape_mtx1)
    matrix2 = mtx2.reshape(shape_mtx2)
    
    return matrix1, matrix2
    
    #Create an empty matrix is necessary for proceed w/ the calculations 
    #Since Kabsch returns a matrix (rotational matrix), we need to have and empty matrix to acomodate the results being passed
    # result = np.zeros((len(matrix1),3))
    
    # for i in range(len(matrix1)):
    #     for j in range(len(matrix1[0])):
    #         result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    # print(result)

if __name__ == '__main__':
    inputFiles() 
    
    
    



    
    
    

