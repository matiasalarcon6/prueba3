import globales
import math

def producto_con_valor_mas_alto():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    lista_ordenada = sorted(todos_los_productos, key=lambda x: x['valor'], reverse=True)

    for i in lista_ordenada[1:]:
        print(f"El producto con mayor valor es: {i['nombre']} con un valor de ${i['valor']}")

def producto_con_iva_mas_alto():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    lista_ordenada = sorted(todos_los_productos, key=lambda x: x['iva'], reverse=True)

    for i in lista_ordenada[1:]:
        print(f"El producto con mayor valor es: {i['nombre']} con un iva de ${i['iva']}")

def promedio_valor_productos():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    suma = 0
    cantidad = 0

    for i in todos_los_productos:
        suma += i['valor']
        cantidad += 1
    
    promedio = suma / cantidad

    print(f"El promedio del valor de los productos es: ${promedio}")

def media_geometrica():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    suma = 0
    cantidad = 0

    for i in todos_los_productos:
        suma += math.log(i['valor'])
        cantidad += 1
    
    media_geo = math.exp(suma / cantidad)

    print(f"La media geometrica de los productos es: ${media_geo}")