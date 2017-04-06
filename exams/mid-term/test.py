'''
Test for Wallet encryption GRPC service.
'''
import unittest
from client import WalletClient

class WalletEncryptionTest(unittest.TestCase):
    token = None

    def test_1_encrypt(self):
        card = {
            'card_holder_name': 'Foo Bar',
            'card_number': '4012888888881881',
            'card_expiry_yyyymm': 201804
        }
        print "########## Encryption ###########"
        print "Card detail:", card
        client = WalletClient()
        resp = client.encrypt(card)
        print "Encrypted %s" % resp
        self.__class__.token = resp.token
        self.assertEqual(len(resp.token), 204)

    def test_2_decrypt(self):
        print "########## Decryption ###########"
        client = WalletClient()
        print "token=%s" % self.__class__.token
        resp = client.decrypt(self.__class__.token)
        print "\nDecrypted %s" % resp
        expected = ("card_holder_name: \"Foo Bar\"\n"
                    "card_number: \"4012888888881881\"\n"
                    "card_expiry_yyyymm: 201804\n")
        self.assertEqual(resp.card_in_plain_text, expected)

if __name__ == '__main__':
    unittest.main()
