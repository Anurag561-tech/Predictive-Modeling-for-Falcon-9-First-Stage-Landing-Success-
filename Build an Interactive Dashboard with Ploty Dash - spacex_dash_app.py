
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

spacex_df = pd.read_csv(r"C:\Users\sriva\COURSE_10 photos\spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Creating a dash application
app = dash.Dash(__name__)

# Creating an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                
                                dcc.Dropdown(id='site-dropdown',  
                                              options=[
                                                {'label': 'All Sites', 'value': 'ALL'},
                                                {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
                                              value='ALL',
                                              placeholder='place holder here',
                                              searchable=True
                                              ),
                                html.Br(),
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                dcc.RangeSlider(id='payload-slider', min=min_payload, max=max_payload, step=1000, marks={int(min_payload): str(int(min_payload)), int(max_payload):str(int(max_payload))}, value=[min_payload, max_payload]),

                    
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))

def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig=px.pie(filtered_df, values='class',
        names='Launch Site',
        title='Total Success Launches by Site')
        return fig
    else:
        df7 = filtered_df[filtered_df['Launch Site'] == entered_site]
        df7 = df7.groupby(['Launch Site', 'class']).size().reset_index(name='class count')
        fig=px.pie(df7, values='class count', names='class', title='Total Success Launches for Site {}'.format(entered_site))
        return fig

@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), Input(component_id='payload-slider', component_property='value')])

def get_scatter_chart(site_location, payload):
    filtered_df = spacex_df[spacex_df['Payload Mass (kg)'].between(payload[0],payload[1])]
    if site_location == 'ALL':
        fig=px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color="Booster Version Category", title='Correaltion between payload and success for all sites')
        return fig
    else:
        df8 = filtered_df[filtered_df['Launch Site'] == site_location]
        # df8 = df8.groupby(['Launch Site','class'])['Payload Mass (kg)'].mean().reset_index()
        fig=px.scatter(df8, x='Payload Mass (kg)', y='class', color="Booster Version Category", title='Correaltion between payload and success for site {}'.format(site_location))
        return fig

# Runing the app
if __name__ == '__main__':
    app.run_server()
