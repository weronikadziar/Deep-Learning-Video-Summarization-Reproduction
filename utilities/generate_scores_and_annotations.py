from csv import reader
from wsgiref import headers
import pandas as pd
import numpy as np
from pyparsing import dict_of
from collections import Counter

def save_to_file(a, file_name):
    f = open("{}.csv".format(file_name), "a")
    for word in a:
        f.write("{}\n".format(word))
    f.close()

dataset = 'val'
df =pd.read_csv("./dataset/annotations/query_frame_annotations_val.csv")
dict_of_frames = {}

for rec in dict_of_frames:
    majority.append(majority_vote(dict_of_frames[rec]))
    average.append(average_rule(dict_of_frames[rec]))
    # print("{} scores: {}".format(rec, dict_of_frames[rec]))
    # print("{} scores: {}".format(rec, np.argmax(np.bincount(dict_of_frames[rec]))))