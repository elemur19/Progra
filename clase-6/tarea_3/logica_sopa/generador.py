import random
from logica_sopa.funciones import pedir_opcion, pedir_palabra, letra_aleatoria, imprimir_matriz


# Direcciones: (df, dc)
DIRECCIONES = [
    (0, 1),    # derecha
    (0, -1),   # izquierda
    (1, 0),    # abajo
    (-1, 0),   # arriba
    (1, 1),    # diagonal abajo-derecha
    (-1, -1),  # diagonal arriba-izquierda
    (1, -1),   # diagonal abajo-izquierda
    (-1, 1),   # diagonal arriba-derecha
]

#Lista de palabras
#Pide todas las palabras en una sola línea 

def pedir_lista_palabras(max_palabras=15, min_palabras=6):
    print(f"\nIngrese sus palabras separadas por coma (,) — mínimo {min_palabras}, máximo {max_palabras}.")
    print("Ejemplo: CASA, PERRO, GATO")

    while True:
        entrada = input("\nPalabras: ").strip().upper()

        # Separar por comas, limpiar espacios, quitar vacíos
        partes = entrada.split(",")
        palabras = []
        for p in partes:
            w = p.strip().replace(" ", "")
            if w != "":
                palabras.append(w)

        # Verificar la cantidad de palabras
        if len(palabras) < min_palabras:
            print(f"Debe ingresar al menos {min_palabras} palabras.")
            continue
        if len(palabras) > max_palabras:
            print(f"Máximo permitido: {max_palabras} palabras. Usted ingresó {len(palabras)}.")
            continue

        # sin tildes, números, símbolos
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ok = True
        for w in palabras:
            if w == "":
                ok = False
                break
            for ch in w:
                if ch not in abc:
                    ok = False
                    break
            if not ok:
                break

        if not ok:
            print("Todas las palabras deben contener solo letras (sin tildes, sin números, sin símbolos).")
            continue

        # Quitar duplicados si es que hay
        sin_dupes = []
        for w in palabras:
            if w not in sin_dupes:
                sin_dupes.append(w)

        # Validar min después de quitar duplicados
        if len(sin_dupes) < min_palabras:
            print(f"Hay palabras repetidas. Ingrese solo palabras distintas.")
            continue

        return sin_dupes


#Matriz
# Crea una matriz n x n con '.' para hacer como la forma de la sopa de letras
def crear_matriz_vacia(n):
    m = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(".")
        m.append(fila)
    return m


def cabe_en_matriz(n, palabra, fila, col, df, dc):
    fin_f = fila + df * (len(palabra) - 1)
    fin_c = col + dc * (len(palabra) - 1)
    return 0 <= fin_f < n and 0 <= fin_c < n


def se_puede_colocar(matriz, palabra, fila, col, df, dc):
    n = len(matriz)
    if not cabe_en_matriz(n, palabra, fila, col, df, dc):
        return False

    for i in range(len(palabra)):
        f = fila + df * i
        c = col + dc * i
        actual = matriz[f][c]
        letra = palabra[i]
        if actual != "." and actual != letra:
            return False
    return True


def colocar_palabra(matriz, palabra, fila, col, df, dc, coords_resaltadas):
    #Coloca la palabra y guarda las coordenadas 
    for i in range(len(palabra)):
        f = fila + df * i
        c = col + dc * i
        matriz[f][c] = palabra[i]
        coords_resaltadas.add((f, c))


def llenar_vacios(matriz):
    #Rellena los '.' con letras aleatorias
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] == ".":
                matriz[f][c] = letra_aleatoria()


# Genera la sopa colocando las palabras
# Retorna: (matriz, coords_resaltadas, no_colocadas)
def generar_sopa(palabras, tam_min=10, tam_max=20, intentos_por_palabra=400):
    if not palabras:
        n = tam_min
        matriz = crear_matriz_vacia(n)
        coords = set()
        llenar_vacios(matriz)
        return matriz, coords, []

    mas_larga = 0
    for w in palabras:
        if len(w) > mas_larga:
            mas_larga = len(w)

    # Tamaño sugerido
    n = mas_larga + 5
    if n < tam_min:
        n = tam_min
    if n > tam_max:
        n = tam_max

    matriz = crear_matriz_vacia(n)
    coords_resaltadas = set()
    no_colocadas = []

    # Colocar primero las más largas
    palabras_ordenadas = sorted(palabras, key=len, reverse=True)

    for palabra in palabras_ordenadas:
        if len(palabra) > n:
            no_colocadas.append(palabra)
            continue

        colocada = False
        for _ in range(intentos_por_palabra):
            df, dc = random.choice(DIRECCIONES)
            fila = random.randint(0, n - 1)
            col = random.randint(0, n - 1)

            if se_puede_colocar(matriz, palabra, fila, col, df, dc):
                colocar_palabra(matriz, palabra, fila, col, df, dc, coords_resaltadas)
                colocada = True
                break

        if not colocada:
            no_colocadas.append(palabra)

    llenar_vacios(matriz)
    return matriz, coords_resaltadas, no_colocadas


#MENU
#Este es el menu del programa, donde se piden las palabras para crear la sopa de letras, se puede imprimir o resolver la sopa
def ejecutar_menu():
    matriz = None
    coords = set()
    no_colocadas = []

    while True:
        print("\n============================================")
        print("                 S O P A                 ")
        print("                   D E                   ")
        print("               L E T R A S               ")
        print("============================================")
        print("      Generador de Sopa de Letras  ")
        print("")
        print("1) Ingresar palabras")
        print("2) Imprimir sopa de letras")
        print("3) Resolver sopa de letras")
        print("4) Salir")

        op = pedir_opcion("Seleccione una opción: ", ["1", "2", "3", "4"])

        if op == "1":
            palabras = pedir_lista_palabras(15)
            matriz, coords, no_colocadas = generar_sopa(palabras)

            print("\nSopa generada.")
            if no_colocadas:
                print("No se pudieron colocar estas palabras:", ", ".join(no_colocadas))

        elif op == "2":
            if matriz is None:
                print("Primero genere una sopa (opción 1).")
            else:
                print("\n--- SOPA ---")
                imprimir_matriz(matriz)

        elif op == "3":
            if matriz is None:
                print("Primero genere una sopa (opción 1).")
            else:
                print("\n--- SOPA RESUELTA (RESALTADO) ---")
                imprimir_matriz(matriz, resaltadas=coords)

        else:
            print("Saliendo... Hasta Luego!")
            break