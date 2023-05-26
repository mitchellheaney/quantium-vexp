from dash import Dash, html, dcc 
import plotly.express as px
import pandas as pd

def main():
    app = Dash(__name__)
    df = pd.read_csv("filtered.csv")
    fig = px.line(df, x="date", y="sales", title="Sales Change After Price Increase In Pink Morsel From 15th of January, 2021")

    app.layout = html.Div(children=[
        html.H1(children='Pink Morsel Sales Dashboard'),

        html.Div(children='''
            Highlighting how Pink Morsel sales have changed from price increases.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
    app.run_server(debug=True)

if __name__ == "__main__":
    main()