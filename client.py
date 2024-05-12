import Pyro5.api

nameserver = Pyro5.api.locate_ns()
uri = nameserver.lookup("Calculadora")

calculadora = Pyro5.api.Proxy(uri)

while True:
    print("Menu:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    option = input("Seleccione una opcion: ")
    if option == "5":
        break
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    
    if option == "1":
        result = calculadora.sumar(num1, num2)
        print("El resultado es:", result)
    elif option == "2":
        result = calculadora.restar(num1, num2)
        print("El resultado es:", result)
    elif option == "3":
        result = calculadora.multiplicar(num1, num2)
        print("El resultado es:", result)
    elif option == "4":
        result = calculadora.dividir(num1, num2)
        print("El resultado es:", result)
    else:
        print("Opcion invalida. Por favor seleccione una opcion valida.")