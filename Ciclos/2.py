def obtener_numero_positivo():
    while True:
        try:
            numero = float(input("Ingrese un número positivo: "))
            if numero > 0:
                return numero
            else:
                print("Por favor, ingrese un número mayor que cero.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Llamada a la función para obtener un número positivo
numero_positivo = obtener_numero_positivo()

print(f"Has ingresado el número positivo: {numero_positivo}")