import numpy as np 
import click 

#in output_result() we can differentiate results by their type (list = Kabsch // numpy.float64 = RMSD) 
#------------------------------------
# if teste_de_lista == []:
#     print('sepa vai dar boa')
# else:
#     print('sepa n vai dar boa')
#------------------------------------

def output_fullResults():
    print('hello world')


def output_onlyRMSD(rmsd):
    msg_rmsd = click.wrap_text(
    """
    COORDINATES ANALYZER\n
    Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.\n
    * Results *\n
    -> RMSD = {}
    """
    .format(rmsd), width=78, preserve_paragraphs=True)
    
    click.echo(msg_rmsd, err=True)
    
def output_onlyKabsch(rotat_mtx, rotat_P_mtx):
    for rotat_elements in rotat_mtx: 
        np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
    
    print(f"""
              COORDINATES ANALYZER\n 
              Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.\n
              * Results *\n 
              Rotational:\n 
              {rotat_elements}
              """, end='\n')
    
    # msg_kabsch = click.wrap_text(
    # """
    # COORDINATES ANALYZER\n
    # Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.\n
    # * Results *\n
    # -> R = {}\n
    # -> P_rotated = {}
    # """
    # .format(rotat_mtx, rotat_P_mtx), width=78, preserve_paragraphs=True)
    
    # click.echo(msg_kabsch, err=True)
    
    # print('Rotational:\n {} \n\n'
    #       'P_rotated: \n {}'.format(np.matrix(matrix_R), np.matrix(rot_matrixP)))
    
    
    
    

    





    