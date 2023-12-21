def verificar_negativo_y_par(numero):
    if numero < 0 and numero % 2 == 0:
        print(f"{numero} es un número negativo y par.")
    else:
        print(f"{numero} no cumple con las condiciones.")

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
verificar_negativo_y_par(numero)