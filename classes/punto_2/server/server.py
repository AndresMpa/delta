from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
import sys


class FileManager:
    # It creates a new file using the gotten data
    def __generate_file(self):
        with open("input.txt", "rb") as handle:
            return handle.read()

    # It get the file data to parser info
    def get_file(self, file_data):
        with open("input.txt", "wb") as handle:
            handle.write(file_data.data)

    # Invert file data

    def invert_file(self):
        file_data = list(self.__generate_file())
        file_data.reverse()

        new_file_data = Binary(bytearray(file_data))
        self.get_file(new_file_data)

        return self.__generate_file()

    # Return number of coincidences
    def count_file(self, target):
        file_data = list(str(self.__generate_file()))
        response = file_data.count(target)
        return response


port = 8000

server = SimpleXMLRPCServer(("localhost", port), allow_none=True)

server.register_instance(FileManager())

print("Server is running on port " + str(port))

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, exiting.")
    sys.exit(0)
