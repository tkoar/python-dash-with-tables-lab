#import dash
import dash
#import dash core components as dcc
import dash_core_components as dcc
#import dash html components as html
import dash_html_components as html
from dash.dependencies import Input, Output

# import data about interest of pho/ramen/soba
from dashwithtables.food_interest_data import data

# create dash app and make path '/'
app = dash.Dash(__name__, url_base_pathname='/')
sort_by = ""

def generate_table(table_data=data):
    return html.Table(id='food-table', children=
        # Header
        [html.Tr(id='headers', children=[html.Th(col) for col in table_data[0].keys()])]

        +

        # Body
        [html.Tr(id='row-data', children=[
            html.Td(data_dict[column]) for column in data_dict.keys()
        ]) for data_dict in table_data]
    )

def generate_drop_down():
    return dcc.Dropdown(
        id='sort-by-selector',
        options=[
            {'label': 'Country', 'value': 'Country'},
            {'label': 'Pho', 'value': 'Pho'},
            {'label': 'Ramen', 'value': 'Ramen'},
            {'label': 'Soba', 'value': 'Soba'}
        ],
        value="Country"
    )


app.layout = html.Div(children=[
    generate_drop_down(),
    html.H3(children='Interest in Pho, Ramen, and Soba by Country according to Google Search from 01/2004 - 06/2018'),
    html.Div(id='table_container')
])

@app.callback(
    Output(component_id='table_container', component_property='children'),
    [Input(component_id='sort-by-selector', component_property='value')]
)
def sort_table(input_value):
    global data
    sorted_data = sorted(data, key=lambda datum: datum[input_value])
    return generate_table(sorted_data)
