import csv


#creamos un nuevo archivo products.csv para no modificar el original.
file_path = 'products.csv'
updated_file_path = 'products_updated.csv'

#Lo abrimos con 'r' que es modo lectura:
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener el nombre de las columnas existentes
    fieldname = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode='w',  newline='') as updated_file:
        csv_write = csv.DictWriter(updated_file, fieldnames=fieldname)
        csv_write.writeheader() #Escribir los encabezados

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_write.writerow(row)
