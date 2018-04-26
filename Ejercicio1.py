#autor: julio
#fecha: 03/04/2018

num1 = float(input("ingrese num 1: "))
num2 = float(input("ingrese num 2: "))



print("app.principal")
print("opciones: ")
print("a) sumarlos")
print("b) restarlos")
print("c) dividir")
print("d) multiplicar")

opcion = input("ingrese opcion: ")

if(opcion == "a" or opcion == "A"):
    suma = num1 + num2
    print("la suma es: ", suma)
else:
    if(opcion == "b" or opcion == "B"):
        resta = num1 - num2
        print("la resta es: ", resta)
    else:
        if(opcion == "c" or opcion == "C"):
            dividir = num1 / num2
            print("la division es: ", dividir)
        else:
            if(opcion == "d" or opcion == "D"):
                multiplicar = num1 * num2
                print("la multiplicacion es: ",multiplicar)


