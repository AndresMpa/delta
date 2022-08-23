# Usage

This basic software uses (XMLRPC)[https://docs.python.org/es/3/library/xmlrpc.html]
under version 3.10 of python to perform files sending trough a client
and its corresponding server, both of them written in python

## Server

Server contains 2 methods to handle "input.txt" file data
`get_file` and `__generate_file` which is a private method,
also `invert_file` and `count_file` allow interaction with
provided data to manage it.

To run it just follow Unix like basic usage for dirs (Something
similar on Windows I guess):

```
cd ./server/
python server.py
```

## Client

Client is a class which storage a main handler method call "main"
this one uses others some others private methods to create and read
data from users.

To run it just like in previous, using basic Unix like commands:

```
cd ./client/
python client.py
```

## Clean up

For Linux users there's a bash script to clean up residual data
(.txt files), just run `./clean` to remove it, actually it is
generated every time you run the code
