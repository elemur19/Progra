from file_converter import FileConverter

def main():

    converter = FileConverter()

    json_data = converter.convertFromJson("catalogo.json")
    print("Datos JSON:")
    print(json_data)

    csv_data = converter.convertFromCSV("catalogo.csv")
    print("\nDatos CSV:")
    print(csv_data)


main()