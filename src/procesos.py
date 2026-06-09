import csv


'''Modulo para limpiar precios y calcular promedios de precios de productos'''
def limpiar_precio(precio_str):
    return int(precio_str.replace("$", ""))

def calcular_promedio(lista):
    if not lista: return 0
    return sum(lista) / len(lista)

"""Función para filtrar productos disponibles (no agotados)"""

def filtrar_disponibles(productos):
    return [p for p in productos if not p["agotado"]]

def generar_reporte_csv(productos, nombre_archivo):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Nombre', 'Precio', 'Agotado'])
        for producto in productos:
            escritor.writerow([producto['nombre'], producto['precio'], producto['agotado']])

    return f"Reporte generado: {nombre_archivo}"