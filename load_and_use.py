from gensim.models import Nmf
import gensim.downloader as api
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from gensim.test.utils import datapath

dataset = api.load("text8")

dct = Dictionary(dataset)  # fit dictionary

temp_file = datapath("model")
nmf = Nmf.load(temp_file)

other_texts = [
    ['computer', 'time', 'graph'],
    ['survey', 'response', 'eps'],
    ['human', 'system', 'computer']
]
other_corpus = [dct.doc2bow(text) for text in other_texts]

unseen_doc = other_corpus[0]
vector = nmf[unseen_doc]
print(vector)
for identity, stat in vector:
    print(f"{dct[identity]}: {stat}")
