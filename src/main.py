from dash import Dash, html, dcc

from src.components.layout import create_layout

def main():
    app = Dash()
    app.title - 'Coordinates Analyzer'
    app.layout = create_layout(app)
    app.run()

if __name__ == '__main__':
    main()