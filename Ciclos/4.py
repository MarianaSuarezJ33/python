def es_numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    return suma_divisores == numero

def main():
    try:
        # Solicitar al usuario que ingrese un número positivo
        numero = int(input("Ingrese un número positivo: "))

        if numero > 0:
            if es_numero_perfecto(numero):
                print(f"{numero} es un número perfecto.")
            else:
                print(f"{numero} no es un número perfecto.")
        else:
            print("Por favor, ingrese un número positivo.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()