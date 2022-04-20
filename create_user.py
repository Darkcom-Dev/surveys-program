#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# ====================================================== Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# ====================================================== Classes

class CreateUser(tk.Frame):
	""" Class doc """
	
	def __init__ (self, parent):
		""" Class initialiser """
		tk.Frame.__init__(self, parent)
		
		ttk.Label(self, text = 'Nuevo usuario').pack()
		self.user = ttk.Entry(self)
		self.user.pack()
		
		ttk.Label(self, text = 'Contraseña').pack()
		self.password = ttk.Entry(self)
		self.password.pack()
		
		ttk.Label(self, text = 'Confirmar contraseña').pack()
		self.password2 = ttk.Entry(self)
		self.password2.pack()
		
		ttk.Button(self, text = 'Crear Usuario', command = self.create_user).pack()
		
	def create_user (self):
		""" Function doc """
		if self.user.get() == '':
			messagebox.showwarning(message = 'Ingrese un nombre de usuario', title = 'Error')
		elif self.password.get() == '':
			messagebox.showwarning(message = 'Ingrese una contraseña correcta', title = 'Error')
		elif self.password2.get() != self.password.get():
			messagebox.showwarning(message = 'Las contraseñas no coinciden', title = 'Error')
		else:
			print(f'Se ha creado el usuario {self.user.get()} exitosamente')

class Application(tk.Tk):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		self.title('Create User')
		self._frame = CreateUser(self)
		self._frame.pack()
# ====================================================== Program Entry

def main(args):
	App = Application()
	App.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
