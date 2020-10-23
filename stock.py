import dash
import numpy as np
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

stocks_df = pd.read_csv('C:/Users/hc-administrator/Downloads/stock.csv')
stocks_daily_return = daily_return(stocks_df)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

header = html.H2(children="Stock Market Analysis")

show_plot(normalize(stocks_df), 'NORMALIZED STOCK PRICES')

graph1 = dcc.Graph(
        id='graph1',
        figure=show_plot,
        className="six columns"
    )

interactive_plot(normalize(stocks_df), 'Normalized Prices')

graph2 = dcc.Graph(
        id='graph2',
        figure=interactive_plot,
        className="six columns"
    )

interactive_plot(stocks_daily_return, 'STOCKS DAILY RETURNS')

graph3 = dcc.Graph(
        id='graph2',
        figure=interactive_plot,
        className="six columns"
    )

interactive_plot(stocks_df, 'Prices')

graph4 = dcc.Graph(
        id='graph2',
        figure=interactive_plot,
        className="six columns"
    )


row1 = html.Div(children=[graph1,graph2],)

row2 = html.Div(children=[graph2, graph4])

layout = html.Div(children=[header, row1], style={"text-align": "center"})

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)