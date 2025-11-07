import os

#cwd = Current Working Directory
#Obtener el directoiro actual
"""cwd = os.getcwd()
print("El directorio de trabajo actual: ",cwd)"""

#Listar los archivos .txt de esta carpeta
txt_file = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_file)

#Renombrar archivo: 
os.rename('caperucitaRoja.txt', 'cuento.txt')
print("El archivo ha sido Renombrado")

#Listar los archivos .txt de esta carpeta
txt_file = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_file)