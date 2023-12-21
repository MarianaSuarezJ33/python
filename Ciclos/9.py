def mostrar_triangulo_rectangulo(numero):
    for i in range(1, numero + 1):
        for j in range(2 * i - 1, 0, -2):
            print(j, end=" ")
        print()

def main():
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero <= 0:
            print("Por favor, ingrese un número entero positivo.")
        else:
            mostrar_triangulo_rectangulo(numero)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()