def verificar_multiplo_de_7_y_par(numero):
    if numero % 7 == 0 and numero % 2 == 0:
        print(f"{numero} es un múltiplo de 7 y par.")
    else:
        print(f"{numero} no cumple con las condiciones.")

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
verificar_multiplo_de_7_y_par(numero)