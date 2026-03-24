def normalize_name(txt):
    """
        Esta función normaliza strings.
        Lo que hace es quitar espacios en blanco 
        al inicio y fin de mi string,
        elimina los espacios en blanco y acomoda 
        el nombre en titulo.
          :params(str): texto de entrada
          :return: texto formateado
    """
    return " ".join(txt.strip().title().split())

def to_mxn(valor, tasa: float=1.0): # Tasa es un parametro opcional
    """
        Convierte un valor a MXN multiplicando por la tasa.
    """
    return float(valor)*float(tasa)