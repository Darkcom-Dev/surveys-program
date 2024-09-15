# ============================================================ Imports

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import save_ui
import home_ui as ih

# ============================================================ Classes

class Dwelling_data(ttk.Frame):
	
	""" Interface class dedicated to features of the dwelling """
	
	def __init__ (self, parent):
		"""
		Initializes the class, creating a new frame with various widgets to collect 
		information about a dwelling's characteristics and services. The frame is 
		packed with a label frame for dwelling characteristics, a label frame for 
		services, and a button to proceed to the next step.

		Parameters:
			parent (tkinter widget): The parent widget of the frame.

		Returns:
			None
		"""
		ttk.Frame.__init__(self, parent)
		
		self.font = ('Iosevka 11')
		
		# -----------------------  Frame caracteristicas de la vivienda
		self.features_frame = ttk.LabelFrame(self, text = 'Caracteristicas de la vivienda')
		self.features_frame.pack(fill = tk.X, padx = 5, pady = 5)
		
		# ~ 17 tipo de vivienda
		ttk.Label(self.features_frame, text = 'Tipo de vivienda').grid(row = 0, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.dwelling_type_combo = ttk.Combobox(self.features_frame, state = 'readonly')
		self.dwelling_type_combo.configure(font = self.font, background = '#5FE888', foreground = '#E8A548')
		self.dwelling_type_combo['values'] = ['Casa','Apartamento','Cuarto','Otro tipo de vivienda', 'Vivienda indigena']
		self.dwelling_type_combo.grid(row = 0, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		# ~ 18 Material predominante exteriores
		ttk.Label(self.features_frame, text = 'Material de paredes exteriores').grid(row = 1, column = 0, sticky = 'WE',padx = 5, pady=5)
		
		self.predominant_material_combo = ttk.Combobox(self.features_frame, state = 'readonly')
		self.predominant_material_combo.configure(font = self.font, background = '#5FE888', foreground = '#E8A548')
		self.predominant_material_combo['values'] = ['Bloque, ladrillo, piedra, madera pulida','Tapia pisada, adobe','Bahareque','Material prefabricado','Madera burda, tabla, tablón','Guadua, caña, esterilla, otro vegetal','Zinc, tela, lona, cartón, latas, desechos, plástico','Sin paredes']
		self.predominant_material_combo.grid(row = 1, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		# ~ 19 Material predominante pisos
		ttk.Label(self.features_frame, text = 'Material de los pisos').grid(row = 2, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		
		self.floors_material_combo = ttk.Combobox(self.features_frame, state = 'readonly')
		self.floors_material_combo.configure(font = self.font, background = '#5FE888', foreground = '#E8A548')
		self.floors_material_combo['values'] = ['Alfombra o tapete, mármol, parqué, madera pulida, lacada', 'Baldosas, vinilo, tableta, ladrillo','Cemento, gravilla','Madera burda, madera en mal estado, tabla, tablón','Tierra o arena','Otro']
		self.floors_material_combo.grid(row = 2, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		# -------------------------------------------------- Servicios
		
		# ~ 20 Servicios publicos o comunales
		self.services_frame = ttk.Labelframe(self,text = '¿Qué servicios publicos, privados o comunales tiene la vivienda?')
		self.services_frame.pack(fill = tk.X, padx = 5, pady = 5)
		# ~ A. Energia
		self.energy = tk.IntVar()
		self.energy_check = ttk.Checkbutton(self.services_frame, text = 'Energia', variable = self.energy, command = self.validate_stratum)
		self.energy_check.pack(fill = tk.X, padx = 10, pady = 10)
		
		ttk.Label(self.services_frame, text = 'Estrato').pack(fill = tk.X, padx = 5, pady = 5)
		
		self.stratum_combo = ttk.Combobox(self.services_frame, state = 'readonly')
		self.stratum_combo.configure(font = self.font, background = '#5FE888', foreground = '#E8A548')
		self.stratum_combo['values'] = ['Bajo-Bajo','Bajo','Medio-Bajo','Medio','Medio-Alto','Alto','Conexión ilegal','Imposible establecer']
		self.stratum_combo.pack(fill = tk.X, padx = 10, pady = 5)
		
		
		# ~ B. Alcantarrillado
		self.sewerage = tk.IntVar()
		self.sewerage_check = ttk.Checkbutton(self.services_frame, text = 'Alcantarrillado', variable = self.sewerage, command = self.validate_toilette)
		self.sewerage_check.pack(fill = tk.X, padx = 10, pady = 5)
		
		# ~ 20. Tipo de toilette
		ttk.Label(self.services_frame, text = '¿Que tipo de sanitario (inodoro) tiene esta vivienda?:').pack(fill = tk.X, padx = 5)
		
		self.toilette_combo = ttk.Combobox(self.services_frame, state = 'readonly')
		self.toilette_combo.configure(font = self.font, background = '#5FE888', foreground = '#E8A548')
		self.toilette_combo.pack(fill = tk.X, padx = 10, pady = 5)
		self.toilette_combo['values'] = ['Inodoro conectado al alcantarillado', 'Inodoro conectado a pozo septico', 'Inodoro sin conexión', 'Letrina', 'Inodoro con descarga directa a funetes de agua (bajamar)', 'Esta vivienda no tiene servicio sanitario']
		
		
		# ~ D. Recoleccion garbage
		self.garbage = tk.IntVar()
		self.garbage_check = ttk.Checkbutton(self.services_frame, text = 'Recoleccion de garbage', variable = self.garbage, command = self.validate_garbage_times)
		self.garbage_check.pack(fill = tk.X, padx = 10, pady = 5)
		
		ttk.Label(self.services_frame, text = 'Cuantas veces por semana').pack(fill = tk.X, padx = 5, pady = 5)
		
		self.garbage_times = tk.IntVar()
		self.garbage_times_spin = tk.Spinbox(self.services_frame, textvariable = self.garbage_times, from_ = 1, to = 7, state = tk.DISABLED)
		self.garbage_times_spin.configure(font = self.font, background = '#5FE888', foreground = '#E8A548')
		self.garbage_times_spin.pack(fill = tk.X, padx = 10, pady = 5)
		
		# ~ E. Acueducto
		self.aqueduct = tk.IntVar()
		self.aqueduct_check = ttk.Checkbutton(self.services_frame, text = 'Acueducto', variable = self.aqueduct)
		self.aqueduct_check.pack(fill = tk.X, padx = 10, pady = 5)
		
		# ~ C. Gas natural domiciliario
		self.gas = tk.IntVar()
		self.gas_check = ttk.Checkbutton(self.services_frame, text = 'Gas natural domiciliario', variable = self.gas)
		self.gas_check.pack(fill = tk.X, padx = 10, pady = 5)
		
		# ~ F. Internet
		self.internet = tk.IntVar()
		self.internet_check = ttk.Checkbutton(self.services_frame, text = 'Internet (Fijo o móvil)', variable = self.internet)
		self.internet_check.pack(fill = tk.X, padx = 10, pady = 5)
		
		# Boton siguiente
		self.next_button = ttk.Button(self, text = 'Siguiente ▶', command = lambda: self.message_data(parent))
		self.next_button.pack(fill = tk.X, padx = 5, pady=10)
		
		self.garbage_times_spin.after(1000, self.update)
	
	def validate_stratum (self):
		"""
		Validates the stratum combo based on the energy status.

		Checks if the energy is 0 and sets the stratum combo to 'Imposible establecer' if true.
		Also configures the state of the stratum combo to 'disabled' if energy is 0, otherwise 'readonly'.

		Parameters:
			self (object): The instance of the class.

		Returns:
			None
		"""
		if self.energy.get() == 0:
			self.stratum_combo.set('Imposible establecer')
		self.stratum_combo.configure(state = 'disabled' if self.energy.get() == 0 else 'readonly')
	
	def validate_toilette(self):
		"""
		Validates the toilette combo based on the sewerage status.

		Checks if the sewerage is connected (i.e., self.sewerage.get() == 1) and 
		sets the toilette combo to 'Inodoro conectado al alcantarillado' if true. 
		Also configures the state of the toilette combo to 'disabled' if the 
		sewerage is connected, otherwise sets it to 'readonly'.

		Parameters:
			None

		Returns:
			None
		"""
		
		if self.sewerage.get() == 1:
			self.toilette_combo.set('Inodoro conectado al alcantarillado')
		self.toilette_combo.configure(state = 'disabled' if self.sewerage.get() == 1 else 'readonly')
	
	def validate_garbage_times (self):
		"""
		Updates the graphical interface by validating the garbage times.
		
		Checks if the garbage option is disabled (i.e., self.garbage.get() == 0) and 
		sets the garbage times spinbox to 0 and disables it. Otherwise, it enables 
		the garbage times spinbox.
		
		Parameters:
			None
		
		Returns:
			None
		"""
		if self.garbage.get() == 0:
			self.garbage_times_spin.delete(0,'end')
			self.garbage_times_spin.insert(0,0)
		self.garbage_times_spin.configure(state = tk.DISABLED if self.garbage.get() == 0 else tk.NORMAL)
	
	def update (self):
		"""
		Updates the graphical interface by validating the garbage times, stratum, and toilette.
		
		Parameters:
			self (object): The instance of the class.
		
		Returns:
			None
		"""
		self.validate_garbage_times()
		self.validate_stratum()
		self.validate_toilette()
	
	def message_data (self, parent):
		"""
		Generates a message based on the input data and displays it to the user.
		The message can be either an error message if any of the required fields are empty,
		or a confirmation message with the collected data if all fields are filled.
		
		Parameters:
			parent: The parent frame to switch to after saving the data.
		
		Returns:
			None
		"""
		
		if self.dwelling_type_combo.get() == '':
			message = 'Tipo de vivienda no tiene una elección válida'
		elif self.predominant_material_combo.get() == '':
			message = 'El material predominante no tiene una elección válida'
		elif self.floors_material_combo.get() == '':
			message = 'El material de los pisos no tiene una elección válida'
		elif self.toilette_combo.get() == '':
			message = 'Tipo de sanitario ni tiene una elección válida'
		elif self.toilette_combo.get() == 'Inodoro conectado al alcantarillado' and self.sewerage.get() == 0:
			message = 'No puede haber un sanitario conectado al alcantarillado si no hay servicio de alcantarillado'
		elif self.garbage_times_spin.get() != '0' and self.garbage.get() == 0:
			message = 'No puede haber recolecciones de basura semanal si no hay un servicio de recolección'
		else:
			message = f'''
Tipo vivienda: {self.dwelling_type_combo.get()}
Material predominante: {self.predominant_material_combo.get()}		
Material pisos: {self.floors_material_combo.get()}

Energia: {'NO' if self.energy.get() == 0 else 'SI'}
	Estrato: {self.stratum_combo.get()}
Alcantarillado: {'NO' if self.sewerage.get() == 0 else 'SI'}
Gas: {'NO' if self.gas.get() == 0 else 'SI'}
Basuras: {'NO' if self.garbage.get() == 0 else 'SI'}
	Veces: {self.garbage_times_spin.get()}
Acueducto: {'NO' if self.aqueduct.get() == 0 else 'SI'}
	Sanitario: {self.toilette_combo.get()}
	'''
		
		if self.dwelling_type_combo.get() == '' or self.predominant_material_combo.get() == '' or self.floors_material_combo.get() == '' or self.toilette_combo.get() == '' or (self.toilette_combo.get() == 'Inodoro conectado al alcantarillado' and self.sewerage.get() == 0) or (self.garbage_times_spin.get() != '0' and self.garbage.get() == 0):
			messagebox.showwarning(message = message, title = 'Error')
		else:
			if messagebox.askyesno(message = message, title = 'Salvar datos de vivienda'):
				print('Los datos de la vivienda han sido guardados exitosamente') 
				save_ui.save_dwelling_characteristics(self.dwelling_type_combo.get(), 
					self.predominant_material_combo.get(), 
					self.floors_material_combo.get())
				
				save_ui.save_services(self.energy.get(), 
					self.stratum_combo.get(), self.sewerage.get(), 
					self.gas.get(), 
					self.garbage.get(),self.garbage_times_spin.get(), 
					self.aqueduct.get(), self.toilette_combo.get()) 
				parent.switch_frame(ih.Home)


class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Class initialiser.

		Initialises the Application class by calling the tk.Tk class initialiser and
		creating a new instance of the Dwelling_data class as the frame for the application.

		Parameters:
			self: The instance of the class.

		Returns:
			None
		"""
		tk.Tk.__init__(self)
		self._frame = Dwelling_data(self)
		self._frame.pack()

# ====================================================== Program Entry

def main():
	"""
	Runs the main function of the application.

	Parameters:
		None

	Returns:
		int: The exit code.
	"""
	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	main()
