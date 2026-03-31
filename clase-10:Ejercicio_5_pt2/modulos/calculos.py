# Funciones para realizar cálculos de promedios de edad, salario y peso

def calcular_promedio(lista_numeros):
    if len(lista_numeros) == 0:
        return 0
    return sum(lista_numeros) / len(lista_numeros)


def calcular_promedios(personas):
    edades = []
    salarios = []
    pesos = []

    for persona in personas:
        edades.append(persona["edad"])
        salarios.append(persona["salario"])
        pesos.append(persona["peso"])

    promedios = {
        "edad": calcular_promedio(edades),
        "salario": calcular_promedio(salarios),
        "peso": calcular_promedio(pesos)
    }

    return promedios