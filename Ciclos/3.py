def obtener_numero_tres_cifras():
    while True:
        try:
            numero = int(input("Ingrese un número positivo de 3 cifras: "))
            if 100 <= numero <= 999:
                return numero
            else:
                print("Por favor, ingrese un número de 3 cifras.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Llamada a la función para obtener un número de 3 cifras
numero_tres_cifras = obtener_numero_tres_cifras()

print(f"Has ingresado el número de 3 cifras: {numero_tres_cifras}")