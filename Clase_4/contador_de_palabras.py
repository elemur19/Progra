
texto = input("Ingrese el texto que quiere revisar: ")
texto = texto.lower()
puntuacion = ".,;:!?"

for signo in puntuacion:
    texto = texto.replace(signo, "")


palabras = texto.split()

palabras_ignoradas = ["el", "la", "de", "y", "a", "un", "una"]

palabras_filtradas = []

for palabra in palabras:
    if palabra not in palabras_ignoradas:
        palabras_filtradas.append(palabra)


contador = {}

for palabra in palabras_filtradas:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

total_de_palabras = len(palabras_filtradas)
palabras_unicas = len(contador)

# 9. Ordenar palabras por frecuencia (mayor a menor)
lista_palabras = list(contador.items())

for i in range(len(lista_palabras)):
    for j in range(i + 1, len(lista_palabras)):
        if lista_palabras[j][1] > lista_palabras[i][1]:
            lista_palabras[i], lista_palabras[j] = lista_palabras[j], lista_palabras[i]


print("\nCantidad total de palabras (sin contar palabras ignoradas):", total_de_palabras)
print("Cantidad de palabras únicas:", palabras_unicas)
print("Top 5 palabras más repetidas:")

limite = 5
if len(lista_palabras) < 5:
    limite = len(lista_palabras)

for i in range(limite):
    palabra = lista_palabras[i][0]
    frecuencia = lista_palabras[i][1]
    print(palabra, "->", frecuencia)
