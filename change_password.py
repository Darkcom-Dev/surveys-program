#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# ====================================================== Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# ====================================================== Classes

class ChangePassword(tk.Frame):
	""" Class doc """
	
	def __init__ (self, parent):
		""" Class initialiser """
		tk.Frame.__init__(self,parent)
		ttk.Label(self, text = 'Cambiar contraseña').pack()

class Application(tk.Tk):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		self.title('Cambiar contraseña')
		self._frame = ChangePassword(self)
		self._frame.pack()

# ====================================================== Program Entry
def main(args):
	'''
	Cuando ya se haya autenticado un usuario, una de las opciones que 
	podrá tomar es la de cambiar la contraseña y para eso es este módulo
	
	'''
	
	App = Application()
	App.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
