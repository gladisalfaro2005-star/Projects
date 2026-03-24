info_yo = {"name" : "Gladis",
"age": '20',
"adress" : 'casa',
"pets":"cat",

}
# imprimir el valor de una llave especifica
print(info_yo['pets'].title())
# imprimir llaves
print(info_yo.keys())
# imprimir valores
print(info_yo.values())
# imprimir cada llave, valor de todo el diciconario
for key, value in info_yo.items():
    print(age, 20) # (key,value)
# para variables en caso de q no existan get
print(info_yo.get("gender", ""))
