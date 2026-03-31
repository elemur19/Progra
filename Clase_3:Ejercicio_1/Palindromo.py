while True:
    texto = input("Ingrese una palabra o frase aqui: ")

    texto = texto.replace(" ", "")

    invertido = texto[::-1]

    if texto.lower() == invertido.lower():
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
