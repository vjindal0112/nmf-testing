from gensim.models import Nmf
import gensim.downloader as api
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from gensim.test.utils import datapath
import wikipedia

NUM_TOPICS = 2

LIST_OF_PAGES = [
    "Computer",
    "Computer science",
    "Computer programming",
    "Computer hardware",
    "Computer software",
    "Computer network",
    "Computer virus",
    "Computer mouse",
    "Computer keyboard",
    "Computer monitor",
    "New york city",
    "Statue of liberty",
    "Central park",
    "Empire state building",
    "Times square",
    "Brooklyn bridge",
    "Grand central terminal",
    "Rockefeller center",
    "Chrysler building",
]

for page in LIST_OF_PAGES:
  print(page)
  print(wikipedia.summary(page))
  print()


# texts = [['human', 'interface', 'computer']]
# dct = Dictionary(texts)  # initialize a Dictionary
# # add more document (extend the vocabulary)
# dct.add_documents([["cat", "say", "meow"], ["dog"]])
# train_set = ["dog", "cat", "bark"], ["human", "interface",
#                                      "computer", "design"], ["bark", "dog", "says"]
# corpus = [dct.doc2bow(doc) for doc in train_set]
# nmf = Nmf(corpus, num_topics=NUM_TOPICS, id2word=dct)

# print("ID TO WORD")
# for x in nmf.id2word.iteritems():
#   print(x)

# # print("TOPICS")
# # for x in nmf.show_topics():
# #   print(x)

# print()
# print("TOPIC TERMS")
# for x in range(NUM_TOPICS):
#   print(f'TOPIC {x}')
#   for term in nmf.show_topic(x, topn=4):
#     print(term)
#   print()
