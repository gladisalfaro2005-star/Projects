names = []
print(names)

# Metodo append para agregar elementos al final de la lista
names.append("Charly")
names.append("Mar")
names.append("Alexis")
names.append("Erick")
names.append("Yadira")
names.append("Arce")

print(names)
print(type(names))
print(len(names))

# metodo insert para agregar elementos en una posicion deseada
names.insert(1,"Hector")
print(names)

# Método pop() sin indice para eliminar el ultimo elemento de la lista
names.pop()
print(names)

# Método pop() con indice para eliminar un elemento deseado
names.pop(2)
print(names)

# Método remove(val) para eliminar elementos por valor
names.remove("Charly")
print(names)