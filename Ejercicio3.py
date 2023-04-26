# Peso y estatura usuario
peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

# Indice masa corporal
imcp = peso / (estatura ** 2)

# Redondeamos el resultado a dos decimales
imcp = round(imcp, 2)

# Imprimimos el resultado por pantalla
print("Tu índice de masa corporal es:", imcp)
