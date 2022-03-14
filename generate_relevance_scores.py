from csv import reader
from wsgiref import headers
import pandas as pd
import numpy as np
from pyparsing import dict_of

df =pd.read_csv("./dataset/annotations/query_frame_annotations_test.csv")
dict_of_frames = {}

for i, row in df.iterrows():
    if row['imageURL'] in dict_of_frames:
        dict_of_frames[row['imageURL']].append(row['Relevance'])
    else:
        dict_of_frames[row['imageURL']] = [row['Relevance']]

for rec in dict_of_frames:
    print("{} scores: {}".format(rec, dict_of_frames[rec]))
    print("{} scores: {}".format(rec, np.argmax(np.bincount(dict_of_frames[rec]))))