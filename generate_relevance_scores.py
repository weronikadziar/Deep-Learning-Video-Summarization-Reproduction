from csv import reader
from wsgiref import headers
import pandas as pd
import numpy as np
from pyparsing import dict_of
from collections import Counter

dataset = 'val'
df =pd.read_csv("./dataset/annotations/query_frame_annotations_val.csv")
dict_of_frames = {}

def majority_vote(arr):
    c = Counter(arr)
    if len(c) >= 2:
        if c.most_common(len(c))[0][1] > c.most_common(len(c))[1][1]:
            return c.most_common(len(c))[0][0]
        else:
            if c.most_common(len(c))[2][0] > c.most_common(len(c))[0][0]:
                return c.most_common(len(c))[0][0]
            else:
                return c.most_common(len(c))[1][0]
    else:
        return c.most_common(len(c))[0][0]

def average_rule(arr):
    return int(sum(arr) / len(arr))

def save_to_file(a, file_name):
    f = open("{}.csv".format(file_name), "a")
    for word in a:
        f.write("{}\n".format(word))
    f.close()

for i, row in df.iterrows():
    if row['imageURL'] in dict_of_frames:
        dict_of_frames[row['imageURL']].append(row['Relevance'])
    else:
        dict_of_frames[row['imageURL']] = [row['Relevance']]

majority = []
average = []
for rec in dict_of_frames:
    majority.append(majority_vote(dict_of_frames[rec]))
    average.append(average_rule(dict_of_frames[rec]))
    # print("{} scores: {}".format(rec, dict_of_frames[rec]))
    # print("{} scores: {}".format(rec, np.argmax(np.bincount(dict_of_frames[rec]))))

save_to_file(majority, 'majority_vote_{}'.format(dataset))
save_to_file(average, 'average_vote_{}'.format(dataset))