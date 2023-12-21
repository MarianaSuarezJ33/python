def evaluar_nota(nota):
    if 0 <= nota <= 0.9:
        mensaje = f"Perdida la materia en {nota} sin tener recuperación."
    elif 1.0 <= nota <= 2.5:
        mensaje = f"Perdida la materia en {nota}, pero se puede recuperar."
    elif 2.6 <= nota <= 2.9:
        mensaje = f"Perdida la materia en {nota}, pero se puede nivelar máximo nota final 3.5."
    elif 3.0 <= nota <= 3.5:
        mensaje = f"Aceptable: {nota} por recuperación."
    elif 3.6 <= nota <= 3.9:
        mensaje = f"Aceptable: {nota}, te recomiendo que sigas mejorando, vas bien."
    elif 4.0 <= nota <= 4.5:
        mensaje = f"Excelente: {nota}, vas por un buen camino hacia el éxito."
    elif 4.6 <= nota <= 5.0:
        mensaje = f"Científico: {nota}, tienes un gran futuro adelante."
    else:
        mensaje = "Nota no válida."

    print(mensaje)

# Ejemplo de uso
nota_ingresada = float(input("Ingrese la nota (0.0 - 5.0): "))
evaluar_nota(nota_ingresada)