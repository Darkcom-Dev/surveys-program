#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2022 Braulio Madrid <darkcom@darkcom-X455LD>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
'''
CONFIGURACION DE VENTANA

dict_keys(['bd', 'borderwidth', 'class', 'menu', 'relief', 'screen', 
'use', 'background', 'bg', 'colormap', 'container', 'cursor', 'height', 
'highlightbackground', 'highlightcolor', 'highlightthickness', 'padx', 
'pady', 'takefocus', 'visual', 'width'])

TLABELFRAME
dict_keys(['relief', 'borderwidth'])

TENTRY
dict_keys(['padding', 'relief', 'fieldbackground'])

TBUTTON
dict_keys(['relief', 'padding', 'anchor', 'width', 'shiftrelief'])

TCHECKBUTTON
dict_keys(['padding', 'indicatorrelief', 'indicatorcolor'])

TRADIOBUTTON
dict_keys(['padding', 'indicatorrelief', 'indicatorcolor'])


TMENUBUTTON
dict_keys(['padding', 'relief'])

TCOMBOBOX
dict_keys(['padding', 'arrowsize'])

PROGRESSBAR
dict_keys(['background'])

TSCALE
dict_keys(['sliderrelief'])

TSCROOLBAR
dict_keys(['width', 'arrowsize'])

TREEVIEW
dict_keys(['foreground', 'background'])

TSPINBOX
dict_keys(['padding', 'arrowsize'])

desde el widget = ScrolledText dict_keys(['autoseparators', 
'background', 'bd', 'bg', 'blockcursor', 'borderwidth', 'cursor', 
'endline', 'exportselection', 'fg', 'font', 'foreground', 'height', 
'highlightbackground', 'highlightcolor', 'highlightthickness', 
'inactiveselectbackground', 'insertbackground', 'insertborderwidth', 
'insertofftime', 'insertontime', 'insertunfocussed', 'insertwidth', 
'maxundo', 'padx', 'pady', 'relief', 'selectbackground', 
'selectborderwidth', 'selectforeground', 'setgrid', 'spacing1', 
'spacing2', 'spacing3', 'startline', 'state', 'tabs', 'tabstyle', 
'takefocus', 'undo', 'width', 'wrap', 'xscrollcommand', 
'yscrollcommand'])


NO TIENEN ESTILOS
TLabel = Pero por alguna razon obedece a los estilos
TFrame = Pero obedece a algunas instrucciones
TScrolledText
TLabeledScale ???
tk.Canvas ???
tk.Listbox ???
tk.Menu ???
tk.Message ???
ttk.Notebook ???
ttk.OptionMenu ???
ttk.PanedWindow ???
ttk.Separator ???
ttk.Sizegrip ???
tk.Text ???


CONTROL TEMÁTICO	ESTILO POR DEFECTO
ttk.Button			TButton
ttk.Checkbutton		TCheckbutton
ttk.Combobox		TCombobox
ttk.Entry			TEntry
ttk.Frame			TFrame
ttk.Label			TLabel
ttk.LabeledScale	TFrame
ttk.LabelFrame		TLabelframe
ttk.Menubutton		TMenubutton
ttk.Notebook		TNotebook
ttk.PanedWindow		TPanedwindow
ttk.Progressbar		TProgressbar
ttk.Spinbox			TSpinbox
ttk.Treeview		Treeview (sin prefjio)

'''



'''
Layout Manager
.pack() = Centra el widget al centro de la ventana y va apilando verticalmente
atributos que se pueden usar son
side = LEFT, RIGHT, TOP, BOTTOM = Esto hace que el widget se posicione
fill = tk.X, tk.Y o tk.BOTH = Esto hace que el widget ocupe el espacio en la ventana
padx, pady = Deja espacio entre widgets en pixeles
ipadx, ipady = Espacio interno horizontal o vertical entre la etiqueta y el borde del widget

.grid() = El layout mas popular en tkinter, el contenido se organiza en columnas y filas
atributos que se puede usar son:
row, column, indice de la columna y la filadict_keys(['relief', 'borderwidth'])

padx, pady = espacio horizontal y vertical
columnspan = junta dos columnas como si fuera uno solo
rowspan = junta dos filas como si fuera una


root.iconifi = funcion que minimiza la ventana
root.destroy = funcion que cierra la ventana

root.resizable(True,True) = Habilita o desabilita la posibilidad de que la pantalla se amplie
root.minsize(width,height) = tamaño minimo al que la pantalla puede ser reducido
root.maxsize(width,height) = tamaño maximo al que puede ser ampliada la ventana

root.lower(*otra_ventana) = mueve la ventana abajo del stack de ventanas
root.lift(*otra_ventana) = mueve la ventana arriba del stack de ventanas
root.iconbitmap('icono.ico') # Cambia el icono de la aplicacion, debe ser .ico la extension

screen_width = root.winfo_screenwidth() = obtiene el ancho de la ventana
screen_height = root.winfo_screenheight() = obtiene la altura de la ventana

'''
	# must be -alpha, -topmost, -zoomed, -fullscreen, or -type
	# -topmost = trae la ventana siempre al frente por encima de las demas.
	# -fullscreen = maximiza la ventana a pantalla completa.
	# '-toolwindow', solo funciona en windows.os
	# ~ root.overrideredirect(1) # Elimina la pestaña principal de la ventana, ideal para splash-screens

# TEKE TEKE POOL - ANZU
# I have no name - NoTitle01

# ============================================================= Imports

import tkinter as tk
from tkinter import ttk # Los widgets de esta libreria son mas recomendables que el clasico
from tkinter import font
from tkinter import messagebox
import random

import login #0


# ============================================================= Classes



class Application(tk.Tk):
	""" Class doc """

	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)

		self.title('Sisben DNP')
		# ~ self.iconbitmap('@/pythontutorial.xbm')
		self.configure(bg = '#581B9E', relief = tk.SUNKEN)
		
		# ~ self.geometry('400x640+50+50')
		# ~ self.resizable(True, False)
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
		# ~ print(self.style.configure('TNotebook').keys())
		# ~ self.style.configure('TWidget', background = self.bg_general, foreground = self.fg_enabled, font = self.font_general)
		'''
		self.style.configure('TLabelframe', background = self.bg_general, foreground = self.fg_enabled, font = self.font_general)
		self.style.configure('TFrame', background = self.bg_widget, foreground = self.fg_enabled, font = self.font_general)
		self.style.configure('TLabel', background = self.bg_widget, foreground = self.fg_enabled, font = self.font_general)
		self.style.configure('TEntry', bg = self.bg_widget, foreground = self.fg_enabled, font = ('G15 12'))
		self.style.configure('TButton', background = self.bg_widget, foreground = self.fg_enabled, font = 'G15')
		self.style.configure('TCheckbutton', background = self.bg_widget, foreground = self.fg_enabled, font = self.font_general)
		self.style.configure('TCombobox', background = self.bg_widget, foreground = self.fg_enabled, font = self.font_general) # Esto modifica la flecha de despliegue
		self.style.configure('TSpinbox', background = self.bg_widget, foreground = self.fg_enabled, font = self.font_general)
		self.style.configure('Text', font = self.font_general, background = '#8631E8', foreground = '#5FE888')
		'''
		# --------------------------------------------------------------

		self._frame = None
		self.switch_frame(login.Login)

	def switch_frame(self, frame_class):
		new_frame = frame_class(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()

# =========================================================== Functions

def main(args):
	print(args)
	App = Application()
	App.mainloop()
	return 0

# ======================================================= Entry program

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))


