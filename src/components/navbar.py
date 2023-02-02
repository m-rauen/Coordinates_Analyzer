import dash_bootstrap_components as dbc
from dash import Dash, html

MENU_ITEMS = [
    dbc.DropdownMenuItem('Plot Molecules', header=True, href='#'),
    #dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem('Compare Molecules', header=True, href='#'),
]

def main_navbar(app):
    navbar = dbc.Container(children=[
        dbc.Navbar(
            class_name='navbar',
            fixed='top',
        )
    ]
)
    return navbar
