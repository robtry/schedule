from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
# import datetime
import pathlib

def timer(subject, nextClass=None, duration=90):
	# Set up
	## Root
	root = Tk()
	root.title("Timetablet")
	root.geometry('300x90')
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
	class_lbl = Label(root, text=subject)
	p_bar = ttk.Progressbar(root, orient='horizontal', length = 200, mode='determinate')
	## Progressbar
	p_bar['maximum'] = 100
	percentage_lbl = Label(root, text="0%")
	## Add to the main frame
	class_lbl.pack()
	p_bar.pack()
	percentage_lbl.pack()

	# update method
	step = 100 / duration
	# print(step)
	def clock():
		# time = datetime.datetime.now().strftime("Time: %H:%M:%S")
		# print(time)
		p_bar['value'] += step
		current_value = str(round(p_bar['value'])) + "%"
		percentage_lbl['text'] = current_value + "\n" + nextClass if nextClass != None else current_value
		if(p_bar['value'] >= 100):
			print(showinfo("Por fin!", "Se acabo la clase :D")) 
			root.destroy()
		root.after(1000 * 60, clock) # run itself again after 1000 * 60 ms

	clock() # to update
	root.mainloop()