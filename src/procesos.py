import csv



def limpiar_precio(precio_str):
    '''Modulo para limpiar precios'''
    return int(precio_str.replace("$", ""))


def calcular_promedio(lista):
    """Función para calcular el promedio de una lista de números"""
    if not lista: return 0
    return sum(lista) / len(lista)




def filtrar_disponibles(productos):
    """Función para filtrar productos disponibles (no agotados)"""
    return [p for p in productos if not p["agotado"]]




def generar_reporte_csv(productos, nombre_archivo):
    """Función para generar un reporte CSV con los productos disponibles"""
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Nombre', 'Precio', 'Agotado'])
        for producto in productos:
            escritor.writerow([producto['nombre'], producto['precio'], producto['agotado']])

    return f"Reporte generado: {nombre_archivo}"
