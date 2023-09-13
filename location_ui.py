
# ============================================================= Imports

import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import georeference_ui as igeo
import save_ui

# Ventana 0

# ============================================================= Classes

class Location(ttk.Frame):
	""" Class doc """
	
	def __init__ (self, parent):
		""" Class initialiser """
		ttk.Frame.__init__(self, parent)

		self.font = ('Iosevka 11')
		
		# --------------------------------------------------Ticket Frame
		self.ticket_frame = ttk.LabelFrame(self, text = 'Informacion de la ficha')
		self.ticket_frame.pack(fill = tk.X, padx = 5, pady = 5)
		
		# Número ficha
		ttk.Label(self.ticket_frame, text = '# Ficha otorgado por la aplicacion').grid(row = 0, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.autoincrement_entry = ttk.Entry(self.ticket_frame)
		self.autoincrement_entry.configure(font = self.font)
		self.autoincrement_entry.insert(0,random.randint(1,1000))
		self.autoincrement_entry.grid(row = 0, column = 1, sticky = 'WE', padx = 10, pady = 5)
		self.autoincrement_entry['state'] = 'readonly'
		
		# Departamento
		ttk.Label(self.ticket_frame, text = save_ui.geo_data['departament_name']).grid(row = 1, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.departament_entry = ttk.Entry(self.ticket_frame)
		self.departament_entry.configure(font = self.font)
		self.departament_entry.grid(row = 1, column =1, sticky = 'WE', padx = 10, pady = 5)
		self.departament_entry.insert(0, save_ui.geo_data['departament'])
		self.departament_entry['state'] = 'readonly'
		
		# Municipio
		ttk.Label(self.ticket_frame, text = save_ui.geo_data['town_name']).grid(row = 2, column = 0, sticky = 'WE', padx = 5, pady = 5)
		self.province_entry = ttk.Entry(self.ticket_frame)
		self.province_entry.configure(font = self.font)
		self.province_entry.grid(row = 2, column = 1, sticky = 'WE', padx = 10, pady = 5)
		self.province_entry.insert(0, save_ui.geo_data['town'])
		self.province_entry['state'] = 'readonly'
		
		# -----------------------------------------  Geopolitical Frame
		self.geopolitical_frame = ttk.Labelframe(self, text = 'Ubicacion geopolitica')
		self.geopolitical_frame.pack(fill = tk.X, padx = 5, pady = 5)
		
		# clase
		ttk.Label(self.geopolitical_frame, text = 'Clase').grid(row = 0, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.class_combo = ttk.Entry(self.geopolitical_frame)
		
		self.class_combo.insert(0, save_ui.geo_data['class'])
		self.class_combo.configure(font = self.font , state = 'readonly')
		self.class_combo.grid(row = 0, column = 1 , sticky = 'WE', padx= 10, pady = 10)
				
		# 5. Codigo centro poblado - El DMC carga automaticamente el codigo del centro poblado
		
		# ACO
		ttk.Label(self.geopolitical_frame,text = 'Area de Coordinación').grid(row = 1, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.aco_entry = ttk.Entry(self.geopolitical_frame)
		self.aco_entry.insert(0,save_ui.geo_data['ACO'])
		self.aco_entry.configure(font = self.font, state = 'readonly')
		self.aco_entry.grid(row = 1, column = 1, sticky = 'WE', padx = 10, pady = 10)
		
		# AO
		ttk.Label(self.geopolitical_frame,text = 'A. Area Operativa').grid(row = 2, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.ao_entry = ttk.Entry(self.geopolitical_frame)
		self.ao_entry.insert(0, save_ui.geo_data['AO'])
		self.ao_entry.configure(font = self.font, state = 'readonly')
		self.ao_entry.grid(row = 2, column = 1, sticky = 'WE', padx = 10, pady = 10)
		
		# UCR ---> Sujeto a cambios
		ttk.Label(self.geopolitical_frame, text = 'B. UCR o UCU').grid(row = 3, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.ucr_entry = ttk.Entry(self.geopolitical_frame)
		self.ucr_entry.insert(0, save_ui.geo_data['UCR'])
		self.ucr_entry.configure(font = self.font, state = 'readonly')
		self.ucr_entry.grid(row = 3, column = 1, sticky = 'WE', padx = 10, pady = 10)
		
		# Localidad
		ttk.Label(self.geopolitical_frame, text='Comuna o location').grid(row = 4, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.location_entry = ttk.Entry(self.geopolitical_frame)
		self.location_entry.configure(font = self.font)
		self.location_entry.grid(row = 4, column = 1, sticky = 'WE', padx = 10, pady = 10)
		
		# 11. Barrio, 9. Corregimiento o 10. Vereda es dependiente de la clase de encuesta.
		ttk.Label(self.geopolitical_frame, text = 'Barrio').grid(row = 5, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.neighborhood_combo = ttk.Combobox(self.geopolitical_frame, state = 'readonly')
		self.neighborhood_combo['values'] = save_ui.geo_data['neighborhood'] # Deben ser cargadas por el DMC
		self.neighborhood_combo.configure(font = self.font)
		self.neighborhood_combo.grid(row = 5, column = 1, sticky = 'WE', padx = 10, pady = 10)
		
		# --------------------------------------------- Boton siguiente
		self.next_button = ttk.Button(self, text = 'Siguiente', command = lambda: self.message_data(parent)).pack(fill='x', padx = 10, pady = 10)
		
	def message_data (self, parent):
		""" Function doc 
		
		"""
		
		if self.class_combo.get() == '':
			message = 'La Clase no tiene una elección válida'
		elif self.aco_entry.get() == '':
			message = 'ACO debe contener algun valor'
		elif self.ao_entry.get() == '':
			message = 'AO debe contener algun valor'
		elif self.ucr_entry.get() == '':
			message = 'UCR o UCU debe contener algun valor'
		elif self.location_entry.get() == '':
			message = 'Localidad debe contener algun valor'
		elif self.neighborhood_combo.get() == '':
			message = 'Barrio no tiene una elección válida'
		else:
			message = f'''
Ficha: {self.autoincrement_entry.get()}
Departamento: {self.departament_entry.get()}
Municipio: {self.province_entry.get()}

Clase: {self.class_combo.get()}
ACO: {self.aco_entry.get()}
AO: {self.ao_entry.get()}
UCR o UCU: {self.ucr_entry.get()}
Localidad: {self.location_entry.get()}
Barrio: {self.neighborhood_combo.get()}
		''' 
		
		if self.class_combo.get() == '' or self.aco_entry.get() == '' or self.ao_entry.get() == '' or self.ucr_entry.get() == '' or self.location_entry.get() == '' or self.neighborhood_combo.get() == '':
			messagebox.showwarning(message = message, title = 'Error')
		else:
			if messagebox.askyesno(message = message, title = 'Salvar Ubicación'):
				print('Se ha guardado la informacion de la ubicacion satisfactoriamente') 
				save_ui.save_ticket(self.autoincrement_entry.get(), 
					self.departament_entry.get(), self.province_entry.get())
					
				save_ui.save_geopolitical( 
					self.class_combo.get(), 
					self.aco_entry.get(), self.ao_entry.get(), 
					self.ucr_entry.get(), self.location_entry.get(), 
					self.neighborhood_combo.get()) 
				parent.switch_frame(igeo.Georeferenciation)

class Application(tk.Tk):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		
		self.title('Info Ubicación')
		self.geometry('400x640+50+50')
		self.resizable(False, False)
		
		self._frame = Location(self)
		self._frame.pack()

def main(args):

	# ~ root.attributes('-alpha', 0.5)
	App = Application()
	App.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
