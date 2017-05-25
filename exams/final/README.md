### 1. Install dependency

```sh
virtualenv exam-venv

source exam-venv/bin/activate

pip install -r requirements.txt
```

> Want to read more about [gRPC lib](http://www.grpc.io/docs/tutorials/basic/python.html)?

### 2. Generate Python gRPC binding code from a service definition .proto file.

* Look at the service interface definition [db.proto](https://github.com/sithu/cmpe273-spring17/blob/master/exams/final/db.proto) file to understand the input and output parameters and payloads.

> DO NOT CHANGE db.proto FILE OR YOU WILL GET ZERO!

```sh
python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. db.proto 
```


### 3. Run the Server

> You need to run three GRPC server instances using 3000-3002 ports as the test (RendezvousHashDBClientTest) needs to connect to all three servers.

```sh
python server.py 3000 3001 3002
```

### 4. Run the pre-req check (Optional)

```sh
python check_pre_req.py 3000
```

_Expected Output_

```sh
Client connected to 0.0.0.0:3000
########## Put ###########
Put Request:
foobar-1@gmail.com {'name': 'Foo Bar - 1', 'email': 'foobar-1@gmail.com'}
Put Response:
id: "foobar-1@gmail.com"

########## Get ###########
Get Response:
data {
  entry {
    key: "email"
    value: "foobar-1@gmail.com"
  }
  entry {
    key: "name"
    value: "Foo Bar - 1"
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

### 5. Implement all TODO sections in rendezvous.py and you don't need to change other files. Finally, test your solution.

* Run this test to validate your solution.

```sh
python -m test
```

__Expected Output__

```sh
Client connected to 0.0.0.0:3000
Client connected to 0.0.0.0:3001
Client connected to 0.0.0.0:3002
################### PUT Test ###################
1 - PUT Response=id: "foobar-1@gmail.com"

2 - PUT Response=id: "foobar-2@gmail.com"

3 - PUT Response=id: "foobar-3@gmail.com"

4 - PUT Response=id: "foobar-4@gmail.com"

5 - PUT Response=id: "foobar-5@gmail.com"

6 - PUT Response=id: "foobar-6@gmail.com"

7 - PUT Response=id: "foobar-7@gmail.com"

8 - PUT Response=id: "foobar-8@gmail.com"

9 - PUT Response=id: "foobar-9@gmail.com"

10 - PUT Response=id: "foobar-10@gmail.com"

.################### GET Test ###################
{u'name': u'Foo bar - 1', u'email': u'foobar-1@gmail.com'}
{u'name': u'Foo bar - 2', u'email': u'foobar-2@gmail.com'}
{u'name': u'Foo bar - 3', u'email': u'foobar-3@gmail.com'}
{u'name': u'Foo bar - 4', u'email': u'foobar-4@gmail.com'}
{u'name': u'Foo bar - 5', u'email': u'foobar-5@gmail.com'}
{u'name': u'Foo bar - 6', u'email': u'foobar-6@gmail.com'}
{u'name': u'Foo bar - 7', u'email': u'foobar-7@gmail.com'}
{u'name': u'Foo bar - 8', u'email': u'foobar-8@gmail.com'}
{u'name': u'Foo bar - 9', u'email': u'foobar-9@gmail.com'}
{u'name': u'Foo bar - 10', u'email': u'foobar-10@gmail.com'}
.################### Info Test ###################
Server#1's info response:
data {
  entry {
    key: "size"
    value: "2"
  }
}

Server#2's info response:
data {
  entry {
    key: "size"
    value: "5"
  }
}

Server#3's info response:
data {
  entry {
    key: "size"
    value: "3"
  }
}

Total number of entries across all servers=10
.
----------------------------------------------------------------------
Ran 3 tests in 0.032s

OK
```


