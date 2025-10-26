import csv

# Abrir el archivo en modo lectura especificando su nombre,  itera sobre cada fila del archivo y las imprime como diccionarios.
"""with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file) #Abrir el archivo en formato diccionario.
    for row in csv_reader:
        print(row)"""

# Visualizar datos específicos por columnas, se puede modificar el código para que imprima solo los valores de interés:
"""with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file) #Abrir el archivo en formato diccionario.
    for row in csv_reader:
        print(f"Producto: {row['name']} - Precio: {row['price']} - Cantidad: {row['quantity']}")"""

# Para añadir información al final de un archivo CSV, emplea el modo de apertura "append" ('a'). Aquí creamos un nuevo producto y agregamos sus datos:
"""new_product = {
    'nombre': 'Cargador Inalámbrico',
    'precio': '75',
    'cantidad': 100,
    'marca': 'MarcaX',
    'categoría': 'accesorios',
    'fecha_entrada': '2023-10-15'
}

with open('products.csv', mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=new_product.keys())
    writer.writerow(new_product)"""