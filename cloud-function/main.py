from gensim.models import Nmf
from gensim.corpora import Dictionary
from google.cloud import storage
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer


def load_and_use_model(request):
  """Responds to any HTTP request.
  Args:
      request (flask.Request): HTTP request object.
  Returns:
      The response text or any set of values that can be turned into a
      Response object using
      `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
  """
  request_json = request.get_json()
  print(request_json)
  print(request.args)
  if 'note_text' in request_json:
    # Instantiates a client
    storage_client = storage.Client()

    # The name for the new bucket
    bucket_name = "nlp-model-store"
    bucket = storage_client.get_bucket(bucket_name)
    model_blob = bucket.blob("model")
    dct_blob = bucket.blob("dictionary")
    with open('./tmp/model', 'wb') as f:
      model_blob.download_to_file(f)
    with open('./tmp/dictionary', 'wb') as f:
      dct_blob.download_to_file(f)
    nmf = Nmf.load("./tmp/model")
    dct = Dictionary.load("./tmp/dictionary")
    print("ID TO WORD")
    for x in nmf.id2word.iteritems():
      print(x)
    doc = dct.doc2bow(clean_text(request_json['note_text']))
    prediction = nmf[doc]
    print(prediction)
    for x in prediction:
      print(x)
    return "works"

  return "Didn't work"


def remove_all_symbols(text: str) -> str:
  text = re.sub("http[s]?\://\S+", "", text)  # remove urls
  text = re.sub(r"[0-9]", "", text)  # remove numbers
  text = re.sub(r"\n", " ", text)  # remove newlines
  text = re.sub('\s+', ' ', text)  # remove extra spaces
  text = re.sub("[^a-zA-Z ]+", " ", text)  # remove all punctuation
  return text


def clean_text(text_str: str) -> list:
  STOPWORDS = set(stopwords.words('english'))
  STOPWORDS.add("also")
  STOPWORDS.add("however")
  STOPWORDS.add("in")
  STOPWORDS.add("depends")
  STOPWORDS.add("depend")
  STOPWORDS.add("")
  STOPWORDS.add("wa")

  text_str = remove_all_symbols(text_str)
  words = text_str.split(" ")
  # words = simple_preprocess(text_str)
  # words = word_tokenize(text_str)

  lemmmatizer = WordNetLemmatizer()
  words = [lemmmatizer.lemmatize(word.lower()) for word in words]

  # remove all words that are in STOPWORDS from words
  words = [w for w in words if not w in STOPWORDS]
  return words
