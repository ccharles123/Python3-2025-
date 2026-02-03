import json

file_path = 'products.json' #Define la ruta del archivo JSON donde están guardados los productos.

new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accesories",
    "entry_date":"2024-07-04"
}

with open(file_path, mode='r') as file: #Abre el archivo products.json en modo lectura ('r').
    products = json.load(file) #Con json.load(file) convierte el contenido del archivo JSON en una lista de diccionarios de Python y la guarda en la variable products.

products.append(new_product) #Agrega el diccionario new_product al final de la lista products. Ahora la lista contiene todos los productos anteriores + el nuevo.

with open(file_path, mode='w') as file: # Abre el archivo products.json en modo escritura ('w') —esto borra el contenido anterior del archivo.
    json.dump(products, file, indent=4) #Luego usa json.dump() para guardar la lista products (que ya incluye el nuevo producto) nuevamente dentro del archivo en formato JSON. El parámetro indent=4 hace que el archivo quede bien formateado (con 4 espacios de sangría), facilitando su lectura.