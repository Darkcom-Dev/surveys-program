#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# ====================================================== Imports

import tkinter as tk
from tkinter import messagebox, ttk

import autentication
import dashboard
import ttk_utils as ttku

# ====================================================== Classes

class Login(ttk.Frame):
	
	def __init__ (self, parent):
		"""
		Class initialiser.

		Initialises the Login class with the given parent frame.

		Parameters:
			parent (tkinter.Frame): The parent frame to initialise with.

		Returns:
			None
		"""
		tk.Frame.__init__(self, parent)
		
		self.user = ttku.LabeledEntry(self,'_Usuario: ')
		self.user.pack(fill = tk.X)
		# ~ options = {'show':'*'}
		
		self.password = ttku.LabeledEntry(self,'Password: ', show = '*')
		self.password.pack(fill = tk.X)
		
		options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
		self.combo_ex = ttku.LabeledCombobox(self, 'Opciones: ', values = options)
		self.combo_ex.pack(fill = tk.X)
		
		ttk.Button(self, text = 'Siguiente', command = lambda: self.authenticate_password(parent)).pack(fill = tk.X)
		
	def authenticate_password(self, parent):
		"""
		Authenticates the user's password.

		Parameters:
			parent: The parent frame to switch to upon successful authentication.

		Returns:
			None
		"""
		if self.user.get() == '':
			messagebox.showwarning(message = 'Ingrese el usuario', title = 'Error')
		elif self.password.get() == '':
			messagebox.showwarning(message = 'Ingrese la contraseña', title = 'Error')
		else:
			if autentication.authenticate_password(self.user.get(), self.password.get()):
				messagebox.showinfo(message = 'Autenticacion exitosa', title = 'Login')
				parent.switch_frame(dashboard.Dashboard)
			else:
				messagebox.showinfo(message = 'Autenticacion fallida', title = 'Login')
			
		

class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Initialises the Application class by calling the Tk class constructor and setting the window title.
		Sets the initial frame to an instance of the Login class and packs it with the dashboard.
		"""
		tk.Tk.__init__(self)
		self.title('Login')
		
		self._frame = Login(self)
		self._frame.pack(dashboard.Dashboard)

# ====================================================== Program Entry

def main():
	"""
	Entry point of the application.

	Parameters:
		None

	Returns:
		int: The exit status of the application.
	"""

	App = Application()
	App.mainloop()
	return 0

if __name__ == '__main__':
	main()
