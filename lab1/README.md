## Lab 1

### What is psutil?

psutil (python system and process utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network) in Python. 


### Requirements

* Use [psutil](https://pythonhosted.org/psutil/) and implement a network socket monitoring tool that can check how many TCP sockets are being created by a web application.
* Create a Python script called _socket-mon.py_.
* List all processes that have any socket connections (meaning the laddr and raddr fields exist).
* Group by the PID and sort the output by the number of the connections per process.

#### Expected Output in CSV format

```sh
$ python socket-mon.py (or $ sudo python socket-mon.py)
"pid","laddr","raddr","status"
"1234","10.0.0.1@48776","93.186.135.91@80","ESTABLISHED"
"1234","10.0.0.1@48777","93.186.135.91@80","ESTABLISHED"
"5678","10.0.0.1@48779","193.286.35.91@8000","CLOSING"
```

> In the above output, the PID 1234 has two active connection with _ESTABLISHED_ status and the 
other PID 5678 is closing one connection.

### How to run a simple http server and check its process id?

* Create index.html file with "Hello World" text.

```sh
$ echo "Hello World" > index.html
```

* Run a default Python HTTP Server inside the same directory that you created "index.html"

```sh
$ python -m SimpleHTTPServer
```

* By default, the SimpleHTTPServer will listen on port 8000. Check you can see the "Hello World" page.

```sh
$ curl -i http://localhost:8000/
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/2.7.13
Date: Wed, 08 Feb 2017 23:10:14 GMT
Content-type: text/html
Content-Length: 12
Last-Modified: Wed, 08 Feb 2017 23:03:11 GMT

Hello World
```

* Now, you can check PID of your Hello World web server.

```sh
$ ps 
  PID TTY           TIME CMD
 3853 ttys000    0:00.24 -bash
64140 ttys006    0:00.04 -bash
64391 ttys007    0:00.03 -bash
64837 ttys007    0:00.06 /{Depending_on_where_you_installed_python}/Python -m SimpleHTTPServer
```

__64837__ is the PID of the SimpleHTTPServer that you launched.

> You can also use [Apache Benchmarking tool](http://stackoverflow.com/questions/12732182/ab-load-testing) to generate multiple TCP/Http connections on the server.
