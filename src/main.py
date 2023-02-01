from dash import Dash, html, dcc
from dash_bootstrap_components.themes import BOOTSTRAP 

from components.layout import create_layout


def main():
    app = Dash(
        external_stylesheets=[
            BOOTSTRAP
        ]
    )
    app.title = 'Coordinates Analyzer'
    app.layout = create_layout(app)
    app.run()

if __name__ == '__main__':
    main()