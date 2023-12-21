def verificar_numero_entero(numero):
    if isinstance(numero, int):
        print(f"{numero} es un número entero.")
    else:
        print(f"{numero} no es un número entero.")

# Ejemplo de uso
numero = float(input("Ingrese un número: "))
verificar_numero_entero(numero)