import numpy as np 
from rich.console import Console
from rich.markdown import Markdown

console = Console()

msg = """
# COORDINATES ANALYZER

Python CLI program that mathematically compare 2 sets of molecular structures, based on their atomic coordinates, throughout the Root-Mean-Square Deviation, and, Kabsch algorithm.

If you are interested in the source code, you can find it on my [**Github**](https://github.com/m-rauen/Coordinates_Analyzer).


"""

result_msg = Markdown(msg)

def output_fullResults(rmsd, rotat_mtx, rotat_P_mtx):
    msg_rmsd = """
    Root-Mean-Square Deviation:
    """
    
    msg_rotational = """
    Rotational Matrix:
    
    """
    
    msg_rotatedP = """
    Matrix P (rotated):
    
    """    
    #fmsg_rmsd = Markdown(msg_rmsd)
    #fmsg_rotational = Markdown(msg_rotational)
    #fmsg_rotatedP = Markdown(msg_rotatedP)
    
    console.print(result_msg)
    console.print('\n')
    console.rule('[cyan]Results')
    console.print(msg_rmsd)
    console.print(msg_rotational, style='grey')
    
    
    for rotat_elements in rotat_mtx: 
        np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
        print(str(rotat_elements).replace(']', '').replace('[', ''), end=',\n')
    
    console.print(msg_rotatedP, style='bold white')
    
    for rotat_elements in rotat_P_mtx: 
        np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
        print(str(rotat_elements).replace(']', '').replace('[', ''), end=',\n')


def output_onlyRMSD(rmsd):
    msg_rmsd = """
    - RMSD = {}
    """.format(rmsd)
    console.print(result_msg, style='white', soft_wrap=False)
    console.print('\n')
    console.rule('[cyan]Results')
    console.print(msg_rmsd, style='bold white')
    

    
def output_onlyKabsch(rotat_mtx, rotat_P_mtx):
    msg_kabsch = """
    - Rotational: 
    """
    console.print(result_msg, soft_wrap=False)
    console.print('\n')
    result_rule = console.rule('[bold blue] Results')
    console.print(msg_kabsch)
    np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
    print('\n {} \n'
          .format(np.matrix(rotat_mtx)))
    
    for rotat_elements in rotat_mtx: 
        np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
        print(str(rotat_elements).replace(']', '').replace('[', ''), end=',\n')
        
    
  
    
    
    


    





    