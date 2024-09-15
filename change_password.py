#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# ====================================================== Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# ====================================================== Classes

class ChangePassword(tk.Frame):
	
	def __init__ (self, parent):
		"""
		Class initialiser.
		
		Initialises the ChangePassword class with the given parent frame.
		
		Parameters:
			self (object): The instance of the class containing this method.
			parent (tkinter.Frame): The parent frame to initialise with.
		
		Returns:
			None
		"""
		tk.Frame.__init__(self,parent)
		ttk.Label(self, text = 'Cambiar contraseña').pack()

class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Class initialiser.

		Initialises the Application class by calling the Tk class constructor and setting the window title.
		Sets the initial frame to an instance of the ChangePassword class and packs it.

		Parameters:
			None

		Returns:
			None
		"""
		tk.Tk.__init__(self)
		self.title('Cambiar contraseña')
		self._frame = ChangePassword(self)
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
