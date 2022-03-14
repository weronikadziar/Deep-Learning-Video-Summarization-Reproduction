import numpy as np
import torch

def query_embedding(box_train_query, word2index, max_length):
    one_hot_x = encode_queries_index(box_train_query, word2index)

    one_hot_x_same_length = []
    for query in one_hot_x:
        if len(query) < max_length:
            query = [*query, *np.zeros(max_length -len(query))]
        else:
            query = query[:max_length]
            
        one_hot_x_same_length.append(query)
        
    return torch.Tensor(one_hot_x_same_length) # return a stack of tensors.

def encode_queries_index(box_train_query, word2index):
    encoded_titles = []
    for title in box_train_query:
        title_words = []
        for word in title.split(" "):
            title_words.append(word2index.index(word))
        encoded_titles.append(title_words)
        
    return encoded_titles