import os
import sys

def base(clase, salon, edificio, tipo, horario, tag="", check=True):
	rtm = "/home/rob/.nvm/versions/node/v12.7.0/bin/rtm"
	print("*************************************")
	print("*********** PRÓXIMA CLASE ***********")
	print("*************************************")
	print("=====================================")
	print("Clase: ", clase)
	print("Edificio: ", edificio)
	print("Salón: ", salon)
	print("Tipo: ", tipo)
	print(horario)
	print("=====================================")
	if check:
		print("TAREAS REGISTRADAS:")
		os.system(rtm + " ls | grep " + tag )
		print("========================")
	os.system(rtm + " planner")
	print("========================")
	input()

if __name__ == "__main__":
	# print(sys.argv[1])
	materia = sys.argv[1]

	if materia == "redes":
		base("Fundamentos de Redes", "A6", "106", "Teórica", "8:30 - 10:00", "redes")
	elif materia == "redes_lab":
		base("Fundamentos de Redes", "CDT-1", "04L05", "Práctica", "2:00 - 3:00", "redes")
	elif materia == "evap":
		base("Español", "A5", "201", "Teórica", "10:00 - 11:30", "evap")
	elif materia == "ingles":
		base("Inglés", "A6", "103", "Teórica", "11:30 - 1:00", "ingles")
	elif materia == "ingles_corto":
		base("Inglés", "A6", "103", "Teórica corta", "11:30 - 12:30", "ingles")
	elif materia == "swim":
		base("Nado", "", "", "", "13:30 - 14:30", check=False)
	elif materia == "salsa":
		base("Salsa", "A3", "203", "Bailongo", "9:00 - 10:00", check=False)
	elif materia == "database":
		base("Base de Datos", "CDT-1", "05L01", "Teórica y Práctica", "1:00 - 2:30", "database")
	elif materia == "progra":
		base("Programación Avanzada", "A5", "103", "Teórica y Práctica", "7:00 - 10:00", "progra")
	elif materia == "algebra":
		base("Algebra Lineal", "A5", "311", "Teórica", "10:00 - 1:00", "algebra")
	elif materia == "mentor":
		base("Peer Mentor", "A5", "302", "Pendeja", "4:00 - 5:30", "mentor")
	else:
		print("Wtf no existe el caso")