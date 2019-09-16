from pprint import pprint

from datapreprocessing import processingdata

def word_count(str):
    tokens=processingdata.tokenizer(str)
    #print(tokens)
    return len(tokens)

def create_doc(data):
    print('sadhgsad')
    documents=[]
    for key,values in data.items():
        #print(values)
        doc_dict={'doc_id':'','question':'','option':'','answer':'','count':0}
        doc_dict['doc_id']=key
        option=''
        for i in range(len(values)):
            #print(values[i])
            if(i==0):
                #print(values[i])
                doc_dict['question']=processingdata.cleaning_data(values[i])
            elif(i==len(values)-1):
                #print(values[i])
                doc_dict['answer'] = processingdata.cleaning_data(values[i])
            else:
                #print(values[i])
                doc_dict['option']+=processingdata.cleaning_data(values[i]) + ' '

        doc_dict['count']=word_count(doc_dict['question'])+word_count(doc_dict['answer'])+word_count(doc_dict['option'])
        #print(doc_dict)
        documents.append(doc_dict)
    #pprint(documents)
    return documents