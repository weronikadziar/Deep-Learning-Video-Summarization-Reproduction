from csv import reader
from wsgiref import headers
import pandas as pd
import numpy as np
from pyparsing import dict_of

def generate_dict():
    df = pd.read_csv("./dataset/annotations/query_frame_annotations_test.csv")
    dict_of_frames = {}
    for i, row in df.iterrows():
        if row['imageURL'] in dict_of_frames:
            dict_of_frames[row['imageURL']].append(row['Relevance'])
        else:
            dict_of_frames[row['imageURL']] = [row['Relevance']]

def generate_scores_simple_count(dict_of_frames):
    res = [] 
    for rec in dict_of_frames:
        res.append((rec, np.argmax(np.bincount(dict_of_frames[rec]))))
    return res

dict_of_frames = generate_dict()
print(dict_of_frames)
res = generate_scores_simple_count(dict_of_frames)
print(res)
