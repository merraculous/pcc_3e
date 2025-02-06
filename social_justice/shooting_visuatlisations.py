from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

# read data and process
df = pd.read_csv('data/mapping_police_violence_snapshot_061920.csv')

df = df[df['State'] != 'Data from 1/1/2013 - 12/31/2019']
df.dropna(how='all', inplace=True)
df.fillna(0, inplace=True)

# Define dropdown options for people killed
ppl_options = [
    {"value": "# Black people killed", "label": "Black people"},
    {"value": "# Hispanic people killed", "label": "Hispanic people"},
    {"value": "# Native American people killed", "label": "Native Americans"},
    {"value": "# Asian people killed", "label": "Asian people"},
    {"value": "# Pacific Islanders killed", "label": "Pacific Islanders"},
    {"value": "# White people killed", "label": "White people"},
    {"value": "# Unknown Race people killed", "label": "Unknown Race"},
]

app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

app.layout = dbc.Container(
    children=[
        # Banner Section
        dbc.Row(
            dbc.Col(
                html.Div(
                    className="banner",
                    children=[
                        # Change App Name here
                        html.Div(
                            className="container scalable",
                            children=[
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
                width={"size": 12, "order": 1, "offset": 0},
            )
        ),

        # Main Body Section
        dbc.Row(
            children=[
                # Left Column with Dropdowns
                dbc.Col(
                    children=[
                        dbc.Card(
                            id="first-card",
                            children=[
                                dbc.CardBody(
                                    [
                                        dbc.Label("Select State"),
                                        dcc.Dropdown(
                                            id="state-dropdown",
                                            options=[{"label": state, "value": state} for state in
                                                     df["State"].unique()],
                                            value=['Alabama'],
                                            multi=True,
                                            clearable=False,
                                            searchable=False,
                                        ),
                                    ]

                                ),
                            ],
                        ),
                        dbc.Card(
                            id="last-card",
                            children=[
                                dbc.CardBody(
                                    [
                                        dbc.Label("Select Data"),
                                        dcc.Dropdown(
                                            id="ppl-dropdown",
                                            options=ppl_options,
                                            value=['# Black people killed'],
                                            multi=True,
                                            clearable=False,
                                            searchable=False,
                                        ),
                                    ]

                                ),
                            ],
                        ),
                    ],
                    width=3,  # Adjust the column width as necessary
                ),

                # Graph Section
                dbc.Col(
                    dcc.Graph(
                        id="line-chart",
                        figure={},
                        className="row",
                    ),
                    width=8,# Adjust the column width as necessary
                ),
            ],
        ),
    ],
    fluid=True,  # Makes the container responsive
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

    # when no states chosen empty graph
    if len(state_value) == 0:
        return {}

    # otherwise create graph
    df_filtered = df[df["State"].isin(state_value)]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_filtered["State"],
        y=df_filtered["# People Killed"],
        name="Total People Killed",
        offsetgroup=0,
        hovertemplate="<br>".join([
            "State: %{x}",
            f"Population: {df_filtered["Population"].iloc[0]}",
            "Total People Killed: %{y}",
        ]),
    ))

    base = [0] * len(df_filtered["State"])
    for chosen in ppl_value:

        fig.add_trace(go.Bar(
            x=df_filtered["State"],
            y=df_filtered[chosen],
            name=chosen,
            offsetgroup=1,
            base=base,
            hovertemplate="<br>".join([
                "State: %{x}",
                f"Population: {df_filtered["Population"].iloc[0]}",
                f"{chosen}: {int(df_filtered[chosen].iloc[0])} ",
            ]),
        ))

        base = [base_value + model_value for base_value, model_value in zip(base, df_filtered[chosen])]

    fig.update_layout(
        plot_bgcolor = '#d9e3f1',
        paper_bgcolor = '#d9e3f1'
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
