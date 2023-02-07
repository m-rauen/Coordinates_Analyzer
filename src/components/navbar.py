import dash_bootstrap_components as dbc
from dash import Dash, html

MENU_ITEMS = [
    dbc.DropdownMenuItem('Plot Molecules', header=True, href='#'),
    #dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem('Compare Molecules', header=True, href='#'),
]

LOGO = '/assets/images/logo_element.png'

def main_navbar(app):
    navbar = dbc.Navbar(
        html.Div(
            [
                dbc.Row([
                    dbc.Col(html.Div(html.Img(src=LOGO, width='80px'))),
                    dbc.Col(html.Div(app.title), align='center', class_name='app-name', width='auto'),
                    dbc.Col(html.Div(dbc.DropdownMenu(
                        MENU_ITEMS,
                        label='',
                        )), class_name='app-menu', align='center')
                ], justify='end')
            ], 
            className='app-main-div'
        ),
        class_name='app-main-nav',
        color='#393737'
    )
    
    # navbar = dbc.Navbar(
    #     html.Div([
    #     dbc.Row([
    #         dbc.Col(html.Div(
    #             children=[
    #                 html.Img(src=LOGO, height='80px'),
    #                 html.H1('Coordinates Analyzer')
    #             ]
    #             ), className='app-name'),
    #         dbc.Col(html.Div(
    #             dbc.DropdownMenu(
    #                 MENU_ITEMS,
    #                 label='Menu',
    #                 class_name='app-tst',
    #                 #in_navbar=True,
    #                 #nav=True
    #             ),
    #             className='app-menu', 
    #         ))
            
    #     ], justify='between')
    # ], className='app-nav')
    # )
    
    return navbar


