from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro

How much money would your movie make?

Pick a budget, genre(s), and runtime.
Then decide when to release.
"""), 

html.Img(src='/assets/jeremy-yap-J39X2xX_8CQ-unsplash.jpg', style={'width':'100%'})]