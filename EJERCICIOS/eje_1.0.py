home = 30  # espacio en GB
var_log = 12  # espacio en GB

# Calcula el espacio total usado
espacio_total_usado=home+var_log

# Calcula el espacio libre (total=100GB)
espacio_libre=100-espacio_total_usado

# Muestra ambos resultados
print(espacio_total_usado)
print(espacio_libre)

