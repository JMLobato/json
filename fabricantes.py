import json
with open("Fabricantes.json") as fichero:
	datos=json.load(fichero)
for actividad in datos:
	print(actividad["name"])