import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import defs
from collections import defaultdict

def map_reduce(inputs,mapper,reducer):
    """A function that maps the task and reduces
    it to its outputs"""
    
    collector=defaultdict(list)  
    #map stage
    
    for input in inputs:
        for key, value in mapper(input):
            #pass each input to the mapper function and receive back each key,value pair
            collector[key].append(value)     
            
    #reduce stage - 1 reducer for each key
    
    outputs=[]
    for key,values in collector.items(): 
        for res in reducer(key,values):
            #take each pair yielded by the reducer and add it to the outputs list
            outputs.append(res)
    
    return outputs

def wc_mapper_len(document):
    """Mapper function
    :returns: a list of word lengths"""
    for word in document:
        yield(len(word),1)

def wc_mapper_freq(document):
    """Mapper function
    :returns: a list of word lengths"""
    for word in document:
        yield(word,1)
        
def wc_reducer(word,counts):
    """Reducer function
    :returns: a sum of the mapper function"""
    yield(word,sum(counts))

document1="timemachine.txt"
lines=[]

with open(document1) as instream:
    for line in instream:        
        tokens=[token.lower() for token in word_tokenize(line.rstrip())]  #strip excess white space, tokenize, lower-case
        lines.append(tokens)

word_len_results = map_reduce(lines,wc_mapper_len,wc_reducer)
xs, ys = zip(*word_len_results)
word_freq_results = map_reduce(lines,wc_mapper_freq,wc_reducer)

plt.scatter(xs,ys,label='Word length') 
plt.legend(loc='upper left')
plt.xlabel('Length of word')
plt.ylabel('Frequency')
plt.title('Frequency of word length in text')