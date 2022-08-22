from sys import exit
import xmlrpc.client


class Client:
    data = []
    server = xmlrpc.client.ServerProxy('http://localhost:8000',
                                       verbose=False,
                                       allow_none=True,
                                       use_builtin_types=True,
                                       headers=[
                                           ('Content-Type', 'application/zip')
                                       ])

    def __init__(self, inputs=15) -> None:
        counter = 0
        while counter < inputs:
            self.data.append(int(input("Type some data: ")))
            counter += 1

    def __create_file(self, file, data) -> None:
        with open(file, "wb") as handle:
            handle.write(bytearray(data))

    def __read_data(self, file):
        with open(file, "rb") as handle:
            return xmlrpc.client.Binary(handle.read())

    def main(self) -> None:
        print("******* Punto 2 *******")
        self.__create_file("file.txt", self.data)
        file_data = self.__read_data("./file.txt")
        self.server.get_file(file_data)

        print('''
        Type 1 to invert data from a file
        Type 2 to get more repeated data in a file
        ''')
        option = int(input("Type an option: "))
        if (option == 1):
            self.__create_file("file.txt", self.server.invert_file())
            response = self.__read_data("./file.txt")
            print(
                f"Data in file.txt updated to its reversed version: {list(response.data)}")
        elif (option == 2):
            target = input("Search term: ")
            response = self.server.count_file(target)
            print(f"There are {response} coincidences with {target}")

        else:
            print("That's no a valid option")


if __name__ == "__main__":
    try:
        client = Client()
        client.main()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        exit(0)
