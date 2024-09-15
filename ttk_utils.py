#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import tkinter as tk
from tkinter import ttk


class LabeledEntry(ttk.Frame):
	""" 
	Class that join Label and entry in a grid 
	This is a normal configuration, this class reduce lines in code.
	"""
	
	def __init__ (self, parent, text, **kwargs):
		"""
		Initializes a new instance of the LabeledEntry class.

		Parameters:
			parent (object): The parent widget of the LabeledEntry.
			text (str): The text to be displayed in the label.
			**kwargs (dict): Additional keyword arguments to configure the entry and label.

		Returns:
			None
		"""
		ttk.Frame.__init__(self,parent)
		
		self.__text = text
		self.kwargs = kwargs
		
		self.label = ttk.Label(self, text = self.__text)
		self.entry = ttk.Entry(self)
		
		if 'show' in self.kwargs:
			self.entry['show'] = self.kwargs['show']
			
		if 'state' in self.kwargs:
			self.entry['state'] = self.kwargs['state']
			self.label['state'] = self.kwargs['state']
		
		self.entry.grid(row = 0, column = 1, stick = 'WE')
		self.label.grid(row = 0, column = 0,stick = 'WE')
		
	def state (self, state):
		"""
		Set the state of the label and entry fields.

		Parameters:
			state (str): The desired state of the label and entry fields. Must be one of the following: 'normal', 'disabled', 'readonly'.

		Returns:
			None
		"""
		self.entry['state'] = state
		self.label['state'] = state
		
	def get (self):
		"""
		Returns the value of the entry field associated with this LabeledEntry instance.
		
		Returns:
			str: The value of the entry field.
		"""
		return self.entry.get()

class LabeledSpinbox(ttk.Frame):
	""" 
	Class that join Label and Spin entry into a grid
	"""
	
	def __init__ (self, parent, text, **kwargs):
		"""
		Initializes a LabeledSpinbox instance.

		Parameters:
			parent: The parent widget of the LabeledSpinbox.
			text: The text to be displayed in the label.
			**kwargs: Additional keyword arguments to configure the LabeledSpinbox.

		Returns:
			None
		"""
		ttk.Frame.__init__(self, parent)
		
		self.__text = text
		self.kwargs = kwargs
		
		self.label = ttk.Label(self, text = self.__text)
		self.spin = tk.Spinbox(self)
		
		if 'state' in self.kwargs:
			self.label['state'] = self.kwargs['state']
			self.spin['state'] = self.kwargs['state']
		
		self.label.grid(row = 0, column = 0, stick = 'WE')
		self.spin.grid(row = 0, column = 1, stick = 'WE')
	
	def state (self, state):
		"""
		Sets the state of the spinbox and its associated label.

		Parameters:
			state (str): The state to set for the spinbox and label.

		Returns:
			None
		"""
		self.spin['state'] = state
		self.label['state'] = state
	
	def get (self):
		"""
		Returns the value of the self entry.
		
		Parameters:
			None
		
		Returns:
			The value of the self entry.
		"""
		return self.entry.get()

class LabeledCombobox(ttk.Frame):
	""" Class that join Label and Spin entry into a grid	"""
	
	def __init__ (self, parent, text, **kwargs):
		"""
		Initializes a LabeledCombobox instance.

		Parameters:
			parent: The parent widget of the LabeledCombobox.
			text: The text to be displayed in the label.
			**kwargs: Additional keyword arguments to configure the Combobox and Label.

		Returns:
			None
		"""
		ttk.Frame.__init__(self, parent)
		
		self.__text = text
		self.kwargs = kwargs
		
		self.label = ttk.Label(self, text = self.__text)
		self.combo = ttk.Combobox(self)
		if 'values' in self.kwargs:
			self.combo['values'] = self.kwargs['values']
		if 'state' in self.kwargs:
			self.combo['state'] = self.kwargs['state']
			self.label['state'] = self.kwargs['state']
		
		self.combo.grid(row = 0, column = 1, stick = 'WE')
		self.label.grid(row = 0, column = 0, stick = 'WE')
	
	def state (self, state):
		"""
		Set the state of the combo box and label.

		Parameters:
		    state (str): The state to set for the combo box and label. Valid options are:
		        - 'normal': The combo box and label are enabled.
		        - 'disabled': The combo box and label are disabled.

		Returns:
		    None
		"""
		self.combo['state'] = state
		self.label['state'] = state
	
	def get (self):
		"""
		Returns the current value of the combobox.
		
		Parameters:
			None
		
		Returns:
			str: The current value of the combobox.
		"""
		return self.combo.get()
