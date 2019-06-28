from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro

How much money would your movie make?

See how well your foreign documentary would perform in September!
"""), 

html.Img(src='/assets/jeremy-yap-J39X2xX_8CQ-unsplash.jpg', style={'width':'100%'})]