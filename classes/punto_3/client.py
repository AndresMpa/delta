from util.index import greeter, conection_accepted, refuse_connection
from files.client.client import run
from sys import exit
import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:3000')


def main():
    userdata = greeter()
    log_status = server.log_user(userdata)
    if log_status:
        conection_accepted()
        run()
    else:
        refuse_connection()
        exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        exit(0)
