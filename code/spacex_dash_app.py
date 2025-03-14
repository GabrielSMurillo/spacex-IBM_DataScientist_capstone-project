# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX launch data into a pandas DataFrame
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Calculate the minimum and maximum payload mass for the slider
min_payload = spacex_df['Payload Mass (kg)'].min()
max_payload = spacex_df['Payload Mass (kg)'].max()

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    # App title
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Add a dropdown list to enable Launch Site selection.
    # Default option is "All Sites"
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
        ],
        value='ALL',
        placeholder="Select a Launch Site",
        searchable=True
    ),
    html.Br(),

    # TASK 2: Add a pie chart to show the total successful launches count for all sites.
    # If a specific launch site is selected, show the success vs. failure counts for that site.
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    
    # Display label for the payload slider
    html.P("Payload range (Kg):"),
    
    # TASK 3: Add a range slider to select payload mass range
    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=1000,
        marks={i: f'{i}' for i in range(int(min_payload), int(max_payload)+1, 2500)},
        value=[min_payload, max_payload]
    ),
    html.Br(),
    
    # TASK 4: Add a scatter chart to show the correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])

# TASK 2: Callback function for updating the pie chart based on the selected launch site
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(selected_site):
    """
    Update the pie chart based on the selected launch site.
    If 'ALL' is selected, display the total success launches by site.
    Otherwise, filter the DataFrame for the selected site and display success vs. failure counts.
    """
    if selected_site == 'ALL':
        # For all sites, group by 'Launch Site' using the 'class' column as measure
        fig = px.pie(spacex_df, 
                     names='Launch Site', 
                     values='class', 
                     title='Total Success Launches by Site')
    else:
        # Filter the DataFrame for the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        # Count outcomes (success = 1, failure = 0)
        outcome_counts = filtered_df['class'].value_counts().reset_index()
        outcome_counts.columns = ['Outcome', 'Count']
        fig = px.pie(outcome_counts, 
                     names='Outcome', 
                     values='Count', 
                     title=f"Launch Outcomes for {selected_site}")
    return fig

# TASK 4: Callback function for updating the scatter plot based on selected launch site and payload range
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_plot(selected_site, payload_range):
    """
    Update the scatter plot based on the selected launch site and payload range.
    Filter the DataFrame based on payload mass and, if a specific site is selected,
    filter by that site as well. The scatter plot shows the correlation between payload mass
    and launch success, with the color indicating the Booster Version.
    """
    low, high = payload_range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & 
                            (spacex_df['Payload Mass (kg)'] <= high)]
    
    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
    
    fig = px.scatter(filtered_df, 
                     x='Payload Mass (kg)', 
                     y='class', 
                     color='Booster Version',
                     title='Correlation between Payload and Launch Success')
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)