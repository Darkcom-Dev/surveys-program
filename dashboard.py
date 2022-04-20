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
	""" Class doc """
	
	def __init__ (self, parent):
		""" Class initialiser """
		tk.Frame.__init__(self, parent)
		
		ttk.Label(self, text = 'Opciones').pack(fill = tk.X)
		
		ttk.Button(self, text = 'Iniciar encuesta', command = lambda : parent.switch_frame(iub.Location)).pack(fill = tk.X)
		ttk.Button(self, text = 'Cambiar contraseña', command = lambda : parent.switch_frame(change_password.ChangePassword)).pack(fill = tk.X)
		ttk.Button(self, text = 'Crear nuevo usuario', command = lambda : parent.switch_frame(create_user.CreateUser)).pack(fill = tk.X)
		ttk.Button(self, text = 'Cerrar sesión', command = lambda : parent.switch_frame(login.Login)).pack(fill = tk.X)
		ttk.Button(self, text = 'Cargar Divipola', command = self.open_file).pack(fill = tk.X)

	def open_file (self):
		""" Function doc """
		filetypes = (('text files', '*.json'),('All files', '*.*'))
		filename = fd.askopenfilename(title = 'Abrir divipola', filetypes = filetypes)
		
		messagebox.showinfo(title = 'Estado divipola', message = f'ha sido cargado {filename} exitosamente.')
		
		save_ui.save_config(filename)
		save_ui.load_config()

class Application(tk.Tk):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		self.title('Dashboard')
		self._frame = Dashboard(self)
		self._frame.pack()

# ====================================================== Program Entry

def main(args):
	App = Application()
	App.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
