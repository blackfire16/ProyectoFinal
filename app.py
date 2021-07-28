import dash
import dash_core_components as dcc    
import dash_html_components as html
import dash_bootstrap_components as dbc

import pandas as pd
import os


dataset = pd.read_csv(os.path.join('data', 'COVID-19-geographic-disbtribution-worldwide.csv'))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


grouped_by_country = dataset.groupby('continentExp').sum()
cases_by_continent = grouped_by_country['cases']
death_by_continent = grouped_by_country['deaths']

grouped_by_country = dataset.groupby('countriesAndTerritories').sum()
cases_by_country = grouped_by_country['cases']
death_by_country = grouped_by_country['deaths']


app.layout = html.Div(children = [
    html.Div(children = [
        dbc.Row(
            [
                dbc.Col(html.H1("Proyecto Semestral"), width=2)
            ],
            justify="center"
        ),
        dbc.Row(
            [
                dbc.Col(html.H3("Edgar Gutierrez 8-921-2371"), width=4)
            ],
            justify="start"
        ),
        dbc.Row(
            [
                dbc.Col(html.H3("Jesus Sevillano 8-931-2043"), width=4)
            ],
            justify="start"
        ),
        dbc.Row(
            [
                dbc.Col(html.H3("Consiglieri Alberto 20-70-3971"), width=4)
            ],
            justify="start"
        ),
        dbc.Row(
            [
                dbc.Col(html.Img(src=app.get_asset_url('CasosCoronavirus.png')))
            ],
            justify="center"
        )
    ]),
    dcc.Graph(
        id = 'death_by_continent',
        figure = {
            'data' : [
                {'x' : death_by_continent.index,
                'y' : death_by_continent,
                'type' : 'bar'}
            ],
            'layout' : {
                'title' : 'Muerte por continente'
            }
        }
    ),
    dcc.Graph(
        id = 'death_by_country',
        figure = {
            'data' : [
                {'x' : death_by_country.index,
                'y' : death_by_country,
                'type' : 'bar'}
            ],
            'layout' : {
                'title' : 'Muerte por pais'
            }
        }
    ),
    dcc.Graph(
        id = 'cases_by_continent',
        figure = {
            'data' : [
                {'x' : cases_by_continent.index,
                'y' : cases_by_continent,
                'type' : 'bar'}
            ],
            'layout' : {
                'title' : 'Casos por continente'
            }
        }
    ),
    dcc.Graph(
        id = 'cases_by_country',
        figure = {
            'data' : [
                {'x' : cases_by_country.index,
                'y' : cases_by_country,
                'type' : 'bar'}
            ],
            'layout' : {
                'title' : 'Casos por pais'
            }
        }
    )

])


if __name__ == '__main__':
    app.run_server(debug=True)
