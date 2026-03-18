

def validar_datos(lista):
    operadores = ["+", "-", "*", "/"]

 
    if len(lista) < 3:
        return False

    if lista[-1] in operadores:
        return False

    for i in range(len(lista)):
        if i % 2 == 0:
            if not lista[i].isdigit() or int(lista[i]) > 9:
                return False
        else:
            if lista[i] not in operadores:
                return False

    return True


def error():
    print("Error: Operación Inválida")
5


def calcular(lista):
    resultado = int(lista[0])
    i = 1

    while i < len(lista):
        operador = lista[i]
        numero = int(lista[i + 1])

        if operador == "+":
            resultado += numero
        elif operador == "-":
            resultado -= numero
        elif operador == "*":
            resultado *= numero
        elif operador == "/":
            if numero == 0:
                print("Inválido: división entre cero")
                return
            resultado /= numero

        i += 2

    print("Resultado:", resultado)


def main():
    operacion = input("Ingrese una operación:")
    lista = operacion.split()

    if not validar_datos(lista):
        error()
        return

    calcular(lista)


main()
