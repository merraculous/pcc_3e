from pathlib import Path
import csv

from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import re

import utils.dash_reusable_components as drc

# read data and remove last 3 rows
df = pd.read_csv('data/mapping_police_violence_snapshot_061920.csv')

df = df[df['State'] != 'Data from 1/1/2013 - 12/31/2019']
df.dropna(how='all', inplace=True)

stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    children=[
        # .container class is fixed, .container.scalable is scalable
        html.Div(
            className="banner",
            children=[
                # Change App Name here
                html.Div(
                    className="container scalable",
                    children=[
                        # Change App Name here
                        html.H2(
                            id="banner-title",
                            children=[
                                html.A(
                                    "Police Shootings Snapshot 1/1/2013 - 12/31/2019",
                                    style={
                                        "text-decoration": "none",
                                        "color": "inherit",
                                    },
                                )
                            ],
                        ),
                    ],
                )
            ],
        ),
        html.Div(
            id="body",
            className="container scalable",
            children=[
                html.Div(
                    id="app-container",
                    # className="row",
                    children=[
                        html.Div(
                            # className="three columns",
                            id="left-column",
                            children=[
                                drc.Card(
                                    id="first-card",
                                    children=[
                                        drc.NamedDropdown(
                                            name="Select State",
                                            id="state-dropdown",
                                            multi=True,
                                            options=df["State"].unique(),
                                            value=['Alabama'],
                                            clearable=False,
                                            searchable=False,
                                        ),
                                    ],
                                ),
                                drc.Card(
                                    id="last-card",
                                    children=[
                                        drc.NamedDropdown(
                                            name="Select Data",
                                            id="ppl-dropdown",
                                            multi=True,
                                            options=[
                                                # Options to be which data to list.
                                                {
                                                    "value": "# Black people killed",
                                                    "label": "Black people"
                                                },
                                                {
                                                    "value": "# Hispanic people killed",
                                                    "label": "Hispanic people"
                                                },
                                                {
                                                    "value": "# Native American people killed",
                                                    "label": "Native Americans"
                                                },
                                                {
                                                    "value": "# Asian people killed",
                                                    "label": "Asian people"
                                                },
                                                {
                                                    "value": "# Pacific Islanders killed",
                                                    "label": "Pacific Islanders"
                                                },
                                                {
                                                    "value": "# White people killed",
                                                    "label": "White people"
                                                },
                                                {
                                                    "value": "# Unknown Race people killed",
                                                    "label": "Unknown Race"
                                                },
                                            ],
                                            value=['# Black people killed'],
                                            clearable=False,
                                            searchable=False,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            id="div-graphs",
                            children=dcc.Graph(
                                id="line-chart",
                                figure={},
                                className="row"
                            ),
                        ),
                        # html.Div(
                        #     html.A(
                        #         id="my-link",
                        #         children="Click here to Visit Twitter",
                        #         href="https://twitter.com/explore",
                        #         target="_blank",
                        #     ),
                        #     className="two columns",
                        # ),
                    ],
                )
            ],
        ),
    ]
)

# Callbacks ***************************************************************
@app.callback(
    Output(component_id="line-chart", component_property="figure"),
    [
        Input(component_id="state-dropdown", component_property="value"),
        Input(component_id="ppl-dropdown", component_property="value")
    ],
)
def update_graph(state_value, ppl_value):
    print(f"Values chosen by user: {ppl_value}")

    if len(state_value) == 0:
        return {}
    else:
        df_filtered = df[df["State"].isin(state_value)]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_filtered["State"],
            y=df_filtered["# People Killed"],
            name="Total People Killed",
            hovertemplate="<br>".join([
                "State: %{x}",
                "Total People Killed: %{y}",
            ]),
        ))
        for chosen in ppl_value:
            fig.add_trace(go.Bar(
                x=df_filtered["State"],
                y=df_filtered[chosen],
                name=chosen,
                hovertemplate="<br>".join([
                    "State: %{x}",
                    f"{chosen}:"+" %{y}",
                ]),
            ))

        return fig

if __name__ == "__main__":
    app.run_server(debug=True)
