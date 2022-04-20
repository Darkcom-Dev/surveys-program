#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import tkinter as tk
from tkinter import ttk


class LabeledEntry(ttk.Frame):
	""" Class that join Label and entry in a grid 
		This is a normal configuration, this class reduce lines in code.
	"""
	
	def __init__ (self, parent, text):
		""" Class initialiser """
		ttk.Frame.__init__(self,parent)
		
		self.__text = text
		ttk.Label(self, text = self.__text).grid(row = 0, column = 0,stick = 'WE')
		self.entry = ttk.Entry(self)
		self.entry.grid(row = 0, column = 1, stick = 'WE')
		
	def get (self):
		""" Return the self entry value """
		return self.entry.get()
