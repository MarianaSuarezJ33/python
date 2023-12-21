def calcular_nomina(sueldo_empleado1, sueldo_empleado2):
    total_nomina = sueldo_empleado1 + sueldo_empleado2
    print(f"La nómina total de la empresa es: {total_nomina}.")

# Ejemplo de uso
sueldo1 = float(input("Ingrese el sueldo del primer empleado: "))
sueldo2 = float(input("Ingrese el sueldo del segundo empleado: "))
calcular_nomina(sueldo1, sueldo2)