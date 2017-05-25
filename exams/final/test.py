"""
NOTE: Your implementation will be graded using this script.
So, do not change the class and method names from the baseline code.

Test RendezvousHashDBClient client-side sharding.
"""
import unittest
from rendezvous import RendezvousHashDBClient 

class RendezvousHashDBClientTest(unittest.TestCase):
    hashClients = RendezvousHashDBClient(['0.0.0.0:3000', '0.0.0.0:3001', '0.0.0.0:3002'])
    max = 11

    def test_1_put(self):
        print "################### PUT Test ###################"
        for i in range(1, self.__class__.max):
            key = 'foobar-%d@gmail.com' % i
            user = {
                'name': 'Foo bar - %d' % i,
                'email': key
            }
            resp = self.__class__.hashClients.put(key, user)
            print "%d - PUT Response=%s" % (i, resp)
            self.assertEqual(key, resp.id)
        

    def test_2_get(self):
        print "################### GET Test ###################"
        for i in range(1, self.__class__.max):
            key = 'foobar-%d@gmail.com' % i
            expected_user = {
                'name': 'Foo bar - %d' % i,
                'email': key
            }
            resp = self.__class__.hashClients.get(key)
            print resp.data.entry
            self.assertEqual(expected_user, resp.data.entry)

    
    def test_3_info(self):
        print "################### Info Test ###################"
        resp = self.__class__.hashClients.info()
        total = 0
        count = 0
        for server in resp:
            count += 1
            print "Server#%d's info response:\n%s" % (count, server)
            total += int(server.data.entry['size'])

        print "Total number of entries across all servers=%d" % total
        self.assertTrue(total >= self.__class__.max - 1)


if __name__ == '__main__':
    unittest.main()
