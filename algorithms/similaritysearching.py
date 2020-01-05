import math
from pprint import pprint

from datapreprocessing.processingdata import cleaning_data,tokenizer

def VSM(query_token,tf_idf):
    vsm_list=[]
    for doc in tf_idf:
        doc_id=doc['doc_id']
        vsm={}
        for token in query_token:
            vsm[token]=0.00
            for key, value in doc['tf_idf'].items():
                if(key==token):
                    vsm[key] = value
        temp={'doc_id':doc_id,'vsm':vsm}
        vsm_list.append(temp)
    #pprint(vsm_list)
    query_vector={}
    for token in query_token:
        query_vector[token] = 1.00
    return query_vector,vsm_list

def dotproduct(v1,v2):
    #print('dgd')
    dot=0.0
    for key in v1.keys():
        dot+=v1[key]*v2[key]
    return dot
def vector_mod(v):
    mod=0.0
    for key in v.keys():
        mod+= math.pow(v[key],2)
    return math.sqrt(mod)

def cosine_similarity(query_vector,vsm):
    sim=[]
    for vector in vsm:
        Q_dot_D=dotproduct(query_vector,vector['vsm'])
        #print(Q_dot_D)
        Q=vector_mod(query_vector)
        #print(Q)
        D=vector_mod(vector['vsm'])
        #print(D)
        if(D>0.0):
            cos_theta=Q_dot_D/(Q*D)
        else:
            cos_theta=0.0
        temp={'doc_id':vector['doc_id'],'sim':cos_theta}
        #print(temp)
        sim.append(temp)
    return sim

def ranking(sim_dict):
    sortedlist = sorted(sim_dict, key=lambda k: k['sim'], reverse=True)
    #pprint(sortedlist)
    return sortedlist[:10]

def searching(query_input,tf_idf):
    query_clean=cleaning_data(query_input)
    query_token=tokenizer(query_clean)
    #print(query_token)
    query_vector,vsm=VSM(query_token,tf_idf)
    #pprint(vsm)
    pprint(query_vector)
    sim=cosine_similarity(query_vector,vsm)
    #pprint(sim)
    ranked_doc=ranking(sim)
    pprint(ranked_doc)
    return ranked_doc


