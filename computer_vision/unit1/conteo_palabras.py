words = "hola hola mundo mundo python hola gatos dia mundo".split()
print(words)

# Diccionarios
freq = {}

for w in words:
    freq[w] = freq.get(w, 0)+1

print(freq)