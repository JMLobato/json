import json
with open("Fabricantes.json") as fichero:
	datos=json.load(fichero)
cont=0
#1º Apartado
for actividad in datos:
	print(actividad["name"])
	cont+=1
#2º Apartado
print("Hay %d actividades"%cont)