from dash import Dash, html, dcc 
from . import navbar

MAIN_THEME = 'https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sandstone/bootstrap.min.css'

def create_layout(app):
    return html.Div(
        className='app-div',
        children=[html.Div(
            children=[navbar.main_navbar(app)]
            )], 
        
    )