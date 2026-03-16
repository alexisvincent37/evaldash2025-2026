import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
import pages.compare_cb

dash.register_page(__name__, path='/compare', name="Comparaison régions")

df = pd.read_csv("data/avocado.csv")
regions = sorted(df['region'].unique())

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.H3("Prix moyen dans le temps", 
                    className="text-white p-2 mb-4", 
                    style={'backgroundColor': '#007bff', 'borderRadius': '5px'}),
            width=12
        )
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Badge("Région 1:", color="info", pill=True, className="mb-2"),
            dcc.Dropdown(id='region-1-dropdown', options=[{'label': r, 'value': r} for r in regions], value=regions[0], clearable=False)
        ], xs=12, md=6, className="mb-4"),
        
        dbc.Col([
            dbc.Badge("Région 2:", color="info", pill=True, className="mb-2"),
            dcc.Dropdown(id='region-2-dropdown', options=[{'label': r, 'value': r} for r in regions], value=regions[1], clearable=False)
        ], xs=12, md=6, className="mb-4"),
    ]),

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(id='graph-region-1'))), xs=12, md=6),
        dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(id='graph-region-2'))), xs=12, md=6),
    ])
], fluid=True)