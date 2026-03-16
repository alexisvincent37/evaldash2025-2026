from dash import callback, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/avocado.csv")
df['Date'] = pd.to_datetime(df['Date'])

@callback(
    Output('graph-region-1', 'figure'),
    Output('graph-region-2', 'figure'),
    Input('region-1-dropdown', 'value'),
    Input('region-2-dropdown', 'value')
)
def update_graphs(reg1, reg2):
    df1 = df[df['region'] == reg1].sort_values("Date")
    df2 = df[df['region'] == reg2].sort_values("Date")
    
    y_min = df['AveragePrice'].min()
    y_max = df['AveragePrice'].max()
    
    fig1 = px.line(df1, x="Date", y="AveragePrice", title=f"Prix moyen dans le temps - {reg1}")
    fig2 = px.line(df2, x="Date", y="AveragePrice", title=f"Prix moyen dans le temps - {reg2}")
    
    for fig in [fig1, fig2]:
        fig.update_yaxes(
            range=[y_min, y_max], 
            title="Prix moyen ($)", 
            showgrid=True, 
            gridcolor='LightGrey'
        )
        fig.update_xaxes(
            title="Date", 
            showgrid=True, 
            gridcolor='LightGrey'
        )
        fig.update_layout(
            margin=dict(l=40, r=20, t=40, b=40),
            hovermode="x unified",
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
    return fig1, fig2