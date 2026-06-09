import json
import os
from procesos import limpiar_precio, calcular_promedio, filtrar_disponibles, generar_reporte_csv


"""Este script carga un archivo JSON con información de productos"""
def cargar_productos(nombre_archivo):
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    
    ruta_completa = os.path.join(carpeta_actual, '..', 'data', nombre_archivo)

    try:
        with open(ruta_completa, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró en la ruta '{ruta_completa}'.")
        return []
    
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_archivo}' no contiene un JSON válido.")
        return []


"""Función principal que carga los productos, limpia los precios, calcula el promedio y lo imprime"""
def main():
    productos = cargar_productos('productos.json')
    disponibles = filtrar_disponibles(productos)
    mensaje = generar_reporte_csv(disponibles, 'reporte_disponibles.csv')
    print(mensaje)


    precios = [limpiar_precio(p['precio']) for p in disponibles]

    if precios:
        promedio = calcular_promedio(precios)
        maximo = max(precios)
        minimo = min(precios)

        print(f"El precio promedio es: {promedio:.2f}")
        print(f"El precio máximo es: {maximo}")
        print(f"El precio mínimo es: {minimo}")
    else:
        print("No hay productos disponibles para calcular el promedio.")


if __name__ == "__main__":
    main()