"""
Check whether DB server is up and a client can access to it.
"""
import sys
from client import DBClient

class DBCheck(object):

    def __init__(self, port):
        self.port = port
        self.client = DBClient(host='0.0.0.0', port=self.port)


    def put(self):
        print "########## Put ###########"
        user = {
            'name': 'Foo Bar - 1',
            'email': 'foobar-1@gmail.com'
        }
        key = 'foobar-1@gmail.com'
        print "Put Request:\n", key, user
        resp = self.client.put(key, user)
        print "Put Response:\n%s" % resp
        return resp.id
        

    def get(self, id=None):
        print "########## Get ###########"
        resp = self.client.get(id)
        print "Get Response:\n%s" % resp


    def info(self):
        print "########## Info ###########"
        resp = self.client.info()
        print "Info Response:\n%s" %resp
        

if __name__ == '__main__':
    total = len(sys.argv)
    if total < 2:
        print "Usage: python %s {SERVER_PORT}" % __file__
        sys.exit(0)

    port = int(sys.argv[1])
    db = DBCheck(port)
    id = db.put()
    db.get(id)
    db.info()