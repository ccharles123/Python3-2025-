import json

#Lectura del archivo.
with open('products.json', mode='r') as file:
    products = json.load(file)#Estamos cargando los datos del archivo.

#Mostrar el contenido.

for product in products: 
    #print(product)
    print(f"nombre : {product['nombre']} - Precio: {product['precio']}")