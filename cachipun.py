from random import choice
opciones = ["piedra","papel","tijera"]

#pedir valor al usuario
seleccion_usuario = input("Ingresa el valor: ").lower()

if seleccion_usuario not in opciones:
    print("Dato erroneo.....")
else:
    seleccion_computador = choice(opciones)
    
    if seleccion_usuario == seleccion_computador:
        print(f"Usuario: {seleccion_usuario} - Computador: {seleccion_computador}\nResultado: Empate")
    
    elif(seleccion_usuario == "papel" and seleccion_computador == "piedra") or \
        (seleccion_usuario == "piedra" and seleccion_computador == "tijera") or \
        (seleccion_usuario == "tijera" and seleccion_computador == "papel"):
            print(f"Usuario: {seleccion_usuario} - Computador: {seleccion_computador}\nResultado: Victoria")
    else:
        print(f"Usuario: {seleccion_usuario} - Computador: {seleccion_computador}\nResultado: Derrota")