"""
    Este programa pide al usuario su pin de acceso.
   
    1) Si es pin es correcto, el programa debe decirles 
    autenticación exitosa, acceso concedidio.

    2) Si el pin es incorrecto, entonces el programa debe 
    decirle al usario pin incorrecto y el número de intentos 
    que le quedan.

    3) Si el usuario supera el número de intentos permitidos,
    entonces el programa le va a decir número de intentos
    superados y cuenta bloqueada.
"""
PIN_CORRECTO = "superdificil"
INTENTOS_MAX = 3
intentos = 0

while intentos < INTENTOS_MAX:
    entrada = input("Ingresa tu pin (4 dígitos)")
    if entrada == PIN_CORRECTO:
        print("Autenticación exitosa.") 
        print("Acceso concedido.")
        break
    else:
        intentos += 1
        restantes = INTENTOS_MAX - intentos
        if restantes > 0:
            print("Pin incorrecto. Te quedan  {restantes}  intentos.")
        else: 
            print("Pin incorrecto. Cuenta bloqueada")