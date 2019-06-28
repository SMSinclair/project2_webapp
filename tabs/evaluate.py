from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Data and Process
This model uses a dataset with 7398 movies and a variety of metadata from [The Movie Database (TMDB)](http://www.themoviedb.org).
The dataset was obtained from a [Kaggle competition](https://www.kaggle.com/c/tmdb-box-office-prediction/overview) 
where the objective was to predict worldwide revenue for 4398 of the movies in the test set.

After importing the data from .csv files, many features were originally string representations of lists 
of dictionaries, and dates were represented in string format. I converted the string representations into
lists of dictionaries and converted the release dates in to dateime objects to extract relevant datetime features. 

Then, I made binary features to indicate whether the movie belongs to a collection, was released, and whether it
has a homepage. Since movies have multiple genres, I created lists of all the genres that apply to each movie then
one-hot encoded these lists. I used ordinal encoding to encode particular production companies, the full genre 
lists, and particular collections that the movies belong to. 

However, the model deployed here is a simplification of my original model. This model does not use any of the 
features that I used ordinal encoding on, and it also discards a feature that I consider to be leakage. A 
production company would not have data on the popularity of their movie when they're trying to project
how profitable it might be and decide whether or not to green light it, so the inclusion of this data would
be a kind of "time travel."

The exclusion of this data did not make the model significantly worse. The root mean squared log errors of the 
best Kaggle submissions for both models were:

Original: 2.12250
Simplified: 2.22215

For more details, check out my [github repo](https://github.com/SMSinclair/Predictive-Modeling-Portfolio-Project).

"""), ]