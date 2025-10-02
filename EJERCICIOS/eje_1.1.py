home = int(input("El tamaño del directorio home es: "))  # espacio en GB
var_log = int(input("El tamaño del directorio var_log es: "))  # espacio en GB

# Calcula el espacio total usado
espacio_total_usado=home+var_log

# Calcula el espacio libre (total=100GB)
espacio_libre=100-espacio_total_usado

# Muestra ambos resultados
print("El espacio total usado es: ",espacio_total_usado,"GB.")
print("El espacio libre en disco es: ",espacio_libre,"GB.")
