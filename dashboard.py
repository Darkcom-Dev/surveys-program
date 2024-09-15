#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# ====================================================== Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

import change_password
import create_user
import login
import location_ui as iub
import save_ui
# ====================================================== Classes

class Dashboard(ttk.Frame):
	
	def __init__ (self, parent):
		"""
		Class initialiser for the Dashboard class.

		Initialises a new instance of the Dashboard class with the given parent.
		Sets up the layout of the dashboard with various buttons for different actions.

		Parameters:
			self: A reference to the current instance of the class.
			parent: The parent widget of the dashboard.

		Returns:
			None
		"""
		tk.Frame.__init__(self, parent)
		
		ttk.Label(self, text = 'Opciones').pack(fill = tk.X)
		
		ttk.Button(self, text = 'Iniciar encuesta', command = lambda : parent.switch_frame(iub.Location)).pack(fill = tk.X)
		ttk.Button(self, text = 'Cambiar contraseña', command = lambda : parent.switch_frame(change_password.ChangePassword)).pack(fill = tk.X)
		ttk.Button(self, text = 'Crear nuevo usuario', command = lambda : parent.switch_frame(create_user.CreateUser)).pack(fill = tk.X)
		ttk.Button(self, text = 'Cerrar sesión', command = lambda : parent.switch_frame(login.Login)).pack(fill = tk.X)
		ttk.Button(self, text = 'Cargar Divipola', command = self.open_file).pack(fill = tk.X)

	def open_file (self):
		"""
		Opens a file dialog for the user to select a Divipola file.

		Parameters:
			self: A reference to the current instance of the class.

		Returns:
			None
		"""
		filetypes = (('text files', '*.json'),('All files', '*.*'))
		filename = fd.askopenfilename(title = 'Abrir divipola', filetypes = filetypes)
		
		messagebox.showinfo(title = 'Estado divipola', message = f'ha sido cargado {filename} exitosamente.')
		
		save_ui.save_config(filename)
		save_ui.load_config()

class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Class initialiser for the Application class.

		Initialises the Application class by calling the Tk class constructor and setting the window title.
		Sets the initial frame to an instance of the Dashboard class and packs it.
		"""
		tk.Tk.__init__(self)
		self.title('Dashboard')
		self._frame = Dashboard(self)
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
