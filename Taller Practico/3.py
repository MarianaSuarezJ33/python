import datetime

def mostrar_reloj():
    ahora = datetime.datetime.now()
    print(f"Hora: {ahora.hour:02d}:{ahora.minute:02d}:{ahora.second:02d}")

# Ejemplo de uso
mostrar_reloj()