"""
1. Carga de Datos:
Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. 
Cada venta debe incluir las siguientes claves:
«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
«producto»: una cadena de texto que represente el nombre del producto vendido.
«cantidad»: un número entero que represente la cantidad de productos vendidos.
«precio»: un número flotante que represente el precio unitario del producto.
"""
# Creando la lista de ventas
ventas = [
  { "fecha": "01-05-2025", "producto": "Bisagra 35x35 negra", "cantidad": 10, "precio": 15.900 },
  { "fecha": "03-05-2025", "producto": "Cerradura de sobreponer 2002", "cantidad": 5, "precio": 50.900 },
  { "fecha": "05-05-2025", "producto": "Cerradura eléctrica 2150", "cantidad": 8, "precio": 92.900},
  { "fecha": "05-05-2025", "producto": "Candado clásico 30mm", "cantidad": 12, "precio": 15.900 },
  { "fecha": "12-05-2025", "producto": "Candado clásico 15mm", "cantidad": 7, "precio": 8.100 }
]

"""
2. Cálculo de Ingresos Totales:
Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales 
generados por todas las ventas. Los ingresos totales se calculan multiplicando 
la cantidad vendida por el precio unitario para cada venta y sumando los resultados
"""
ingresos_totales = 0

# Bucle para calcular ingresos totales de ventas
for venta in ventas:
  subtotal_venta = venta["cantidad"] * venta["precio"]
  ingresos_totales += subtotal_venta

# Imprimir el ingreso total
print(f"Ingreso total de ventas: ${ ingresos_totales }") #Ingreso total de ventas: $1404.2




"""
3. Análisis del Producto Más Vendido:
- Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y 
los valores sean la cantidad total vendida de cada producto.
- Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.
"""
# Crear un diccionario para almacenar las ventas por producto
ventas_por_producto = {}

# Agregando producto y su cantidad vendida al diccionario ventas_por_producto
for venta in ventas:
  producto = venta["producto"]
  cantidad = venta["cantidad"]
  
  if producto in ventas_por_producto:
    ventas_por_producto[producto] += cantidad
  else:
    ventas_por_producto[producto] = cantidad

# Encontrar el producto más vendido
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_total = ventas_por_producto[producto_mas_vendido]

# Imprimir las ventas por producto y el producto más vendido
print("\nVentas por producto:")
for producto, cantidad in ventas_por_producto.items():
  print(f"- {producto}: {cantidad} unidades")

# Imprimir el producto más vendido
print(f"\nProducto más vendido: '{producto_mas_vendido}' con {cantidad_total} unidades vendidas")
#Producto más vendido: 'Candado clásico 30mm' con 12 unidades vendidas


"""
4. Promedio de Precio por Producto:
- Crea un diccionario llamado precios_por_producto donde las claves 
sean los nombres de los productos y los valores sean tuplas. 
Cada tupla debe contener dos elementos: la suma de los precios de venta de 
todas las unidades vendidas y la cantidad total de unidades vendidas.

- Calcula el precio promedio de venta para cada producto utilizando 
la información de este diccionario.
"""

precios_por_producto = {}

for venta in ventas:
  producto = venta["producto"]
  cantidad = venta["cantidad"]
  precio_total_venta = venta["precio"] * cantidad
  
  if producto in precios_por_producto:
    # Sumamos al precio total y a la cantidad total
    precio_total, cantidad_total = precios_por_producto[producto]
    precios_por_producto[producto] = (precio_total + precio_total_venta, cantidad_total + cantidad)
  else:
    precios_por_producto[producto] = (precio_total_venta, cantidad)

# Calculamos y mostramos los promedios
print("\nPrecio promedio por producto:")
for producto, (precio_total, cantidad_total) in precios_por_producto.items():
  precio_promedio = precio_total / cantidad_total
  print(f"- {producto}: ${precio_promedio:.2f} (basado en {cantidad_total} unidades)")

# Precio promedio por producto:
# - Bisagra 35x35 negra: $15.90 (basado en 10 unidades)
# - Cerradura de sobreponer 2002: $50.90 (basado en 5 unidades)
# - Cerradura eléctrica 2150: $92.90 (basado en 8 unidades)
# - Candado clásico 30mm: $15.90 (basado en 12 unidades)
# - Candado clásico 15mm: $8.10 (basado en 7 unidades)


"""
5. Ventas por Día:
- Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas 
y los valores sean los ingresos totales generados en cada día.

- Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.
"""

ingresos_por_dia = {}

# Agregando ingresos por día al diccionario ingresos_por_dia
for venta in ventas:
  fecha = venta["fecha"]
  ingreso = venta["cantidad"] * venta["precio"]
  
  if fecha in ingresos_por_dia:
    ingresos_por_dia[fecha] += ingreso
  else:
    ingresos_por_dia[fecha] = ingreso

# Mostramos los resultados
print("\nIngresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"- {fecha}: ${ingreso}")

# Ingresos por día:
# - 01-05-2025: $159.0
# - 03-05-2025: $254.5
# - 05-05-2025: $934.0
# - 12-05-2025: $56.699


"""
6. Representación de Datos:
- Crea un diccionario llamado resumen_ventas donde las claves sean los nombres 
de los productos y los valores sean diccionarios anidados. 
Cada diccionario anidado debe contener:
  - «cantidad_total»: la cantidad total vendida del producto.
  -«ingresos_totales»: los ingresos totales generados por la venta del producto.
  -«precio_promedio»: el precio promedio de venta del producto.
"""
resumen_ventas = {}

# Agregando información al diccionario resumen_ventas
for venta in ventas:
  producto = venta["producto"]
  cantidad = venta["cantidad"]
  ingreso = venta["cantidad"] * venta["precio"]
  
  if producto in resumen_ventas:
    # Se actualizan los valores existentes
    resumen_ventas[producto]["cantidad_total"] += cantidad
    resumen_ventas[producto]["ingresos_totales"] += ingreso
  else:
    # Se crean nuevas entradas
    resumen_ventas[producto] = {
      "cantidad_total": cantidad,
      "ingresos_totales": ingreso
    }

# Calculo de precios promedios
for producto, datos in resumen_ventas.items():
    datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"]

# Imprimir resumen completo
print("\nResumen completo de ventas por producto:")
for producto, datos in resumen_ventas.items():
    print(f"\nProducto: {producto}")
    print(f"- Cantidad total vendida: {datos['cantidad_total']} unidades")
    print(f"- Ingresos totales: ${datos['ingresos_totales']}")
    print(f"- Precio promedio: ${datos['precio_promedio']}")

# Producto: Bisagra 35x35 negra
# - Cantidad total vendida: 10 unidades
# - Ingresos totales: $159.0
# - Precio promedio: $15.9

# Producto: Cerradura de sobreponer 2002
# - Cantidad total vendida: 5 unidades
# - Ingresos totales: $254.5
# - Precio promedio: $50.9

# Producto: Cerradura eléctrica 2150
# - Cantidad total vendida: 8 unidades
# - Ingresos totales: $743.2
# - Precio promedio: $92.9

# Producto: Candado clásico 30mm
# - Cantidad total vendida: 12 unidades
# - Ingresos totales: $190.8
# - Precio promedio: $15.9

# Producto: Candado clásico 15mm
# - Cantidad total vendida: 7 unidades
# - Ingresos totales: $56.699999999999996
# - Precio promedio: $8.1