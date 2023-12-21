def mostrar_palabra_10_veces():
    try:
        palabra = input("Ingrese una palabra: ")
        for _ in range(10):
            print(palabra)
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")

if __name__ == "__main__":
    mostrar_palabra_10_veces()