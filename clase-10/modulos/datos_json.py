import json

# Función para leer personas desde un archivo JSON
def leer_personas_json(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    personas = []

# Abrir el archivo JSON y leer su contenido
    for persona in datos:
        registro = {
            "edad": float(persona["edad"]),
            "salario": float(persona["salario"]),
            "peso": float(persona["peso"])
        }
        personas.append(registro)

    return personas