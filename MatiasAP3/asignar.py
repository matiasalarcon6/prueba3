import globales
import random


def asignar_montos_aleatorios():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    for productos in todos_los_productos:
        nombre = random.choice(productos)
        valor = random.randint(2000,10000)
        iva = int(valor*0.19)

        valores_aleatorios = {
            'nombre': nombre,
            'valor': valor,
            'iva': iva
        }
        todos_los_productos.append(valores_aleatorios)
        
    globales.guardar_archivo_json('productos.json', todos_los_productos)