from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import datetime
import pathlib

def timer(now, nextClass):
	print(nextClass)
	# Set up
	## Root
	root = Tk()
	root.title("Timetablet")
	root.geometry('250x90')
	root.resizable(0, 0) # False
	photo = PhotoImage(file = str(pathlib.Path(__file__).parent.absolute()) + "/icon.png")
	root.iconphoto(False, photo)
	### Gets the requested values of the height and widht.
	windowWidth = root.winfo_reqwidth()
	windowHeight = root.winfo_reqheight()
	#print("Width",windowWidth,"Height",windowHeight)
	### Gets both half the screen width/height and window width/height
	positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
	positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
	### Positions the window in the center of the page.
	root.geometry("+{}+{}".format(positionRight, positionDown))
	## Labels
	class_lbl = Label(root, text="Clase actual:{}".format(now))
	p_bar = ttk.Progressbar(root, orient='horizontal', length = 200, mode='determinate')
	## Progressbar
	p_bar['maximum'] = 100
	percentage_lbl = Label(root, text="")
	## Add
	class_lbl.pack()
	p_bar.pack()
	percentage_lbl.pack()

	def clock():
		time = datetime.datetime.now().strftime("Time: %H:%M:%S")
		print(time)
		p_bar['value'] += 1
		current_value = str(round(p_bar['value'])) + "%"
		percentage_lbl['text'] = current_value + "\nsiguiente: " + nextClass if nextClass != None else current_value
		if(p_bar['value'] == 30):
			print(showinfo("Por fin!", "Se acabo la clase :D")) 
			root.destroy()
		root.after(1000, clock) # run itself again after 1000 ms

	clock() # to update
	root.mainloop()