print("Este prorama captura importes")
info = """
             CALCULA TU SUMA
    Este programa lleva el conteo de cuantos importes ha introducido un usuario.

    Va acumulando todos los importes que el usuario ingresa.

    Si el usuario desea terminar el programa puede escribir en cualquier momento la palabra quit, exit, terminar.

                                               Gladis
"""
print(info) 
conteo = 0
suma = 0.0
minimo = None
maximo = None

while True:
    user_mesage = """
    Ingresa tu importe (MXN)
    Si quieres dejar de capturar importes
    puedes ingresar en cualquier momento
    exit, quit, terminar.
    """
    line = input(user_mesage).lower()
    if line == "exit" or line == "quit" or line == "terminar":
        break
    try:
        value = float(line)
    except ValueError:
        print("Valor inválido. Intenta con números 0.0")
        continue
    conteo += 1 # cuantos numeros he ingresad0
    suma += value # acumulación

    if minimo is None or value < minimo:
        minimo = value 

    if maximo is None or value > maximo:
        maximo = value

if conteo == 0:
    print("No se capturaron importes")
else:
    print("="*32)
    print("La cantidad de números ingresados es: ", f"{conteo}")
    print("La sumatoría de todos los números es: ", f"{suma}")
    print("El mínimo es: ", f"{minimo}")
    print("El máximo es: ", f"{maximo}")

print("Programa finalizado")