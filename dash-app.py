from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

def main():
    """app = Dash(__name__)
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
    app.run_server(debug=True)"""
    app = Dash(__name__)
    df = pd.read_csv("filtered.csv")
    app.layout = html.Div([
        html.Div(
            dcc.Graph(id='graph',
                    style={'height': 400, 'width': 800}
                    ),
        ),
        html.Div([
                    dcc.RadioItems(
                        ['All', 'North', 'East', 'South', 'West'],
                        'All',
                        id='radio',
                        style={"width": "19%", 
                               "font-size": "20px", 
                               "font-family": "Arial", 
                               "color": "Black", 
                               "border":"2px black solid", 
                               "border-radius": "5px", 
                               "background": "LightGray",
                               "padding": "5px 5px"},
                        inline=True
                    ),
            ]),
    ])


    # ---------------------------------------------------------------
    @app.callback(
        Output('graph', 'figure'),
        Input(component_id='radio', component_property='value')
    )
    def build_graph(value):
        if value == 'All':
            return px.line(df, x="date", y="sales", title="All Sales Change After Price Increase In Pink Morsel From 15th of January, 2021")
        elif value == 'North':
            return px.line(df[df['region'] == 'north'], x="date", y="sales", title="North Sales Change After Price Increase In Pink Morsel From 15th of January, 2021")
        elif value == 'East':
            return px.line(df[df['region'] == 'east'], x="date", y="sales", title="East Sales Change After Price Increase In Pink Morsel From 15th of January, 2021") 
        elif value == 'South':
            return px.line(df[df['region'] == 'south'], x="date", y="sales", title="South Sales Change After Price Increase In Pink Morsel From 15th of January, 2021") 
        else:
            return px.line(df[df['region'] == 'west'], x="date", y="sales", title="West Sales Change After Price Increase In Pink Morsel From 15th of January, 2021") 
        
    app.run_server(debug=True)

if __name__ == '__main__':
    main()