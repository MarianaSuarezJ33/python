def verificar_par_y_multiplo_de_6(numero):
    if numero % 2 == 0 and numero % 6 == 0:
        print(f"{numero} es un número par y múltiplo de 6.")
    else:
        print(f"{numero} no cumple con las condiciones.")

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
verificar_par_y_multiplo_de_6(numero)