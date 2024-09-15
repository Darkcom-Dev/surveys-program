#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ethnicity.py
#  
# ~ 1.1 ¿A cual grupo indigena pertenece?
# ~ 1.2. ¿A cual clan pertnece?
		
# ~ 2.1 ¿A cual vitsa pertenece?
# ~ 2.2 ¿A cual kumpania pertenece?
		
# ~ 38. ¿... Habla la lengua nativa de su pueblo?
# ~ 38.1 ¿Habla otras lenguas nativas?

import tkinter as tk
from tkinter import ttk
import ttk_utils as ttku

class Ethnicity(tk.Toplevel):
	""" Class that get Ethnicity info of a person """
	
	def __init__ (self):
		"""
		Class initialiser.

		Initialises the Ethnicity class by setting up the necessary UI elements 
		to collect information about a person's ethnicity, including their 
		indigenous group, clan, native language, and other languages spoken.

		Parameters:
			self: The instance of the Ethnicity class.

		Returns:
			None
		"""
		super().__init__()
		
		self.ethnicity = 'pueblo indigena','vitsa'
		self.clan = 'clan','kumpania'
		
		self.ethnicity_entry = ttku.LabeledEntry(self,text = f'¿A cual {self.ethnicity[0]} pertenece?'.center(35,'.'))
		self.ethnicity_entry.state('disabled')
		
		self.ethnicity_entry.pack()
		
		self.clan_entry = ttku.LabeledEntry(self,text = f'¿A cual {self.clan[0]} pertenece?'.center(35,'.'))
		self.clan_entry.pack()
		
		self.native_language = tk.IntVar()
		self.native_language_check = ttk.Checkbutton(self,text = '¿Habla la lengua nativa de su pueblo?', variable = self.native_language)
		self.native_language_check.pack(fill = tk.X, padx = 5, pady = 5)
		
		self.understand_language = tk.IntVar()
		self.understand_language_check = ttk.Checkbutton(self,text = '¿Entiende la lengua nativa de su pueblo?', variable = self.understand_language)
		self.understand_language_check.pack(fill = tk.X, padx = 5, pady = 5)
		
		self.other_languages = tk.IntVar()
		self.other_languages_check = ttk.Checkbutton(self,text = '¿Habla otras lenguas nativas?', variable = self.other_languages)
		self.other_languages_check.pack(fill = tk.X, padx = 5, pady = 5)
		
		self.amounts_spin = ttku.LabeledSpinbox(self, text = 'Cuantas: '.center(35, '.'), state = 'disabled')
		self.amounts_spin.pack(fill = tk.X, padx = 5, pady = 5)
		
		self.close_button = ttk.Button(self, text = 'Cerrar', command = self.update).pack(fill = tk.X, padx = 5, pady = 5)
		
	def update (self):
		"""
		Updates the state of the understand language check and amounts spin based on the native language and other languages checkboxes.
		
		Triggers the update function to be called again after a 1000ms delay.
		
		Parameters:
			None
		
		Returns:
			None
		"""
		self.amounts_spin.after(1000, self.update)

		self.understand_language_check['state'] = tk.NORMAL if self.native_language.get() == 1 else tk.DISABLED
		self.amounts_spin.state(tk.NORMAL if self.other_languages.get() == 1 else tk.DISABLED)

class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Initializes the Ethnicity application by calling the constructor of the tk.Tk class and creating an instance of the Ethnicity class. 

		Parameters:
		None

		Returns:
		Nothing
		"""
		tk.Tk.__init__(self)
		self._frame = Ethnicity()
		# ~ self._frame.pack()

def main():
	"""
	Entry point of the application.

	Parameters:
		None

	Returns:
		int: The exit status of the application.
	"""
	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	main()
