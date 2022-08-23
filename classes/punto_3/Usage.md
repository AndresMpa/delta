# Usage

This basic software uses (XMLRPC)[https://docs.python.org/es/3/library/xmlrpc.html]
under version 3.10 of python to perform a log in process sending raw data to a server
and its answer allow client to redirect user to another server or not, each one of them
written in python

## Client

Main client at ./ directory contains necessary functions to send log data, also some
invocations to graphic utilities to let users know if login process was successful or not,
to run it just use python:

```
python ./client.py
```

## Server

Main server contains what is necessary to handle log in process on server side, also this server
allow or not client to redirect users, to run it, just like in previous:

```
pytyhon ./server.py
```

> Note: Available users an password are storage at ./store.txt under structure <user, password>

## file.server

This is a secondary server, quite similar to what you should saw at "point_2", it's necessary to
run it before to send request as a logged user, so; to make it possible just change to its directory
them run it like this:

```
cd ./files/server/
python ./server.py
```

### Disclaimer

Every instruction up there should be run in a different terminal
