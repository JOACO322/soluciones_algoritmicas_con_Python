def imprimir_menu():
    print("Programa:")
    print("1. Contar número de ocurrencias de letras")
    print("2. Sabes si un número es negativo o positivo")
    print("3. Sacar sumatoria y promedio")
    print("4. Suma te todos los dígitos de un número")
    print("5. Salir")


def obtener_opcion():
    opcion = input("Ingrese una opción: ")
    while opcion not in ["1", "2", "3", "4", "5"]:
        opcion = input("Opción inválida. Ingrese una opción nuevamente: ")
    return opcion


# trabajo_De_Texto_Con_Python
# soluciones_algorítmicas_con_Python


def suma_letras():
    cadena = input("Ingrese cadena a tratar: ")
    cadena = list(cadena)
    caracteres = []
    for i in cadena:
        contador = 0
        x = i
        if x not in caracteres:
            caracteres.append(x)
            if x != " ":
                for c in cadena:
                    if c == x:
                        contador = contador + 1
                print(f"{i} : {contador}")


def numero_n_p():
    print("El ingreso de números seguirá hasta que la respuesta sea asterisco (*)")
    while True:
        numero = input("Ingrese número a tratar: ")
        if numero == "*":
            break
        else:
            numero = float(numero)
            if numero == 0:
                print("Número igual a cero")
            elif numero > 0:
                print("Número positivo")
            elif numero < 0:
                print("Número negativo")


def sumatoritaYpromedio():
    print("El ingreso de números seguirá hasta que la respuesta sea cero (0)")
    lista = []

    while True:
        numero = float(input("Ingrese número a tratar: "))
        if numero == 0:
            break
        elif numero != int(numero):
            while numero != int(numero):
                numero = float(input("Número no entero, ingrese número a tratar: "))
        else:
            lista.append(numero)
            print(lista)
            print("La suma total es de: ")
            suma = 0
            for i in lista:
                suma = suma + i
            print(suma)
            print("El promedio total es de: ")
            print(suma / len(lista))


def suma_digitos():
    numero = int(
        input(
            "Ingrese un número entero\n Si ingresa un número con parte decimal solo se tendrá encuenta la parte entera: "
        )
    )
    numero = str(numero)
    numero = list(map(int, numero))
    suma = 0
    for i in numero:
        suma = suma + i
    print("El total de la suma de dígitos es de :", suma)


while True:
    imprimir_menu()
    opcion = obtener_opcion()
    if opcion == "1":
        suma_letras()
    elif opcion == "2":
        numero_n_p()
    elif opcion == "3":
        sumatoritaYpromedio()
    elif opcion == "4":
        suma_digitos()
    elif opcion == "5":
        print("Programa finalizado")
        break
    input("Presione cualquier tecla para continuar")
