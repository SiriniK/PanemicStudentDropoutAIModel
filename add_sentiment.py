import numpy as np
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def csv_download_link(df, csv_file_name, delete_prompt=True):
    """Display a download link to load a data frame as csv from within a Jupyter notebook"""
    df.to_csv(csv_file_name, index=False)
    from IPython.display import FileLink
    display(FileLink(csv_file_name))
    if delete_prompt:
        a = input('Press enter to delete the file after you have downloaded it.')
        import os
        os.remove(csv_file_name)
data = pd.read_csv("COVID-Bulgaria.csv")
i = 0
data['Sentiment'] = 1
analyzer = SentimentIntensityAnalyzer()
while i < len(data['Do you have some recommendations for improving the quality of distance learning?']):
    sentiment = 1
    comment = str(data['Do you have some recommendations for improving the quality of distance learning?'][i]) 
    if comment != "nan":
        vs = analyzer.polarity_scores(comment)
        if vs['neg'] > 0.1:
            sentiment = -1
    i = i + 1
data    