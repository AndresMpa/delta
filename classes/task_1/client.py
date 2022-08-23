import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:3000')

print("***************** Menú Matemático *****************")
print("""\n

      a. Suma
      b. Restar
      c. Multiplicar
      d. Dividir
      e. Potencia
      f. Fibonacci

      """
      )


option = input('Escoja su opción: ')

if option == "a":
    result = server.add(
        int(input("Number 1: ")),
        int(input("Number 2: "))
    )
    print("Result is: ", result)
elif option == "b":
    result = server.rest(
        int(input("Number 1: ")),
        int(input("Number 2: "))
    )
    print("Result is: ", result)
elif option == "c":
    result = server.multiply(
        int(input("Number 1: ")),
        int(input("Number 2: "))
    )
    print("Result is: ", result)
elif option == "d":
    result = server.divide(
        int(input("Number 1: ")),
        int(input("Number 2: "))
    )
    print("Result is: ", result)
elif option == "e":
    result = server.power(
        int(input("Number 1: ")),
        int(input("Number 2: "))
    )
    print("Result is: ", result)
elif option == "f":
    result = server.fibonacci(
        int(input("Term: ")),
    )
    print("Result is: ", result)
else:
    print("Please, select a valid option")
