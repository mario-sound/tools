# tools
Tools for files and directories management.

En este repositorio compartiré herramientas útiles para el manejo de archivos y directorios.

structure.py
  En este archivo, encontraremos diferentes funciones que nos permiten crear dos archivos de texto. "folders.txt" y "filedatabase.txt"
  "folders.txt"
     Almacenará la estructura de carpetas/directorios y subcarpetas/subdirectorios del directorio actual, sin almacenar en este los nombres de los archivos.
  "filedatabase.txt"
     Almacenará los nombres de los archivos que hay en la ruta actual y los nombres de todos los archivos que haya en los diferentes subdirectorios.

  Utilidad:
    Esto es útil para obtener un listado de archivos completo para comprobar una base de datos con la que podemos necesitar trabajar después.
    También nos permite obtener la estructura de carpetas de manera sencilla, para después poder regenerar esta estructura.
    Ejemplo:
      Supongamos un proyecto de audio en el que recibimos 1000 archivos de audio en los que tenemos 1000 líneas diferentes de diálogo en inglés. También recibimos un script/guión con el texto y nombre de estos archivos.
      El objetivo es entregar al cliente la misma estructura de archivos y carpetas pero con los audios traducidos a español.
      Una vez recibimos la base de audio original, podemos comprobar si es correcta con nuestro archivo "filedatabase.txt" y una sencilla comprobación en Excel.
      Una vez hayamos generado los audios en español, necesitaremos mover estos a la estructura de carpetas original, la cual tenemos en el archivo "folders.txt".
