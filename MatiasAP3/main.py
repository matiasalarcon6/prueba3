import os
import globales
import asignar
import estadisticas
import random
os.system("cls")

def ver_estadisticas():
    print("=== ESTADISTICAS ===")
    print("1. Producto con valor más alto.")
    print("2. Producto con valor del IVA más bajo.")
    print("3. Promedio del valor de los productos.")
    print("4. Media geométrica del valor de los productos.")

    try:
        opcion = globales.seleccionar_opcion(4)
    except:
        pass
    
    if opcion == 1:
        print("1. Producto con valor más alto.")
        estadisticas.producto_con_valor_mas_alto()
    elif opcion == 2:
        print("2. Producto con valor del IVA más bajo.")
        estadisticas.producto_con_iva_mas_alto()
    elif opcion == 3:
        print("3. Promedio del valor de los productos.")
        estadisticas.promedio_valor_productos()
    elif opcion == 4:
        print("4. Media geométrica del valor de los productos.")
        estadisticas.media_geometrica()


def asignar_montos_aleatorios():
    ventas = globales.leer_archivo_json('ventas.json')
    productos = globales.leer_archivo_json('productos.json')


    for producto in productos:
        nombre = producto['Nombre']
        valor = random.randint(2000,10000)
        iva = int(valor*0.19)

        valores_aleatorios = {
            'nombre': nombre,
            'valor': valor,
            'iva': iva
        }
        ventas.append(valores_aleatorios)
        
    globales.guardar_archivo_json('ventas.json', ventas)
    print("Montos ingresados")


    
def menu_principal():
    print("=== MENU ===")
    print("1. Asignar montos aleatorios.")
    print("2. Ver estadístcas.")
    print("3. Salir del programa")

    try:
        opcion = globales.seleccionar_opcion(3)
    except:
        pass

    if opcion == 1:
        print("1. Asignar montos aleatorios.")
        asignar_montos_aleatorios()
    elif opcion == 2:
        print("2. Ver estadístcas.")
        ver_estadisticas()
    elif opcion == 3:
        os.system("cls")
        print("Usted salio del programa")
        return

menu_principal()