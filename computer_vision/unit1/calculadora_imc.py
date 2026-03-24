weight_txt = input("Peso (kg): ")
height_txt = input("Altura (m): ")

try:
    weight = float(weight_txt)
    height = float(height_txt)
    imc = weight / (height ** 2)
    print(f"Tu IMA es {imc}")
except (ValueError):
    print("Datos inválidos. Ej.: peso 70.5, altura 1.75")
except ZeroDivisionError:
    print("Error. NO esta permitida la división por zero")
