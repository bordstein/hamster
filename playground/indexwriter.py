from multiprocessing.managers import BaseManager
from whoosh_action.index import HamsterIndex
import u1db
import json

def index(movie):
    try:
        db = u1db.open("/tmp/out.db", create=True)
        h_index.index_movie(movie)
        db.create_doc(json.dumps(movie), doc_id=movie["_id"])
        print "indexed and stored:", movie['title']
    except Exception as e:
        print "failed"
        print e

class QueueManager(BaseManager):
    pass

if __name__ == "__main__":

    h_index = HamsterIndex("/tmp/hamster.idx")

    QueueManager.register('index', callable=index)
    m = QueueManager(address=('', 50000), authkey='abracadabra')
    s = m.get_server()
    s.serve_forever()

    
