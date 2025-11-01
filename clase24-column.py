import csv


#Define nombre de los archivos  y se crea uno nuevo para no modificar el original.
file_path = 'products.csv' #Es el archivo original (el que ya existe).
updated_file_path = 'products_updated.csv' #es el nuevo archivo que se creará con los cambios. Así se evita dañar el archivo original.

#Lo abrimos con 'r' que es modo lectura:
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file) #lee cada fila del archivo y la convierte en un diccionario. Por ejemplo: {'name': 'Mouse', 'price': '50', 'quantity': '3', ...}
    #Obtener el nombre de las columnas existentes
    fieldname = csv_reader.fieldnames + ['total_value'] #Obtiene los nombres de las columnas del archivo original (por ejemplo: ['name', 'price', 'quantity', 'brand', 'category', 'entry_date']). Luego se agrega una nueva columna llamada 'total_value'.

    with open(updated_file_path, mode='w',  newline='') as updated_file: #Crea el nuevo archivo y lo abre en modo escritura ('w')
        csv_write = csv.DictWriter(updated_file, fieldnames=fieldname) #permite escribir diccionarios como filas.
        csv_write.writeheader() #Escribe la primera fila del archivo (los nombres de las columnas).

        #Calcula el valor total de cada producto
        for row in csv_reader: #Recorre cada fila del archivo original.
            row['total_value'] = float(row['price']) * int(row['quantity']) #Convierte price en número decimal (float) y quantity en entero (int).
            csv_write.writerow(row) #Multiplica ambos para obtener el valor total del inventario de ese producto.
