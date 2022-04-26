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
		""" Function doc """
		self.entry['state'] = state
		self.label['state'] = state
		
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
		self.kwargs = kwargs
		
		self.label = ttk.Label(self, text = self.__text)
		self.spin = tk.Spinbox(self)
		
		if 'state' in self.kwargs:
			self.label['state'] = self.kwargs['state']
			self.spin['state'] = self.kwargs['state']
		
		self.label.grid(row = 0, column = 0, stick = 'WE')
		self.spin.grid(row = 0, column = 1, stick = 'WE')
	
	def state (self, state):
		""" Function doc """
		self.spin['state'] = state
		self.label['state'] = state
	
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
		""" Function doc """
		self.combo['state'] = state
		self.label['state'] = state
	
	def get (self):
		""" Function doc """
		return self.combo.get()
