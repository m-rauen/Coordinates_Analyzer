from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from src.components.layout import *



def main():
    app = Dash(
        __name__, 
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )
    app.scripts.config.serve_locally = False
    app.title = 'Coordinates Analyzer'
    app.layout = create_layout(app)
    app.run()

if __name__ == '__main__':
    main()