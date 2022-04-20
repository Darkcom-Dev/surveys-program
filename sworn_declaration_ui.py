# ============================================================ Imports

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import dwelling_data_ui as idv
# Ventana 3

# ============================================================ Classes

class Sworn_declaration(ttk.Frame):
	""" Clase de interfaz dedicada a la sworn_declaration juramentada y 
	tratamiento de datos """
	
	def __init__ (self,parent):
		""" Class initialiser """
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
		print(tk.Misc.winfo_class(self.st))
		
		self.refuse_button = ttk.Button(self, text = 'No Acepto', command = self.destroy)
		self.refuse_button.grid(row = 1, column = 0, sticky = 'WE')
		self.accept_button = ttk.Button(self, text = 'Acepto', command = lambda: parent.switch_frame(idv.Dwelling_data))
		self.accept_button.grid(row = 1, column = 1, sticky = 'WE')
		
		self.sworn_declaration.close()
		self.data_treatment.close()
		
	def accept_action (self):
		""" Action for accept button """
		print('Accept Action')
		
	def refuse_action(self):
		'''Action for refuse button
		Hacer una ventana en comun si rechaza la entrevista.
		'''
		print('Refuse Action')

class Application(tk.Tk):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		self._frame = Sworn_declaration(self)
		self._frame.pack()

# ====================================================== Program Entry

def main(args):
	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
