### 1. How to install dependency

```sh
# http://www.grpc.io/docs/tutorials/basic/python.html
pip install grpcio-tools
# https://cryptography.io/en/latest/fernet/
pip install cryptography
```

### 2. How to generate Python gRPC code from your .proto service definition.

```sh
python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. wallet.proto 
```

The above step will generates wallet_pb2.py and wallet_pb2_grpc.py files.

### 3. Implement all TODO sections.

### 4. How to run the Server

```sh
python server.py
```

Server startup output:
```sh
Server started at...3000
```

### 5. How to test

```sh
python -m test
```

_Expected Output_

```sh
# Listing files under the mid-term directory.
$ ls
README.md           server.py           wallet_pb2.py       wallet_pb2_grpc.pyc
client.py           test.py             wallet_pb2.pyc
client.pyc          wallet.proto        wallet_pb2_grpc.py

# Run the test
$ python -m test
########## Encryption ###########
Card detail: {'card_expiry_yyyymm': 201804, 'card_number': '4012888888881881', 'card_holder_name': 'Foo Bar'}
Encrypted token: "gAAAAABY5XdrIzSNyC3sMwMv9zGrGNPVwPz5z0dCNot4DgEhv98ZhieYOLA_8DOpfZgBcnDGW6wX5JiVOa1mpB0YdSFvh14jQaJkiknhuBe1rkTmtwdQyRz4E2OP3wARAOnWPVFkonXCE35cb4GzPrTHHScDDi9V5dVtPoPXs3zMQKizGiP-KQshjcjWoDxIS7CZ4toHlbRp"

.########## Decryption ###########
token=gAAAAABY5XdrIzSNyC3sMwMv9zGrGNPVwPz5z0dCNot4DgEhv98ZhieYOLA_8DOpfZgBcnDGW6wX5JiVOa1mpB0YdSFvh14jQaJkiknhuBe1rkTmtwdQyRz4E2OP3wARAOnWPVFkonXCE35cb4GzPrTHHScDDi9V5dVtPoPXs3zMQKizGiP-KQshjcjWoDxIS7CZ4toHlbRp

Decrypted card_in_plain_text: "card_holder_name: \"Foo Bar\"\ncard_number: \"4012888888881881\"\ncard_expiry_yyyymm: 201804\n"

.
----------------------------------------------------------------------
Ran 2 tests in 0.006s

OK
```
