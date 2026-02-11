#Definir PI 

PI = 3.14

# Formulas 

def volumen_cubo(lado):
    return lado * lado * lado

def volumen_paralelepipedo(largo, ancho, alto):
    return largo * ancho * alto

def volumen_cilindro(radio, altura):
    return PI * radio * radio * altura

def volumen_esfera(radio):
    return (4.0/3.0) * PI * radio * radio * radio

def volumen_cono(radio, altura):
    return (1.0/3.0) * PI * radio * radio * altura