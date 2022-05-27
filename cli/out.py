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


def output_singleResult(final_result):
    msg_rmsd = click.wrap_text(
    """
    COORDINATES ANALYZER\n
    Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.\n
    * Results *\n
    -> RMSD = {}
    """
    .format(final_result), width=78, preserve_paragraphs=True)
    
    # msg_kabsch = click.wrap_text(
    # """
    # COORDINATES ANALYZER\n
    # Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.\n
    # * Results *\n
    # -> R = {}\n
    # -> P_rotated = {}
    # """
    # .format(final_result), width=78, preserve_paragraphs=True)
    
    if final_result == []:
        print('kabsch')
    else:
        click.echo(msg_rmsd, err=True)
    





    