def verificar_primo_par_impar(numero):
    es_primo = True

    if numero < 2:
        es_primo = False
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break

    if es_primo:
        mensaje_primo = f"{numero} es un número primo."
    else:
        mensaje_primo = f"{numero} no es un número primo."

    if numero % 2 == 0:
        mensaje_par_impar = f"{numero} es un número par."
    else:
        mensaje_par_impar = f"{numero} es un número impar."

    print(mensaje_primo)
    print(mensaje_par_impar)

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número: "))
verificar_primo_par_impar(numero_ingresado)