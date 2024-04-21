from pathlib import Path
import os

actualdir=Path() # Para trabajar en el dirctorio actual. Podremos modificarlo después.
directorio=(list(Path(actualdir).iterdir())) # Para crear una lista con el contenido del directorio en el que trabajemos.

#Creamos dos funciones para usar con recurrencia dentro de las funciones que necesitaremos después.

# Esta función sirve para comprobar si hay archivos dentro del directorio actual y registrar estos en un archivo .txt que veremos después.
def subfolderscheckfiles(listado, filestructure):
    for files in list(Path(listado).iterdir()):
        checkfiles(files, filestructure)
        if files.is_dir():
            subfolderscheckfiles(files, filestructure)

# Esta función sirve para registrar los ARCHIVOS no ocultos que hay dentro del directorio actual en un archivo.txt.
def checkfiles(files, filestructure):
    if os.path.isfile(files):
            if not str(files).startswith(".") and str(files).endswith(".wav"): 
                # En mi caso me interesa registrar sólo los archivos de audio en formato wav por lo que añado esta línea: and str(files).endswith(".wav")
                print(files, file=filestructure) # Esta línea escribe el contenido del print en el archivo definido en filestructure.

# Esta función sirve para registrar TODOS los archivos dentro de la estructura de la carpeta en la que trabajemos, en el archivo de texto definido después.
def filedatabase(listado, filestructure):
    for subdir in listado:
        checkfiles(subdir, filestructure)
        if os.path.isdir(subdir):
            subfolderscheckfiles(subdir, filestructure)
# Esta función sirve para comprobar si hay subdirectorios dentro del directorio actual y registrar estos en un archivo .txt que veremos después.
def subfolders(listado, filestructure):
    for subdir in listado:
        if os.path.isdir(subdir):
            print(subdir, file=filestructure) # Esta línea escribe el contenido del print en el archivo definido en filestructure.
            subfolders(list(Path(subdir).iterdir()), filestructure)

# Creamos dos archivos de texto. Uno para almacenar la estructura de archivos del directorio donde trabajamos,
# y otro para almacenar sólamente la estructura de carpetas, sin los archivos.

# Archivo para almacenar las carpetas del directorio actual.
with open('folders.txt', 'w') as filestructure:
    subfolders(directorio, filestructure)
filestructure.close()

# Archivo para almacenar los archivos del directorio actual.
with open('filedatabase.txt', 'w') as filestructure:
    filedatabase(directorio, filestructure)
filestructure.close()