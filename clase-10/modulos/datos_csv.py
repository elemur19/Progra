import csv

# Función para leer personas desde un archivo CSV
def leer_personas_csv(ruta_archivo):
    personas = []

# Abrir el archivo CSV y leer su contenido
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            persona = {
                "edad": float(fila["edad"]),
                "salario": float(fila["salario"]),
                "peso": float(fila["peso"])
            }
            personas.append(persona)

    return personas