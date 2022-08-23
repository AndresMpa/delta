from xmlrpc.server import SimpleXMLRPCServer
from sys import exit


class AccessManager:
    def get_datastore(self):
        store = []
        with open("store.txt", "r") as handle:
            store = handle.readlines()
        store = [data[0:-1:1] for data in store]
        return [tuple(map(str, data.split(', '))) for data in store]

    def log_user(self, data):
        if tuple(data) in self.get_datastore():
            return True
        else:
            return False


access_port = 3000

server = SimpleXMLRPCServer(("localhost", access_port), allow_none=True)
server.register_introspection_functions()
server.register_instance(AccessManager())


def start_server():
    print("Server is running on port " + str(access_port))
    server.serve_forever()


try:
    start_server()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, exiting.")
    exit(0)
