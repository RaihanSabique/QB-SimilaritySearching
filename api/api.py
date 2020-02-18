# -*- coding: utf-8 -*-
#happy_coding('~')
import json
from pprint import pprint

import os
import database.connectdb as db
import algorithms.tfidf as tfidf
from algorithms.similaritysearching import searching
import datapreparation.documentcreate as document_creation

from flask import Flask, jsonify, request, flash, render_template
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

import word2vector.model as model

question_weight=0.4
option_weight=0.6
answer_weight=0.8

#Train model
objectdb = db.dataReader()
data = objectdb.get_data()
print(len(data))
questions=model.get_scentences(data)
# pprint(questions)
model,saved_model_path=model.do_embedding(questions)
print ("Model Saved On: ",saved_model_path)
test_question=[]
for i in range(min(10,len(questions))):
    test_question.append(questions[i])
print(test_question)
# print('similarity')
# print(model.similarity('ধারণা','ফাংশন'))

#@app.route('/<string:folder_name>/<string:dpp_name>', methods=['POST','GET'])
@app.route('/',methods=['POST'])
def start():
    objectdb=db.dataReader
    Test=request.form['test']
    print(Test)

@app.route('/search',methods=['POST'])
def extraction():
    try:
        data=request.get_json(force=True)
        query_mcq = data['query_input']
        print(query_mcq)
        #tfidf.tf_idf(data)
        results=similarity_searching(query_mcq)
        return jsonify(results)

    except Exception as e:
        return '<p>error<p>'

def create_model():
    objectdb = db.dataReader()
    data = objectdb.get_data()
    #pprint(data)
    print('inside..')
    documents = document_creation.create_doc(data)
    #pprint(documents)
    freq_list = tfidf.create_freqDict_list(documents, question_weight, option_weight, answer_weight)
    tf = tfidf.computeTF(freq_list)
    # pprint(tf)
    idf = tfidf.computeIDF(documents, freq_list)
    # pprint(idf)
    tf_idf = tfidf.computeTFIDF(tf, idf)
    #pprint(tf_idf)
    return data,freq_list,tf_idf



def similarity_searching(query_mcq):
    raw_data,frequency_list,tf_idf=create_model()
    pprint(raw_data)
    #pprint(tf_idf)
    ranked_doc=searching(query_mcq,tf_idf)
    results=[]
    i=1
    for doc in ranked_doc:
        temp={'rank':i,'mcq_id':doc['doc_id'],'similarity':doc['sim'],'question':data[doc['doc_id']]}
        results.append(temp)
        i+=1
    return results

    #tfidf.tf_idf(data,query_mcq)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5555')

