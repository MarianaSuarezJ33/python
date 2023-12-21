def acceso_a_salas(creditos):
    salas = ["Consolas", "Juegos 2D", "Juegos 3D", "Realidad Virtual"]

    if creditos == 4:
        print("Acceso a todas las salas.")
    elif creditos == 3:
        print("Acceso a las tres primeras salas.")
    elif creditos == 2:
        print("Acceso a las dos primeras salas.")
    elif creditos == 1:
        print("Acceso a la primera sala.")
    else:
        print("Número de créditos no válido.")

# Ejemplo de uso
creditos = int(input("Ingrese la cantidad de créditos (1-4): "))
acceso_a_salas(creditos)