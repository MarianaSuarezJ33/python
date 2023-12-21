def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    try:
        # Solicitar al usuario que ingrese un número
        numero = int(input("Ingrese un número para obtener su tabla de multiplicar: "))
        
        # Llamar a la función para imprimir la tabla de multiplicar
        tabla_multiplicar(numero)

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()