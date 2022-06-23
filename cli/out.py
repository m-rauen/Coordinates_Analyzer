import numpy as np 
from rich.console import Console
from rich.markdown import Markdown

console = Console()

title = """ # COORDINATES ANALYZER"""
msg = """

Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates. By default the program runs and print the full calculation, i.e. RMSD and Kabsch algorithm, on a external .xyz file generated. However, you can specify the type of calculation using the options.

If you are interested in the source code, you can find it on my [**Github**](https://github.com/m-rauen/Coordinates_Analyzer).
"""

result_title = Markdown(title)
result_msg = Markdown(msg)

def output_fullResults(rmsd, rotat_mtx, rotat_P_mtx):
    output_rotationalMtx = open('rotatioanl_matrix.xyz', 'w')
    output_rotationalMtx.write(str(len(rotat_mtx)) + '\n')
    output_rotationalMtx.write('RMSD = ' + str(rmsd) + '\n')
    for rotat_elements in rotat_mtx: 
        output_rotationalMtx.write(str(rotat_elements).replace('[','').replace(']',''))
        output_rotationalMtx.write('\n')
        
    output_P_rotated = open('P_rotated.xyz', 'w')
    output_P_rotated.write(str(len(rotat_P_mtx)) + '\n')
    output_rotationalMtx.write('RMSD = ' + str(rmsd) + '\n')
    for protated_elements in rotat_P_mtx:
        output_P_rotated.write(str(protated_elements).replace('[','').replace(']',''))
        output_P_rotated.write('\n')


def output_onlyRMSD(rmsd):
    msg_rmsd = """
    - RMSD = {}
    """.format(rmsd)
    console.print(result_title)
    console.print(result_msg, style='bold dim', soft_wrap=False)
    console.print('\n')
    console.rule('[bold cyan]Results')
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
        
    
  
    
    
    
    # msg_rmsd = """
    # Root-Mean-Square Deviation:
    # RMSD = {}
    # """.format(rmsd)
    
    # msg_rotational = """
    # Rotational Matrix:
    
    # """
    
    # msg_rotatedP = """
    # Matrix P (rotated):
    
    # """    
    # #fmsg_rmsd = Markdown(msg_rmsd)
    # #fmsg_rotational = Markdown(msg_rotational)
    # #fmsg_rotatedP = Markdown(msg_rotatedP)
    
    # console.print(result_msg)
    # console.print('\n')
    # console.rule('[cyan]Results')
    # console.print(msg_rmsd)
    # console.print(msg_rotational, style='dim')
    
    
    # for rotat_elements in rotat_mtx: 
    #     np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
    #     print(str(rotat_elements).replace(']', '').replace('[', ''), end=',\n')
    
    # console.print(msg_rotatedP, style='bold white')
    
    # for rotat_elements in rotat_P_mtx: 
    #     np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
    #     print(str(rotat_elements).replace(']', '').replace('[', ''), end=',\n')

    





    