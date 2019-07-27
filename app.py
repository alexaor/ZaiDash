import os
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server

graph_height = 400
main_container_width = 2000

app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'First graph',
                'height': graph_height
            }
        }
    ),
    html.Div(
        [
            dcc.Graph(
                id='example-graph2-1',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'height': graph_height / 2

                    }
                }
            ),
            dcc.Graph(
                id='example-graph2-2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'height': graph_height / 2
                    }
                }
            )
        ],
        style={'display': 'flex', 'flex-flow': 'column '}),

    dcc.Graph(
        id='example-graph3',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'height': graph_height
            }
        }
    ),
    dcc.Graph(
        id='example-graph4',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'height': graph_height
            }
        }
    ),
    dcc.Graph(
        id='example-graph5',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'height': graph_height
            }
        }
    ),
    html.Div(
        [
            dcc.Graph(
                id='example-graph6-1',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'height': graph_height / 4

                    }
                }
            ),
            dcc.Graph(
                id='example-graph6-2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'height': graph_height / 4
                    }
                }
            ),
            dcc.Graph(
                id='example-graph6-3',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'height': graph_height / 4

                    }
                }
            ),
            dcc.Graph(
                id='example-graph6-4',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'height': graph_height / 4
                    }
                }
            )
        ],
        style={'display': 'flex', 'flex-flow': 'column '}
    )
], style={
    'display': 'grid',
    'grid-template-columns': 'minmax(700px, 20%) minmax(700px, 20%)',
    'grid-template-rows': '1fr 1fr 1fr',
    'box-sizing': 'border-box',
    'width': '100%',
    'justify-content': 'center'


}
)

if __name__ == '__main__':
    app.run_server(debug=True)
