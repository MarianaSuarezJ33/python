def obtener_precio_y_descripcion(plato_elegido):
    menu = {
        "hamburguesa": {"precio": 10.0, "descripcion": "Hamburguesa con queso y papas fritas."},
        "pizza": {"precio": 8.0, "descripcion": "Pizza de pepperoni."},
        "ensalada": {"precio": 6.0, "descripcion": "Ensalada fresca con aderezo de la casa."},
        # Agrega más platos según sea necesario
    }

    if plato_elegido in menu:
        precio = menu[plato_elegido]["precio"]
        descripcion = menu[plato_elegido]["descripcion"]
        print(f"Precio: ${precio:.2f}")
        print(f"Descripción: {descripcion}")
    else:
        print("Plato no encontrado en el menú.")

# Ejemplo de uso
plato_pedido = input("Ingrese el plato que desea (hamburguesa, pizza, ensalada, etc.): ").lower()
obtener_precio_y_descripcion(plato_pedido)