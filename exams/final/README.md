### 1. Install dependency

```sh
virtualenv exam-venv

source exam-venv/bin/activate

# http://www.grpc.io/docs/tutorials/basic/python.html
pip install -r requirements.txt
```

### 2. Generate Python gRPC binding code from a service definition .proto file.

```sh
python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. db.proto 
```

Check the generated code

```sh
$ ls
README.md        db.proto         exam-venv
check_pre_req.py db_pb2.py        requirements.txt
client.py        db_pb2_grpc.py   server.py
```

### 3. Run the Server

```sh
python server.py
```

### 4. Run the pre-req check

```sh
python check_pre_req.py 3000
```

_Expected Output_

```sh
Client connected to 0.0.0.0:3000
########## Put ###########
Put Request:
{'name': 'Foo Bar', 'email': 'foo_bar@gmail.com'}
Put Response:
id: "6a6d3a1837a448069a85604de456618d"

########## Get ###########
Get Response:
data {
  entry {
    key: "email"
    value: "foo_bar@gmail.com"
  }
  entry {
    key: "name"
    value: "Foo Bar"
  }
}

########## Info ###########
Info Response:
data {
  entry {
    key: "size"
    value: "1"
  }
}
```
