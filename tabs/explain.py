from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Insights

From the permutation importances below you can see the relative importance of each feature included in this model.
Budget was the most important feature, and this makes sense. Higher budget movies can recruit bankable stars, attract
talented crew, and spend the money on advertising that is required for a wide release:
"""), 

html.Img(src='/assets/perm_importances.png', style={'width':'30%'}),

dcc.Markdown("""
Although the month of release is not one of the top factors, a partial dependence plot of release_month does seem
to confirm the conventional wisdom about ["dump months"](https://en.wikipedia.org/wiki/Dump_months) in the 
entertainment industry. In September, young people spend their disposible income on school supplies and many people
start spending their time watching football. This leads to depressed box office revenues in September, October, and 
November: 
"""),

html.Img(src='/assets/release_month_pdp.png', style={'width':'100%'}),
]