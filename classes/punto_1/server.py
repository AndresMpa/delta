from xmlrpc.server import SimpleXMLRPCServer


class Calculator:
    def add(self, a, b):
        return int(a) + int(b)

    def rest(self, a, b):
        return int(a) - int(b)

    def multiply(self, a, b):
        return int(a) * int(b)

    def divide(self, a, b):
        return int(a) / int(b)

    def power(self, a, b):
        return int(a) ** int(b)

    def fibonacci(self, terms):
        fibonacci_serie = []
        n1, n2 = 0, 1
        count = 0
        if terms <= 0:
            print("Please enter a positive integer")
        elif terms == 1:
            print("Fibonacci sequence upto", terms, ":")
            print(n1)
        else:
            print("Fibonacci sequence:")

            while count < terms:
                fibonacci_serie.append.append(n1)
                nth = n1 + n2

                n1 = n2
                n2 = nth
                count += 1

        return n1


port = 3000

server = SimpleXMLRPCServer(("localhost", port))

server.register_instance(Calculator())

print("Server is running on port " + str(port))

server.serve_forever()
