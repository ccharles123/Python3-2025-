import statistics #statistics: contiene funciones estadísticas como mean, median, mode, etc.
import csv

monthly_sales = {} #Crea un diccionario vacío llamado monthly_sales, donde se guardarán los datos de ventas.

with open('monthly_sales.csv', mode='r') as file: #Abre el archivo llamado monthly_sales.csv en modo lectura ('r').
    reader = csv.DictReader(file)   #Crea un lector CSV que interpreta cada fila del archivo como un diccionario, donde las claves son los nombres de las columnas (por ejemplo: 'month' y 'sales').                                    
    for row in reader: #Recorre cada fila del archivo CSV.
        month = row['month'] #Extrae el nombre del mes desde la columna 'month'.
        sales = int(row['sales']) #Toma el valor de la columna 'sales' y lo convierte a entero (de texto a número).
        monthly_sales[month] = sales #Guarda el par clave-valor en el diccionario monthly_sales. {'January': 1200, 'February': 1350, 'March': 980}

sales = list(monthly_sales.values()) #Crea una lista con solo los valores numéricos (las ventas), sin los meses. [1200, 1350, 980]
print(sales) #Muestra la lista de ventas en pantalla.

#hallamos la media aritmética (promedio) de los datos:

mean_sales = statistics.mean(sales) #La función usada es statistics.mean(), que devuelve el valor central si los datos están ordenados.

print(f'La media es: {mean_sales}')

#Hallamos la mediana 

median_sales = statistics.median(sales)
print(f'La mediana es: {median_sales}')

#Hallamos la Moda:
mode_sales = statistics.mode(sales)
print(f'La moda es: {mode_sales}')

#Hallamos la desviacion Estandar:
stdev_sales = statistics.stdev(sales)
print(f'La desviacion estandar es: {stdev_sales}')

#Hallamos la varianza
variance_sales = statistics.variance(sales)
print(f'La variance es: {variance_sales}')

#Extraer el dato Maximo y el Minimo:
max_sale = max(sales)
min_sale = min(sales)

print(f'El dato Max es: {max_sale} y el dato minimo es: {min_sale}')

#hallar el rango en el que tenemos las ventas:
range_sale = max_sale - min_sale
print(f'El rango de ventas es: {range_sale}')