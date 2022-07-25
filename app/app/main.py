"""main.py"""
import dash_bootstrap_components as dbc

from dash import (
    Dash, dcc, html,
    Input, Output, State
)
from steam_achievements.achvm.steam_achvm import steam_achvm


app = Dash(
    external_stylesheets=[dbc.themes.DARKLY],
    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

steam_data = dcc.Store(id='intermediate-value')

header = dbc.Row(
    dbc.Col(
        html.Header(html.P('Steam Achievements'), className='display-3 p-5 text-center'),
        width=12
    )
)

body = html.Div([
    dbc.Row([
        dbc.Col(html.Div([
            html.P('Select a game', className='lead')
        ], className='p-3'), width=4),
        dbc.Col(width=8)
    ])
])


app.layout = dbc.Container(
    [
        header,
        body,
        steam_data
    ],
    fluid=True
)


@app.callback(Output('intermediate-value', 'data'),)
def clean_data(value):
    pass


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
