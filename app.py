import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    use_pages=True,
    suppress_callback_exceptions=True
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Affichage des données", href="/table")),
            dbc.NavItem(dbc.NavLink("Comparaison entre régions", href="/compare")),
            dbc.NavItem(dbc.NavLink("Aide en ligne", href="/markdown")),
        ],
        brand="Application des M2 MECEN",
        color="primary",
        dark=True,
        className="mb-4"
    ),
    dbc.Container(dash.page_container, fluid=True)
])

@app.callback(
    Output('url', 'pathname'),
    Input('url', 'pathname')
)
def redirect_to_home(pathname):
    if pathname == '/':
        return '/table'
    return dash.no_update

if __name__ == "__main__":
    app.run(debug=False)