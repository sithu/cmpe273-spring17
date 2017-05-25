"""
################################## client.py #############################
# DBClient, a GRPC client, to communicate to the DB Service.
################################## client.py #############################
"""
import grpc
import db_pb2

class DBClient(object):
    
    def __init__(self, host='0.0.0.0', port=3000):
        _channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = db_pb2.DBStub(channel=_channel)
        print "Client connected to %s:%d" % (host, port)


    def info(self):
        return self.stub.info(db_pb2.Empty())


    def put(self, key, dataMap):
        _data = db_pb2.Data(entry=dataMap)
        req = db_pb2.PutRequest(id=key, data=_data)
        return self.stub.put(req)


    def get(self, key):
        req = db_pb2.GetRequest(id=key)
        return self.stub.get(req)
