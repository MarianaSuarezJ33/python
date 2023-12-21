def mostrar_combo(numero_combo):
    combos = {
        1: "Combo de hamburguesas de carne al horno con jugo de coco",
        # Agrega más combos según sea necesario
    }

    if numero_combo in combos:
        print(combos[numero_combo])
    else:
        print("Combo no válido.")

# Ejemplo de uso
numero_combo = int(input("Ingrese el número del combo: "))
mostrar_combo(numero_combo)