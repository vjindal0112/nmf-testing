from gensim.models import Nmf
from google.cloud import storage

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
      blob = bucket.blob("model")
      with open('./tmp/model', 'wb') as f:
        blob.download_to_file(f)
      nmf = Nmf.load("./tmp/model")
      print("ID TO WORD")
      for x in nmf.id2word.iteritems():
        print(x)
      return "works"

    return "Didn't work"
