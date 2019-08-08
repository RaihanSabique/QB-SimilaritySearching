from cltk.tokenize.sentence import TokenizeSentence
import datapreprocessing.parser as parser
import datapreprocessing.stopword as stopword

stop=stopword.stopwords()
stemmer=parser.Stemmer()
from py_bangla_stemmer import BanglaStemmer
Stemmer = BanglaStemmer()
def clean(str):
    stop_free = " ".join([i for i in str if i not in stop])
    #punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    #normalized = " ".join(lemma.lemmatize(word) for word in stop_free.split())
    stemm_line=""
    for word in stop_free.split():
        try:
            stemm_line+=Stemmer.stem(word)+" "
        except:
            stemm_line+=stemmer.stem_word(word)+" "
    #print(stemm_line)
    y = stemm_line.split()
    #print(y)
    return y

def cleaning_data(str):
    tokenizer = TokenizeSentence('bengali')
    bengali_text_tokenize = tokenizer.tokenize(str)
    # print(bengali_text_tokenize)
    cleaned = clean(bengali_text_tokenize)
    cleaned = ' '.join(cleaned)
    return cleaned

def tokenizer(str):
    tokenizer = TokenizeSentence('bengali')
    bengali_text_tokenize = tokenizer.tokenize(str)
    return bengali_text_tokenize
