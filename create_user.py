#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# ====================================================== Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# ====================================================== Classes

class CreateUser(tk.Frame):
	
	def __init__ (self, parent):
		"""
		Class initialiser.
		
		Initialises the CreateUser class with the given parent frame.
		
		Parameters:
			self (object): The instance of the class containing this method.
			parent (tkinter.Frame): The parent frame to initialise with.
		
		Returns:
			None
		"""
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
		"""
		Creates a new user by validating the provided username and password.
		
		Checks if the username and password fields are not empty, and if the password and confirmation password match.
		
		If any of the checks fail, displays an error message. Otherwise, prints a success message with the created username.
		
		Parameters:
			self (object): The instance of the class containing this method.
		
		Returns:
			None
		"""
		if self.user.get() == '':
			messagebox.showwarning(message = 'Ingrese un nombre de usuario', title = 'Error')
		elif self.password.get() == '':
			messagebox.showwarning(message = 'Ingrese una contraseña correcta', title = 'Error')
		elif self.password2.get() != self.password.get():
			messagebox.showwarning(message = 'Las contraseñas no coinciden', title = 'Error')
		else:
			print(f'Se ha creado el usuario {self.user.get()} exitosamente')

class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Initializes the Application class by calling the Tk class constructor and setting the window title.
		Sets the initial frame to an instance of the CreateUser class and packs it.

		Parameters:
		None

		Returns:
		None
		"""
		tk.Tk.__init__(self)
		self.title('Create User')
		self._frame = CreateUser(self)
		self._frame.pack()
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
