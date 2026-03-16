import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, path='/markdown', name="Aide en ligne")

def read_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

layout = dbc.Container([
    html.Div([
        dbc.Row([
            dbc.Col(
                html.Div(
                    html.H3("Présentation de Dash", 
                            className="text-white text-center", 
                            style={
                                "textTransform": "uppercase",
                                "fontWeight": "bold",
                                "margin": "0",
                                "paddingTop": "40px",
                                "paddingBottom": "40px"
                            }
                    ),
                    className="p-0",
                    style={
                        "backgroundImage": "url('/assets/dash.jpg')",
                        "backgroundSize": "cover",
                        "backgroundPosition": "center",
                        "minHeight": "120px",
                        "borderRadius": "10px 10px 0 0"
                    }
                ),
                width=12
            )
        ], className="m-0"),

        dbc.Row([
            dbc.Col(
                dbc.Accordion([
                    dbc.AccordionItem(
                        dcc.Markdown(read_md("assets/expli1.md")),
                        title="Accueil",
                        item_id="item-1",
                    ),
                    dbc.AccordionItem(
                        dcc.Markdown(read_md("assets/expli2.md")),
                        title="Layout",
                        item_id="item-2",
                    ),
                    dbc.AccordionItem(
                        dcc.Markdown(read_md("assets/expli3.md")),
                        title="CallBack",
                        item_id="item-3",
                    ),
                ], 
                active_item="item-1",
                flush=True,
                className="p-3"
                ),
                width=12,
                className="p-0"
            )
        ], className="m-0"),

    ], 
    style={
        "backgroundColor": "white",
        "width": "90%",
        "margin": "30px auto",
        "padding": "0",
        "borderRadius": "10px",
        "boxShadow": "0 10px 30px rgba(0,0,0,0.1)"
    })

], fluid=True, style={"backgroundColor": "#f8f9fa", "minHeight": "100vh", "padding": "20px"})