import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, path='/markdown', name="Aide en ligne")

def read_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

layout = dbc.Container([
    html.H1("Aide & Informations", className="my-4"),

    dbc.Accordion([
        dbc.AccordionItem(
            dcc.Markdown(read_md("assets/expli1.md")),
            title="Accueil"
        ),
        dbc.AccordionItem(
            dcc.Markdown(read_md("assets/expli2.md")),
            title="Layout"
        ),
        dbc.AccordionItem(
            dcc.Markdown(read_md("assets/expli3.md")),
            title="CallBack"
        ),
    ])
], fluid=True)