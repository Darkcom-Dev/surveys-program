
# ============================================================ Imports

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import save_ui
import sworn_declaration_ui as dj

# Ventana 2

# ============================================================ Classes

class Dwelling_basic(ttk.Frame):

	""" Dedicated interface class to living place physical direction 
	and edification use """
	
	def __init__ (self, parent):
		""" Class initialiser and main function"""
		ttk.Frame.__init__(self,parent)

		self.normalized_direction = tk.IntVar()
				
		# ~ Style Configuration
		self.font = ('Iosevka 12')
		
		# ---------------------------------------------- Dwelling Frame
		self.dwelling_frame = ttk.Labelframe(self, text = 'Información básica de la vivienda')
		self.dwelling_frame.pack(fill = tk.X, expand = True, padx = 5, pady = 5, ipady = 5)
		
		# ~ 11. normalized_direction Checkbox
		self.normalized_direction_check = ttk.Checkbutton(self.dwelling_frame, text = 'Dirección normalizada', variable = self.normalized_direction, onvalue = 1)
		self.normalized_direction_check.grid(row = 0, column = 0, columnspan = 1, sticky = 'WE', padx = 5)
		
		# ~ 12. Direction Entry
		ttk.Label(self.dwelling_frame, text = 'Dirección').grid(row = 1, column = 0, sticky = 'WE', padx = 5, pady = 5)
		self.direction_entry = ttk.Entry(self.dwelling_frame)
		self.direction_entry.configure(background = '#E8A548', foreground = '#E8A548' , font = self.font)
		self.direction_entry.grid(row = 1, column = 1, sticky = 'WE', padx = 10)

		# ~ 14. Edification use
		ttk.Label(self.dwelling_frame, text = 'Uso de la edificación').grid(row = 2, column = 0, sticky = 'WE', padx = 5, pady = 5)
		self.edification_use_combo = ttk.Combobox(self.dwelling_frame, state = 'readonly', postcommand = self.validate_edification_use)
		self.edification_use_combo.configure(font = self.font, background = '#E8A548', foreground = '#E8A548')
		self.edification_use_combo['values'] = ['Vivienda Ocupada', 'Uso Comercial', 'Vivienda Desocupada', 'Ausente']
		self.edification_use_combo.grid(row = 2, column = 1, sticky = 'WE', padx = 10)
		
		# ~ Homes amount
		ttk.Label(self.dwelling_frame, text = 'Cantidad de hogares en la vivienda').grid(row = 3, column = 0, sticky = 'WE', padx = 5, pady = 5)
		self.homes_amount_spin = tk.Spinbox(self.dwelling_frame, from_ = 0, to = 9, xscrollcommand = 12)
		self.homes_amount_spin.configure( font = self.font, background = '#5FE888', foreground = '#E8A548')
		self.homes_amount_spin.grid(row = 3, column = 1, sticky = 'WE', padx = 10)
		
		# ~ Next button
		self.next_button = ttk.Button(self, text = 'Siguiente ▶', command = lambda: self.message_data(parent)).pack(fill= tk.X, padx = 5, pady = 10)

	def validate_edification_use(self):
		
		if self.edification_use_combo.get() == 'Vivienda Desocupada' or self.edification_use_combo.get() == 'Uso Comercial':
			self.homes_amount_spin.delete(0, 'end')
			self.homes_amount_spin.insert(0, 0)
			self.homes_amount_spin.configure(state = 'disabled')
			
			print(self.edification_use_combo.get())
		elif self.edification_use_combo.get() == 'Vivienda Ocupada' or self.edification_use_combo.get() == 'Ausente':
			self.homes_amount_spin.configure(state = 'normal')
			print(self.edification_use_combo.get())
		else:
			print('Debe elegir una opción')

	def message_data (self, parent):
		""" Recoge los datos y los muestra en una ventana """
		
		if self.direction_entry.get() == '':
			message = 'La direccion no debe estar vacia'
		elif self.edification_use_combo.get() == 'Vivienda Ocupada' and self.homes_amount_spin.get() == '0':
			message = 'Una vivienda ocupada debe tener al menos un hogar'
		elif self.edification_use_combo.get() == '':
			message = 'El uso de la edificación está vacio, elige una opcion valida'
		else:
			message = f'''
Normalizada: {self.normalized_direction.get()}
Dirección: {self.direction_entry.get()}
Hogares: {self.homes_amount_spin.get()}
Uso vivienda: {self.edification_use_combo.get()}
		'''
		
		if self.direction_entry.get() == '' or self.edification_use_combo.get() == '' or (self.edification_use_combo.get() == 'Vivienda Ocupada' and self.homes_amount_spin.get() == '0'):
			messagebox.showwarning(message = message, title = 'Falta información')
		else:
			if messagebox.askyesno(message = message, title = 'Salvar información básica'):
				print('La informacion basica de vivienda ha sido guardada exitosamente') 
				save_ui.save_dwelling_basic(self.normalized_direction.get(), 
					self.direction_entry.get(), 
					self.homes_amount_spin.get(), 
					self.edification_use_combo.get()) 
				parent.switch_frame(dj.Sworn_declaration)

class Application(tk.Tk):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		self._frame = Dwelling_basic(self)
		self._frame.pack()

# ====================================================== Program Entry

def main(args):
	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
