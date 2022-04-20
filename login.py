#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


# ====================================================== Imports

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import autentication
import ttk_utils as ttku
import dashboard
# ====================================================== Classes



class Login(ttk.Frame):
	""" Class doc """
	
	def __init__ (self, parent):
		""" Class initialiser """
		tk.Frame.__init__(self, parent)
		
		self.user = ttku.LabeledEntry(self,'_Usuario: ')
		self.user.pack(fill = tk.X)
		self.password = ttku.LabeledEntry(self,'Password: ')
		self.password.pack(fill = tk.X)
		
		ttk.Button(self, text = 'Siguiente', command = lambda: self.authenticate_password(parent)).pack(fill = tk.X)
		
	def authenticate_password(self, parent):
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
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		self.title('Login')
		
		self._frame = Login(self)
		self._frame.pack(dashboard.Dashboard)

# ====================================================== Program Entry

def main(args):
	App = Application()
	App.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
