import time

def contar_regresivo(horas, minutos, segundos):
    tiempo_total_segundos = horas * 3600 + minutos * 60 + segundos

    while tiempo_total_segundos > 0:
        horas_restantes, rem = divmod(tiempo_total_segundos, 3600)
        minutos_restantes, segundos_restantes = divmod(rem, 60)

        print(f"{horas_restantes:02d}:{minutos_restantes:02d}:{segundos_restantes:02d}")
        time.sleep(1)
        tiempo_total_segundos -= 1

    print("¡Tiempo agotado!")

def main():
    try:
        horas = int(input("Ingrese las horas: "))
        minutos = int(input("Ingrese los minutos: "))
        segundos = int(input("Ingrese los segundos: "))

        if horas < 0 or minutos < 0 or segundos < 0:
            print("Por favor, ingrese valores no negativos.")
        else:
            contar_regresivo(horas, minutos, segundos)

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()