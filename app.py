import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle

####### Intiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/BWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='knn'

####### Read in the model and the dataset
training = pd.read_pickle('resources/training_dataset.pkl')
filename = open('resources/final_model.pkl', 'rb')
model = pickle.load(filename)
filename.close()


####### Set up the layout
app.layout = html.Div([
    html.H1('This is my KNN model for predicting a NBA players position'),
    dcc.Slider(
        id='slider-no-1',
        min=1,
        max=10,
        marks={i:str(i) for i in range(1,11)},
        step=0.5,
        value=5
    ),
    html.Br(),
    html.Br(),
    dcc.Slider(
        id='slider-no-2',
        min=1,
        max=10,
        marks={i:str(i) for i in range(1,11)},
        step=0.5,
        value=5
    ),
    html.Br(),
    html.Br(),
    dcc.Slider(
        id='slider-no-3',
        min=1,
        max=10,
        marks={i:str(i) for i in range(1,11)},
        step=0.5,
        value=5
    ),
    html.Br(),
    html.Br(),
    dcc.Slider(
        id='slider-no-4',
        min=1,
        max=10,
        marks={i:str(i) for i in range(1,11)},
        step=0.5,
        value=5
    ),
    html.Br(),
    html.Br(),
    dcc.Slider(
        id='slider-no-5',
        min=1,
        max=10,
        marks={i:str(i) for i in range(1,11)},
        step=0.5,
        value=5
    ),
    html.Br(),
    html.Br(),
    html.H6(id='my-output-message-here', children='')
])

@app.callback(Output('my-output-message-here', 'children'),
                [Input('slider-no-1', 'value'),
                Input('slider-no-2', 'value'),
                Input('slider-no-3', 'value'),
                Input('slider-no-4', 'value'),
                Input('slider-no-5', 'value')]
)
def make_prediction(input0, input1, input2, input3, input4):
    new_observation = [[input0, input1, input2, input3, input4]]
    predication=model.predict(new_observation)
    player=['Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center']
    return f'The position of your NBA player is: {player[prediction[0]]}'

####### Deploy my app
if __name__=='__main__':
    app.run_server()
