"""
################################## server.py ################################
# DB Server handles storing and retrieving any string type key-value pairs. #
################################## server.py ################################
"""
import time
import grpc
import db_pb2
import db_pb2_grpc
import uuid

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DBServicer(db_pb2.DBServicer):
    
    def __init__(self):
        self.map = {}


    def info(self, request, context):
        _entry = {
            "size": str(len(self.map))
        }
        return db_pb2.InfoResponse(data=db_pb2.Data(entry=_entry))


    def put(self, request, context):
        print "Saving data into the DB...\n", request.data
        key = uuid.uuid4().hex
        value = request.data
        self.map[key] = value
        return db_pb2.PutResponse(id=key)


    def get(self, request, context):
        print "Retrieving data from the DB, key=%s" % request.id
        return db_pb2.GetResponse(data=self.map[request.id])


def run(host, port):
    """Run a GRPC server instance."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    db_pb2_grpc.add_DBServicer_to_server(DBServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()
    print "Server started at...%d" % port
    return server

def forever(servers):
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        for server in servers:
            server.stop(0)


if __name__ == '__main__':
    forever([run('0.0.0.0', 3000)])
