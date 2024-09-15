#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# ============================================================= Imports

import tkinter as tk
from tkinter import ttk
import login #0

# ============================================================= Classes


class Application(tk.Tk):

	def __init__ (self):
		"""
		Class initialiser.

		Initialises the Application class by setting the title, background colour, 
		and transparency of the window. It also sets various style attributes such 
		as colours, font, and relief. Additionally, it sets the initial frame to None 
		and switches to the login frame.

		Parameters:
			self: The instance of the Application class.

		Returns:
			None
		"""
		tk.Tk.__init__(self)

		self.title('Sisben DNP')
		self.configure(bg = '#581B9E', relief = tk.SUNKEN)
		self.attributes('-alpha', 0.5)
		
		# ------------------------------------------------------ Styles
		self.bg_general = '#581B9E'
		self.bg_widget = '#8631E8'
		self.fg_disabled = '#9C6821'
		self.fg_enabled = '#E8A548'
		self.other_color = '#5FE888'

		self.font_general = tk.font.Font(family = 'JetBrainsMono Nerd Font Mono', size = 12, weight = 'bold')

		self.relief = tk.FLAT

		self.style = ttk.Style()
		
		# --------------------------------------------------------------

		self._frame = None
		self.switch_frame(login.Login)

	def switch_frame(self, frame_class):
		"""
		Switches the current frame to a new one of the given class.

		Parameters:
			frame_class (class): The class of the new frame to switch to.

		Returns:
			None
		"""
		new_frame = frame_class(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()

# =========================================================== Functions

def main(args):
	"""
	Entry point of the application.

	Parameters:
		args (list): A list of command line arguments.

	Returns:
		int: The exit status of the application.
	"""
	print(args)
	App = Application()
	App.mainloop()
	return 0

# ======================================================= Entry program

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))


