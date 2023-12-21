def mostrar_tabla_multiplicar():
    for i in range(1, 11):
        print(f"\nTabla de multiplicar del {i}:\n")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")

if __name__ == "__main__":
    mostrar_tabla_multiplicar()