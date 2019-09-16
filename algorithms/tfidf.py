import math
from pprint import pprint

from datapreprocessing.processingdata import cleaning_data, tokenizer


def word_count(str):
    tokens = tokenizer(str)
    # print(tokens)
    return len(tokens)


def create_freqDict_list(doc_info_list, w1, w2, w3):
    freq_dict_list = []
    for doc in doc_info_list:
        # pprint(doc)
        freq_dict = {}
        weight_dict = {}
        question_tokens = tokenizer(doc['question'])
        option_tokens = tokenizer(doc['option'])
        answer_tokens = tokenizer(doc['answer'])
        for token in answer_tokens:
            if token in freq_dict:
                freq_dict[token] += 1
            else:
                weight_dict[token] = w3
                freq_dict[token] = 1
        for token in option_tokens:
            if token in freq_dict:
                freq_dict[token] += 1
            else:
                weight_dict[token] = w2
                freq_dict[token] = 1
        for token in question_tokens:
            if token in freq_dict:
                freq_dict[token] += 1
            else:
                weight_dict[token] = w1
                freq_dict[token] = 1

        temp = {'doc_id': doc['doc_id'], 'freq_list': freq_dict, 'weight_list': weight_dict, 'count': doc['count']}
        # pprint(temp)
        freq_dict_list.append(temp)
    # pprint(freq_dict_list)
    return freq_dict_list


def computeTF(freq_dict_list):
    TF_scores = []
    for tempDict in freq_dict_list:
        doc_id = tempDict['doc_id']
        count = tempDict['count']
        tf_score = {}
        for key, value in tempDict['freq_list'].items():
            tf_score[key] = value / count
        temp = {'doc_id': doc_id, 'tf_score': tf_score}
        TF_scores.append(temp)
    return TF_scores


def computeIDF(doc_info, freq_dict_list):
    IDF_scores = []
    for temp in freq_dict_list:
        doc_id = temp['doc_id']
        idf_score = {}
        counter = 0
        for k in temp['freq_list'].keys():
            counter = sum([k in tempDict['freq_list'] for tempDict in freq_dict_list])
            idf_score[k] = math.log(len(doc_info) / counter)
        temp = {'doc_id': doc_id, 'idf_score': idf_score}
        IDF_scores.append(temp)
    return IDF_scores


def computeTFIDF(tf_scores, idf_scores):
    print('TF-IDF')
    TFIDF_scores = []
    for i in range(len(idf_scores)):
        print('dhd')
        tf_idf = {}
        for tfkey, tfvalue in tf_scores[i]['tf_score'].items():
            for idfkey, idfvalue in idf_scores[i]['idf_score'].items():
                print(tfkey, tfvalue)
                if (tfkey == idfkey):
                    tf_idf[tfkey] = tfvalue * idfvalue
        temp = {'doc_id': tf_scores[i]['doc_id'], 'tf_idf': tf_idf}
        TFIDF_scores.append(temp)
    return TFIDF_scores
