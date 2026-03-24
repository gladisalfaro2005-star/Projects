from pathlib import Path 
BASE = Path(__file__).resolve().parent.parent # ir saliendo de las ruras/carpeta
print(BASE) # Carpeta de mi proyecto

raw = BASE / "data" / "raw"
clean = BASE / "data" / "clean"

#creacion de carpetas
raw.mkdir(parents=True, exist_ok = True)
clean.mkdir(parents=True, exist_ok = True)

# Escribir a un archivo txt
txt_path = raw / "notas.txt"
txt_path.write_text("MiS akumnos favoritos\n Hola Yo\n \t No van a reprobar", encoding="utf-8") 