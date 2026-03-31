import random

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Colores usando ANSI
ANSI_RESET = "\033[0m"
ANSI_GREEN = "\033[92m"

#Opciones del menu
#Pide una opción al usuario hasta que sea válida.
#opciones_validas: 1,2,3,4

def pedir_opcion(mensaje, opciones_validas):
    while True:
        op = input(mensaje).strip()
        if op in opciones_validas:
            return op
        print("Opción inválida. Intente de nuevo.")

# Pide las palabras 
def pedir_palabra(mensaje):
    while True:
        w = input(mensaje).strip().upper().replace(" ", "")
        if w == "":
            print("No puede venir vacía.")
            continue

        ok = True
        for ch in w:
            if ch not in ABC:
                ok = False
                break

        if ok:
            return w

        print("Solo se permiten letras A-Z (sin tildes, sin números, sin símbolos).")

#Poner letras aleatorias para rellenar espacios de la sopa
def letra_aleatoria():
    """Devuelve una letra aleatoria A-Z."""
    return random.choice(ABC)


#Imprime la forma de de la sopa 
def imprimir_matriz(matriz, resaltadas=None, color=ANSI_GREEN):
    if resaltadas is None:
        resaltadas = set()

    for f in range(len(matriz)):
        fila_out = []
        for c in range(len(matriz[0])):
            ch = matriz[f][c]
            if (f, c) in resaltadas:
                fila_out.append(color + ch + ANSI_RESET)
            else:
                fila_out.append(ch)
        print(" ".join(fila_out))