csv_file = open('./data.csv', 'r', encoding='utf-8') #Leo el archivo data.py
data = [[int(d) if d[0] in '0123456789' else d.lower() for d in new_line.split(',')] for new_line in csv_file.read().strip().split('\n')][1:] #Formateo los datos para tener el nombre de la capital y la aptitud como str y el resto de datos como int
csv_file.close() #Cierro el archivo
ciudad = input().lower() #Obtengo el nombre de una ciudad
c = [] #Es para guardar los datos de la altura y la profundidad de la ciudad seleccionada
aptitud = {'sumamente': 0, 'moderadamente': 0, 'marginalmente': 0, 'no': 0} #Es para el conteo de la aptitud de la ciudad seleccionada
for d in data: #Inicio el recorrido de todos los datos del archivo
    if d[0] != ciudad: #Si no es la cuidad seleccionada ignorar sus datos
        continue
    c.append([d[2], d[5]]) #d[2]: altura sobre el nivel del mar, d[5]: profundidad efectiva del suelo
    aptitud[d[6].split(' ')[0]] += 1 #contar la aptitud
print(f'{sum([msnm[0] for msnm in c])/len(c):.2f} {sum([msnm[1] for msnm in c])/len(c):.2f}\n{min([msnm[0] for msnm in c])} {min([msnm[1] for msnm in c])}\n{max([msnm[0] for msnm in c])} {max([msnm[1] for msnm in c])}') #Calculo e imprimo el promedio, min y max de los datos altura y profundidad
while len(aptitud) != 0: #Se repetirá hasta que se impriman las cuatro aptitudes
    for j in sorted(aptitud): #Recorro las aptitudes en forma ordenada
        if aptitud[j] == max(list(aptitud.values())): #Verifico si la aptitud actual es la mayor
            print(f'{j} apto {aptitud[j]}') #Imprimo la aptitud y cuantas veces aparecio
            aptitud.pop(j) #Elimino la aptitud para no volver a evaluarla
