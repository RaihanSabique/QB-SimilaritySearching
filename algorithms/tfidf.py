from datapreprocessing.processingdata import cleaning_data,tokenizer

def tf_idf(data_dict,query_mcq):
    print(len(data_dict))
    for key,values in data_dict.items():
        print(values)
        for value in values:
            clean_data=cleaning_data(value)
            print(clean_data)
            token=tokenizer(clean_data)
            print(token)

