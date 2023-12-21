def ofrecer_bebida(menu):
    if menu == "carne":
        print("Bebida recomendada: vino tinto.")
    elif menu == "pescado":
        print("Bebida recomendada: vino blanco.")
    elif menu == "verdura":
        print("Bebida recomendada: agua.")
    else:
        print("Elija carne, pescado o verdura.")

# Ejemplo de uso
menu_elegido = input("Elija carne, pescado o verdura: ").lower()
ofrecer_bebida(menu_elegido)