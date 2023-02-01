from dash import Dash, html, dcc
from components.layouts import *


def main():
    app = Dash(
        external_stylesheets=[
            MAIN_THEME
        ]
    )
    app.title = 'Coordinates Analyzer'
    app.layout = create_layout(app)
    app.run()

if __name__ == '__main__':
    main()