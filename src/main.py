from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from components.layout import create_layout


def main():
    app = Dash(
        external_stylesheets=[
            dbc.themes.BOOTSTRAP
        ]
    )
    app.title = 'Coordinates Analyzer'
    app.layout = create_layout(app)
    app.run()

if __name__ == '__main__':
    main()