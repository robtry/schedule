import os

def reminder(subject, classroom, kind, schedule, tag="*", check=True):

	def checkRTM():
		location_rtm = os.popen('which rtm').read().strip()
		# print(location_rtm)
		if(len(location_rtm) == 0):
			print("first install", "https://github.com/dwaring87/rtm-cli")
			return False
		return location_rtm

	rtm = checkRTM()
	print("timetable by rob")
	print("*************************************")
	print("*********** PRÓXIMA CLASE ***********")
	print("*************************************")
	print("=====================================")
	print("Clase: ", subject)
	print("Salón: ", classroom)
	print("Tipo: ", kind)
	print(schedule)
	print("=====================================")
	if check and rtm:
		print("TAREAS REGISTRADAS:")
		os.system(rtm + " ls | grep " + tag )
		print("========================")
		#os.system(rtm + " planner")
		#print("========================")
	else:
		print("Can not run rtm")
	input()
