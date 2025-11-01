import csv

#Crear e insertar el nuevo producto al listado en su parte final

new_product = {
    'name': 'Wireless Chatger',
    'price': '78',
    'quantity': 110,
    'brand':'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2025-10-26'
}

with open('products.csv', mode='a', newline='') as file:
    #file.write('\n')
    csv_write = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_write.writerow(new_product)

