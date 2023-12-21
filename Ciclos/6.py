def mostrar_anios_cumplidos(edad):
    print("Años que has cumplido:")
    for anio in range(1, edad + 1):
        print(anio)

def main():
    try:
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            print("Por favor, ingrese una edad válida.")
        else:
            mostrar_anios_cumplidos(edad)
    except ValueError:
        print("Por favor, ingrese una edad válida.")

if __name__ == "__main__":
    main()