def verificar_impar_y_multiplo_de_5(numero):
    if numero % 2 != 0 and numero % 5 == 0:
        print(f"{numero} es un número impar y múltiplo de 5.")
    else:
        print(f"{numero} no cumple con las condiciones.")

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
verificar_impar_y_multiplo_de_5(numero)