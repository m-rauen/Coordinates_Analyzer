from dash import Dash, html, dcc 
from . import navbar

def create_layout(app):
    return html.Div(
        className='app-div',
        children=[html.Div(
            children=[navbar.main_navbar(app)]
            )], 
        
    )