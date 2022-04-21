#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import tkinter as tk
from tkinter import ttk


class LabeledEntry(ttk.Frame):
	""" Class that join Label and entry in a grid 
		This is a normal configuration, this class reduce lines in code.
	"""
	
	def __init__ (self, parent, text, **kwargs):
		""" Class initialiser """
		ttk.Frame.__init__(self,parent)
		
		self.__text = text
		self.kwargs = kwargs
		ttk.Label(self, text = self.__text).grid(row = 0, column = 0,stick = 'WE')
		
		self.entry = ttk.Entry(self)
		if 'show' in self.kwargs:
			self.entry['show'] = self.kwargs['show']
		self.entry.grid(row = 0, column = 1, stick = 'WE')
		
	def get (self):
		""" Return the self entry value """
		return self.entry.get()

class LabeledSpinbox(ttk.Frame):
	""" Class that join Label and Spin entry into a grid
	"""
	
	def __init__ (self, parent, text, **kwargs):
		""" Function doc """
		ttk.Frame.__init__(self, parent)
		
		self.__text = text
		
		ttk.Label(self, text = self.__text).grid(row = 0, column = 0, stick = 'WE')
		self.entry = tk.Spinbox(self)
		
		self.entry.grid(row = 0, column = 1, stick = 'WE')
	
	def get (self):
		""" Function doc """
		return self.entry.get()

class LabeledCombobox(ttk.Frame):
	""" Class that join Label and Spin entry into a grid
	"""
	
	def __init__ (self, parent, text, **kwargs):
		""" Function doc """
		ttk.Frame.__init__(self, parent)
		
		self.__text = text
		self.kwargs = kwargs
		
		ttk.Label(self, text = self.__text).grid(row = 0, column = 0, stick = 'WE')
		self.entry = ttk.Combobox(self)
		if 'values' in self.kwargs:
			self.entry['values'] = self.kwargs['values']
		self.entry.grid(row = 0, column = 1, stick = 'WE')
	
	def get (self):
		""" Function doc """
		return self.entry.get()
