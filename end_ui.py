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
	""" Class doc """
	
	def __init__ (self, parent):
		""" Class initialiser """
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
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		self.title('End')
		
		self._frame = End(self)
		self._frame.pack()

# ====================================================== Program Entry

def main(args):
	App = Application()
	App.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
