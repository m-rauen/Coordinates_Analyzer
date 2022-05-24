import click

#in output_result() we can differentiate results by their type (list = Kabsch // numpy.float64 = RMSD) 

def output_fullResults():
    print('hello world')


def output_singleResult(final_result):
    """
    COORDINATES ANALYZER
    
    Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.\n
    
    RMSD = {}
    """.format(final_result)
    
    