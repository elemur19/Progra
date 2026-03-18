def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Entrada inválida. No puede estar vacía.")


def pedir_entero(mensaje):
    while True:
        dato = input(mensaje).strip()
        try:
            valor = int(dato)
            if valor >= 0:
                return valor
            print("Debe ser un número entero mayor o igual a 0.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")


def pedir_float(mensaje):
    while True:
        dato = input(mensaje).strip()
        try:
            valor = float(dato)
            if valor >= 0:
                return valor
            print("Debe ser un número mayor o igual a 0.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")