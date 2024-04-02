import json
from datetime import datetime, timedelta
import os

# Lee los datos desde el archivo JSON
with open(r'C:\Users\MarinaSmall\Documents\MasterBio\TFM\datos\zepplife_copy.json', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    datos = json.loads(contenido)
    

# Crear el directorio si no existe
directorio = "datos/sleep_time2/"
if not os.path.exists(directorio):
    os.makedirs(directorio)

# Crear el diccionario lista_sueños
lista_sueños = {}
for element in datos["rows"]:
    lista_sueños[element[2]] = element[3]


for clave, valor in lista_sueños.items():
    valor = json.loads(valor)
    # Verificar si "slp" existe antes de convertir
    if "slp" in valor:
        slp = valor["slp"]
        if "st" in slp:
            st_tiempo = slp["st"]
            st_legible_st = datetime.utcfromtimestamp(st_tiempo)
            slp["st"] = st_legible_st.strftime('%Y-%m-%d %H:%M:%S')


        if "ed" in slp:
            ed_tiempo = slp["ed"]
            ed_legible_ed = datetime.utcfromtimestamp(ed_tiempo)
            slp["ed"] = ed_legible_ed.strftime('%Y-%m-%d %H:%M:%S')

        if "stage" in slp:
            stages = slp["stage"]
            for stage in stages:
                if "start" in stage:
                    st_unix = stage["start"]
                    # Verificar si el timestamp está en milisegundos y convertirlo a segundos si es necesario
                    if st_unix > 1_000_000_000_000:
                        st_unix = st_unix / 1000  # Convertir de milisegundos a segundos
                    st_legible = datetime.utcfromtimestamp(st_unix)
                    stage["start"] = st_legible.strftime('%H:%M:%S')

                if "stop" in stage:
                    ed_unix = stage["stop"]
                    # Verificar si el timestamp está en milisegundos y convertirlo a segundos si es necesario
                    if ed_unix > 1_000_000_000_000:
                        ed_unix = ed_unix / 1000  # Convertir de milisegundos a segundos
                    ed_legible = datetime.utcfromtimestamp(ed_unix)
                    stage["stop"] = ed_legible.strftime('%H:%M:%S')

    # Guardar el contenido actualizado en el diccionario
        valor["slp"] = slp
        lista_sueños[clave] = json.dumps(valor)

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


