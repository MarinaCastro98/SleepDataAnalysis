import json
from datetime import datetime, timedelta
import os

# Lee los datos desde el archivo JSON
with open(r'C:\Users\MarinaSmall\Documents\MasterBio\TFM\datos\zepplife_copy.json', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    datos = json.loads(contenido)
    
# Crear el directorio si no existe
directorio = "datos/sleep_time/"
if not os.path.exists(directorio):
    os.makedirs(directorio)

# Crear el diccionario lista_sueños
lista_sueños = {}
for element in datos["rows"]:
    lista_sueños[element[2]] = element[3]

# Guardar cada clave y valor en un archivo dentro del directorio
for clave, valor in lista_sueños.items():
    # Nombre del archivo
    nombre_archivo = f"{clave}.json"
    
    # Ruta completa del archivo
    ruta_archivo = os.path.join(directorio, nombre_archivo)
    
    # Guardar el contenido en el archivo
    with open(ruta_archivo, "w") as archivo:
        archivo.write(valor)

    print(f"Archivo '{nombre_archivo}' creado en '{directorio}' con éxito.")


