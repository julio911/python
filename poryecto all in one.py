print("hola me llamo all in one y te puedo hacer lo siguiente")
print("a) calculadora")
print("b) invertir cualquier palabra")
print("c) darte un bono de acuerdo a tu sueldo")
print("d) darte un 30% de tu sueldo en forma de bono")
print("e) ingresar tu direccion y nombre y ver si tienes un bono")
print("f) mostrarte un porcentaje de azules y rojos")
print("g) ver el precio final de un producto ingresando un descuento")
print("--------------------------------------------------------------")
print("entonces ingresa la letra del proceso que quieres realizar: ")

opcion = input()

if(opcion == "a" or opcion == "A"):
    print("calculadora")
    num1 = float(input("ingrese num 1: "))
    num2 = float(input("ingrese num 2: "))

    print("app.principal")
    print("opciones: ")
    print("a) sumarlos")
    print("b) restarlos")
    print("c) dividir")
    print("d) multiplicar")

    opcion = input("ingrese opcion: ")

    if (opcion == "a" or opcion == "A"):
        suma = num1 + num2
        print("la suma es: ", suma)
    else:
        if (opcion == "b" or opcion == "B"):
            resta = num1 - num2
            print("la resta es: ", resta)
        else:
            if (opcion == "c" or opcion == "C"):
                dividir = num1 / num2
                print("la division es: ", dividir)
            else:
                if (opcion == "d" or opcion == "D"):
                    multiplicar = num1 * num2
                    print("la multiplicacion es: ", multiplicar)

elif (opcion == "b" or opcion == "B"):
    print("ingrese una frase: ")
    frase = input()

    var = ''
    for h in frase:
        var = h + var

    print(var)