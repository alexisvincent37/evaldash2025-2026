from dash import callback, Input, Output
import pandas as pd

df = pd.read_csv("data/avocado.csv")

@callback(
    Output('data-table', 'data'),
    Input('region-filter', 'value'),
    Input('type-filter', 'value')
)
def update_table(selected_region, selected_type):
    filtered_df = df[df['region'] == selected_region]
    
    if selected_type != 'Tous':
        filtered_df = filtered_df[filtered_df['type'] == selected_type]
    
    return filtered_df.to_dict('records')