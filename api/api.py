# -*- coding: utf-8 -*-
#happy_coding('~')
import json
from pprint import pprint

import os
import database.connectdb as db
import algorithms.tfidf as tfidf

from flask import Flask, jsonify, request, flash, render_template
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

import word2vector.model as model
#Train model
objectdb = db.dataReader()
data = objectdb.get_data()
questions=model.get_scentences(data)
pprint(questions)
model,saved_model_path=model.do_embedding(questions)
print ("Model Saved On: ",saved_model_path)
test_question=[]
for i in range(min(10,len(questions))):
    test_question.append(questions[i])
print(test_question)


#@app.route('/<string:folder_name>/<string:dpp_name>', methods=['POST','GET'])
@app.route('/',methods=['POST'])
def start():
    objectdb=db.dataReader
    Test=request.form['test']
    print(Test)

@app.route('/qbsss',methods=['POST'])
def extraction():
    try:
        data=request.get_json(force=True)
        query_mcq = data['query']
        print(query_mcq)
        #tfidf.tf_idf(data)
        similarity_searching(query_mcq)
        return "hell0"

    except Exception as e:
        return '<p>error<p>'

def similarity_searching(query_mcq):
    objectdb = db.dataReader()
    data = objectdb.get_data()
    print('inside..')
    tfidf.tf_idf(data,query_mcq)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5555')

