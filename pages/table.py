import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
import pandas as pd
import pages.table_cb

dash.register_page(__name__, path='/table', name="Affichage des données")

df = pd.read_csv("data/avocado.csv")
regions = sorted(df['region'].unique())
types = sorted(df['type'].unique())

layout = dbc.Container([
    html.H1("Affichage des données", className="my-4"),
    dbc.Row([
        dbc.Col([
            html.Label("Sélectionner une région :"),
            dcc.Dropdown(
                id='region-filter',
                options=[{'label': r, 'value': r} for r in regions],
                value=regions[0],
                clearable=False
            )
        ], xs=12, md=6, className="mb-3"),
        dbc.Col([
            html.Label("Sélectionner un type :"),
            dcc.Dropdown(
                id='type-filter',
                options=[{'label': 'Tous', 'value': 'Tous'}] + [{'label': t, 'value': t} for t in types],
                value='Tous',
                clearable=False
            )
        ], xs=12, md=6, className="mb-3"),
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='data-table',
                columns=[{"name": i, "id": i} for i in df.columns if i not in 
                         ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]],
                data=[],
                page_action='none',
                fixed_rows={'headers': True},
                style_table={'overflowX': 'auto',
                             'maxHeight': '500px',
                             'overflowY': 'auto', 
                             'overflowX': 'auto',},
                style_header={
                    'backgroundColor': "#007bff",
                    'color': 'white',
                    'fontWeight': 'bold'
                },
                style_cell={'textAlign': 'left', 'padding': '10px'},
            )
        ])
    ])
], fluid=True)