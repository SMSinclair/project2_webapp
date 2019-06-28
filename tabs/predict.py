from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd

from app import app

genres = ['Foreign', 'Documentary', 'Family', 'Animation', 'Comedy', 'Western', 
          'Adventure', 'Mystery', 'Drama', 'Romance']
months=['January', 'February,', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December']

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict

        Use the controls below to find your predicted box office revenue:
    
    """), 

    html.Div(id='prediction-content', style={'fontWeight':'bold'}), 

    html.Div([
        dcc.Markdown('###### Budget'), 
        dcc.Slider(
            id='budget', 
            min=0,
            max=200000000,
            step=1000000,
            value=18000000, 
            marks={n: f'${n/1000000:.0f}M' for n in range(0,200000000,10000000)} 
        ), 
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Genres'), 
        dcc.Checklist(
            id='genre_selection',
            options=[{'label': genre, 'value': genre} for genre in genres],
            value=[genres[0], genres[1]]
        ),
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Runtime'), 
        dcc.Slider(
            id='runtime', 
            min=60, 
            max=180, 
            step=10, 
            value=120, 
            marks={n: f'{n:.0f}min' for n in range(60,180,10)}
        ),  
    ], style=style),

    html.Div([
        dcc.Markdown('###### Release Month'), 
        dcc.Dropdown(
            id='month', 
            options=[{'label': month, 'value': month} for month in months], 
            value=months[0]
        ), 
    ], style=style),
])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('budget', 'value'),
     Input('genre_selection', 'value'),
     Input('runtime', 'value'),
     Input('month', 'value'),])
def predict(budget, genre_selection, runtime, month):

    genre_dict = {'Foreign':0, 'Documentary':0, 'Family':0, 'Animation':0, 'Comedy':0, 'Western':0, 
          'Adventure':0, 'Mystery':0, 'Drama':0, 'Romance':0}

    month_dict = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8,
        'September':9, 'October':10, 'November':11, 'December':12}

    for i in genre_selection:
        genre_dict[i]=1


    df = pd.DataFrame(
        columns=['budget', 'collection', 'release_year', 'runtime', 
                 'Foreign', 'Documentary', 'Family', 'Animation', 
                 'Comedy', 'Western', 'original_english', 'release_month', 
                 'Adventure', 'Mystery', 'Drama', 'Romance'], 
        data=[[budget, 1, 2019, runtime,
               genre_dict['Foreign'], genre_dict['Documentary'], genre_dict['Family'], genre_dict['Animation'],
               genre_dict['Comedy'], genre_dict['Western'], 1, month_dict[month], 
               genre_dict['Adventure'], genre_dict['Mystery'], genre_dict['Drama'], genre_dict['Romance'] ]]
    )

    pipeline = load('model/pipeline.joblib')
    y_pred_log = pipeline.predict(df)
    y_pred = np.expm1(y_pred_log)[0]
    y_pred_formatted = "{:,}".format(y_pred)

    return f'${y_pred_formatted}0 gross revenue predicted for your movie.'
