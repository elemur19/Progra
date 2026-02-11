abecedario = "abcdefghijklmnopqrstuvwxyz" 

def encriptar_cesar(texto, desplazamiento):
    output = ""
    texto = texto.lower()

    for letra in texto:
        if letra in abecedario:
            puesto = abecedario.index(letra)
            nuevo_puesto = (puesto + desplazamiento) % len(abecedario)
            output += abecedario[nuevo_puesto]
    return output 

def desncriptar_cesar(texto, desplazamiento):
    output = ""
    texto = texto.lower() 

    for letra in texto:
        if letra in abecedario:
            puesto = abecedario.index(letra)
            nuevo_puesto = (puesto - desplazamiento) % len(abecedario)
            output += abecedario[nuevo_puesto]
    return output 

