# from gensim.models import Nmf
# import gensim.downloader as api
# from gensim.models import TfidfModel
# from gensim.corpora import Dictionary
# from gensim.test.utils import datapath
from mediawiki import MediaWiki
import time


NUM_TOPICS = 2

# LIST_OF_PAGES = [
#     "Computer",
#     "Computer science",
#     "Computer programming",
#     "Computer hardware",
#     "Computer software",
#     "Computer network",
#     "Computer virus",
#     "Computer mouse",
#     "Computer keyboard",
#     "Computer monitor",
#     "New york city",
#     "Statue of liberty",
#     "Central park",
#     "Empire state building",
#     "Times square",
#     "Brooklyn bridge",
#     "Grand central terminal",
#     "Rockefeller center",
#     "Chrysler building",
# ]
wikipedia = MediaWiki()


# ['Computers', 'Consumer electronics', 'Electronics industry']

# for page_name in LIST_OF_PAGES:
#   page = wikipedia.page(page_name)
#   time.sleep(0.20)
#   print(page.title)
#   print(page.summary)


# for every page in LIST_OF_PAGES write the summary to a file
for page_name in LIST_OF_PAGES:
  page = wikipedia.page(page_name)
  with open(f'./training-data/set-2/{page_name}.txt', 'w') as f:
    for category in page.categories:
      f.write(category + "~")
    f.write("\n||||||\n")
    f.write(f'{page.title}\n')
    f.write("||||||\n")
    f.write(page.summary)


# p = wikipedia.page('Chess')
# p.title
# p.summary
# p.categories
# p.images
# p.links
# p.langlinks
# p.content

# wikipedia.random(pages=3)
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
