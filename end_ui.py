#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# ====================================================== Imports

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttk_utils as ttku
# ====================================================== Classes

class End(ttk.Frame):
	
	def __init__ (self, parent):
		"""
		Initialises the End class.
		
		Parameters:
			parent: The parent widget.
		
		Returns:
			None
		"""
		tk.Frame.__init__(self, parent)
		
		self.password = ttku.LabeledSpinbox(self,'Visita número: ')
		self.password.pack(fill = tk.X)
		
		options = ['Completa', 'Incompleta', 'Ocupado', 'Ausencia de informante calificado', 'Nadie en el hogar','Rechazo', 'Otro motivo']
		self.combo_ex = ttku.LabeledCombobox(self, 'Resultado de entrevista: ', values = options)
		self.combo_ex.pack(fill = tk.X)
		
		ttk.Button(self, text = 'Terminar', command = self.end_survey).pack(fill = tk.X)
		
	def end_survey(self):
		print('Encuesta terminada')
			
		

class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Initialises the Application class by calling the Tk class constructor, setting the window title, 
		creating an instance of the End class, and packing it into the window.
		"""
		tk.Tk.__init__(self)
		self.title('End')
		
		self._frame = End(self)
		self._frame.pack()

# ====================================================== Program Entry

def main():
	"""
	Program entry point.

	Initializes the Application class and starts the Tkinter event loop.
	
	Returns:
		int: Exit status of the application.
	"""
	App = Application()
	App.mainloop()
	return 0

if __name__ == '__main__':
	main()
