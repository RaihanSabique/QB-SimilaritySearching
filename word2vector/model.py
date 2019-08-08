#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,codecs
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from bijoy2unicode import converter
test = converter.Unicode()

model_path="../word2vector" # all files path [ folder name]
save_model_path="../savemodel" # where i save model


def chomps(s):
    return s.rstrip('\n')

def get_unicode(input):
    input=chomps(input)
    #print(input)
    #print(type(input))
    t=type(input)
    #print(ord(input[0]))
    #s=input.encode('ascii', 'replace')
    #print(type(s))
    #toUnicode = test.convertBijoyToUnicode(input)
    #print(toUnicode)
    if (t=="<class 'str'>"):
        #print('h')
        input =  input.decode('utf-8')
        #print(input)
        return input
    else:
        #print(input)
        return input


from datapreprocessing.processingdata import cleaning_data,tokenizer
def get_scentences(data_dict):
    scentences=[]
    for key,values in data_dict.items():
        #print(values)
        content=''
        for value in values:
            clean_data=cleaning_data(value)
            #print(clean_data)
            content += clean_data + ' '
        lines_token=tokenizer(content)
        scentences.append(lines_token)
    return scentences


def do_embedding(sentences):
    print ('----[start embedding on data corpus ]---')
    # word2vec parameters
    min_count=1 # word frequency grater or equal 'min_count' can be embedded
    size=100 # word vector size.simply known as 'embedding size'
    workers=4
    window = 4 # contexual window

    # a memory-friendly iterator
    print(sentences)
    model = gensim.models.Word2Vec(sentences,
        min_count=min_count,
        size=size,
        workers=workers,
        window=window
    )
    save_p=save_model_path+'/model_word2vec'
    model.save(save_p)
    return model,save_p

def read_file_for_test(path):
    sentences=[]
    with open(path,'r') as r:
        for x in r.readlines():
            words=[y for y in x.split()]
            words=[get_unicode(y) for y in words]
            sentences.append(words)
    return sentences

def output_test(model,path):
    print ("<>"*34)
    words=read_file_for_test(path)
    # print first 2 words embedding-vector
    for i in range(min(5,len(words))):
        print(words[i][0])
        print ("Words: ",words[i][0]," em-vec: ",model[words[i][0]])
        pass

    # print first 10 words embedding vectors similarity
    print ("*"*80)
    for i in range(min(10,len(words))):
        a=words[i][0]
        b=words[i+1][0]
        print(a,b)
        sim_vec=model.similarity(a,b)
        print ("words-sim-vec: ",sim_vec)

def main():
    model,saved_model_path=do_embedding(bd_corpus_path)
    print ("Model Saved On: ",saved_model_path)
    output_test(model,test_path)

