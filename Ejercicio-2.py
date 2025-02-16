# Diccionario para el inventario
inventario = {}

# Funciones
def agregar_producto(codigo, nombre, cantidad, precio): # 1
    if codigo in inventario:
        print(f"El producto con código {codigo} ya existe.")
    else:
        inventario[codigo] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        print(f"Producto {nombre} agregado exitosamente.")

def actualizar_stock(codigo, cantidad): # 2
    if codigo in inventario:
        inventario[codigo]["cantidad"] += cantidad
    else:
        print(f"El producto {codigo} no existe.")

def registrar_venta(codigo, cantidad): # 3
    if codigo in inventario:
        if inventario[codigo]["cantidad"] >= cantidad:
            inventario[codigo]["cantidad"] -= cantidad
            print(f"Venta registrada. Stock restante de {inventario[codigo]['nombre']}: {inventario[codigo]['cantidad']}")
        else:
            print("Stock insuficiente")
            print(inventario[codigo]["cantidad"])

def mostrar_inventario(): # 4
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\nInventario actual:")
        for codigo, detalles in inventario.items():
            print(f"Código: {codigo}, Nombre: {detalles['nombre']}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")

# Menú principal
while True:
    print("\nMenú de Inventario")
    print("1. Agregar producto")
    print("2. Actualizar stock")
    print("3. Registrar venta")
    print("4. Mostrar inventario")
    print("5. Salir")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        codigo = input("\nCódigo del producto: ")
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad incial: "))
        precio = float(input("Precio por unidad: "))
        agregar_producto(codigo, nombre, cantidad, precio)
        
    elif opcion == 2:
        codigo = input("\nCódigo del producto: ")
        cantidad = int(input("Cantidad a agregar: "))
        actualizar_stock(codigo, cantidad)
        
    elif opcion == 3:
        codigo = input("\nCódigo del producto: ")
        cantidad = int(input("Cantidad a vender: "))
        registrar_venta(codigo, cantidad)
        
    elif opcion == 4:
        mostrar_inventario()
        
    elif opcion == 5:
         print("\n¡Adiós!")
         break
    
    else:
        print("\nOpción no válida, intenta de nuevo.")