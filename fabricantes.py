import json
with open("Fabricantes.json") as fichero:
	datos=json.load(fichero)
cont=0
#1º Apartado
for actividad in datos:
	print(actividad["name"])
	cont+=1
print()
#2º Apartado
print("Hay %d actividades"%cont)
print()
#3º Apartado
fecha=input("Introduce una fecha separada por guiones y empezando por el año: ")
for fechi in datos:
	if str(fechi["date"][0])==str(fecha):
		print(fechi["name"])
print()
#4º Apartado
Area=input("Introduce un area: ")
for areas in datos:
	for area in areas["areas"]:
		if area["name"].upper() == Area.upper():
			print(areas["name"])