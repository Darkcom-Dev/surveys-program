# ============================================================ Imports

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import dwelling_data_ui as idv
import end_ui
# Ventana 3

# ============================================================ Classes

class Sworn_declaration(ttk.Frame):
	""" 
	An dedicated class interface to sworn_declaration and data processing
	"""
	
	def __init__ (self,parent):
		"""
		Initialises the Sworn_declaration class.

		Parameters:
			self (Sworn_declaration): The instance of the class.
			parent: The parent widget of the current instance.

		Returns:
			None
		"""
		ttk.Frame.__init__(self, parent)
		
		self.font = ('Iosevka 10')
		
		self.st = ScrolledText(self, width = 50, height = 33)
		# ~ self.st.configure(font = self.font, background = '#8631E8', foreground = '#5FE888')
		
		self.sworn_declaration = open('assets/declaracion_juramentada.txt','r')
		self.data_treatment = open('assets/uso_tratamiento_datos.txt', 'r')
		
		self.st.insert('1.0',self.data_treatment.read())
		self.st.insert('1.0',self.sworn_declaration.read()) 
		self.st['state'] = 'disabled'
		self.st.grid(column = 0, row = 0, columnspan = 2, padx = 10, pady = 5, sticky = 'WE')
		
		self.refuse_button = ttk.Button(self, text = 'No Acepto', command = lambda: parent.switch_frame(end_ui.End))
		self.refuse_button.grid(row = 1, column = 0, sticky = 'WE')
		self.accept_button = ttk.Button(self, text = 'Acepto', command = lambda: parent.switch_frame(idv.Dwelling_data))
		self.accept_button.grid(row = 1, column = 1, sticky = 'WE')
		
		self.sworn_declaration.close()
		self.data_treatment.close()
		


class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Class initialiser for the Application class.

		Initialises the Application object by calling the tk.Tk class initialiser 
		and setting the _frame attribute to a Sworn_declaration object.
		"""
		tk.Tk.__init__(self)
		self._frame = Sworn_declaration(self)
		self._frame.pack()

# ====================================================== Program Entry

def main():
	"""
	Program entry point.

	Initializes the Application class and starts the main event loop.
	
	:return: int: The program's exit status.
	"""
	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	main()
