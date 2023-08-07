import csv
import json

# Leer el archivo CSV y crear el objeto JSON
def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Saltar la primera fila si es el encabezado
        for row in reader:
            id = int(row[0])
            artista = row[1]
            nombre = row[2]
            cancion = {'id': id, 'artista': artista, 'nombre': nombre}
            data.append(cancion)

    # Escribir el objeto JSON en un archivo
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=2)

# Llamar a la función con el nombre del archivo CSV y el nombre deseado para el archivo JSON
csv_to_json('canciones.csv', 'canciones.json')
