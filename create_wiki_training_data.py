# from gensim.models import Nmf
# import gensim.downloader as api
# from gensim.models import TfidfModel
# from gensim.corpora import Dictionary
# from gensim.test.utils import datapath
from mediawiki import MediaWiki

LIST_OF_PAGES = [
    # "Computer",
    # "Computer science",
    # "Computer programming",
    # "Computer hardware",
    # "Computer software",
    # "Computer network",
    # "Computer virus",
    # "Computer mouse",
    # "Computer keyboard",
    # "Computer monitor",
    # "New york city",
    # "Statue of liberty",
    # "Central park",
    # "Empire state building",
    # "Times square",
    # "Brooklyn bridge",
    # "Grand central terminal",
    # "Rockefeller center",
    # "Chrysler building",
    # "Programming lanuage",
    # "Graphics processing unit",
    # "Computer graphics",
    # "Computer vision",
    # "Machine learning",
    # "Artificial intelligence",
    # "Data science",
    # "Data mining",
    # "Data engineering",
    # "Data analysis",
    # "Data visualization",
    # "Data warehouse",
    # "Data lake",
    "Computer architecture",
    "Computer engineering",
    "Computer security",
    "Control unit",
    "Computer memory",
    "Computer processor",
    "Computer motherboard",
    "Computer bus",
    "Cracking (software)",
    "Cryptography",
    "Finite state automaton",
    "Hacker (computer security)",
    "Human-computer interaction",
    "Kilobyte",
    "Multiprocessing",
    "Operating system",
    "Scripting language",
    "Virtual memory",
    "World wide web"
]
wikipedia = MediaWiki()

# for every page in LIST_OF_PAGES write the summary to a file
for page_name in LIST_OF_PAGES:
  page = wikipedia.page(page_name)
  # Change set before running!
  with open(f'./training-data/set-2/{page_name}.txt', 'w') as f:
    for category in page.categories:
      f.write(category + "~")
    f.write("\n||||||\n")
    f.write(f'{page.title}\n')
    f.write("||||||\n")
    f.write(page.summary)
