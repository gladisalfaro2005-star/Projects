# pide al usuario dinero en pesos mxn, porcentaje de iva y propina y monto total
subtotal_txt = input("Subtotal(mxn): ")
iva_txt = input("IVA(%) ej. 16: ")
propina_txt = input("Propina (%) ej. 10: ")

try:
    # metodo built in float
    subtotal = float(subtotal_txt)
    iva = float(iva_txt)/100
    propina = float(propina_txt)/100
except ValueError
    print("Entrada inválida. Utiliza números")

monto_iva = subtotal*iva
monto_propina = subtotal*propina
total = monto+monto_iva+monto_propina