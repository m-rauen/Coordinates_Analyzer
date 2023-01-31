from dash import Dash, html, dcc 

def create_layout(app):
    return html.Div(
        className = 'app-div',
        children = [
            html.H1(app.title),
            html.Hr()
        ]
    )