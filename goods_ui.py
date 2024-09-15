
# ============================================================ Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import save_ui
import persons_ui

# ============================================================ Classes
class Goods(tk.Frame):
	
	def __init__ (self, parent):
		"""
		Initializes the class, creating a new frame with various widgets to collect user data.
		
		Parameters:
			parent (tkinter widget): The parent widget of this frame.
		
		Returns:
			None
		"""
		tk.Frame.__init__(self, parent)
		
		self.font = ('Iosevka 10')
		
		# ------------------------------------------------------ Bienes
		self.goods_frame = ttk.LabelFrame(self, text = 'Bienes')
		self.goods_frame.pack(fill = tk.X, expand = True, padx = 5, pady = 5)
		
		self.freezer = tk.IntVar()
		self.freezer_check = ttk.Checkbutton(self.goods_frame, text = 'Nevera o refrigerador', variable = self.freezer)
		self.freezer_check.pack(fill = tk.X, padx = 5)
		
		self.laundry = tk.IntVar()
		self.laundry_check = ttk.Checkbutton(self.goods_frame, text = 'Maquina lavadora de ropa', variable = self.laundry)
		self.laundry_check.pack(fill = tk.X, padx = 5)
		
		self.computer = tk.IntVar()
		self.computer_check = ttk.Checkbutton(self.goods_frame, text = 'Computador', variable = self.computer)
		self.computer_check.pack(fill = tk.X, padx = 5)
		
		self.motorcicle = tk.IntVar()
		self.motorcicle_check = ttk.Checkbutton(self.goods_frame, text = 'Moto o motoneta', variable = self.motorcicle)
		self.motorcicle_check.pack(fill = tk.X, padx = 5)
		
		self.tractor = tk.IntVar()
		self.tractor_check = ttk.Checkbutton(self.goods_frame, text = 'Tractor', variable = self.tractor)
		self.tractor_check.pack(fill = tk.X, padx = 5)
		
		self.car = tk.IntVar()
		self.car_check = ttk.Checkbutton(self.goods_frame, text = 'Carro', variable = self.car)
		self.car_check.pack(fill = tk.X, padx = 5)
		
		self.realstate = tk.IntVar()
		self.realstate_check = ttk.Checkbutton(self.goods_frame, text = 'Otro bien raiz', variable = self.realstate)
		self.realstate_check.pack(fill = tk.X, padx = 5)
		
		#------------------------------------------------------- Gastos
		
		self.expenses_frame = ttk.Labelframe(self, text = 'Gastos')
		self.expenses_frame.pack(fill = tk.X, expand = True, padx = 5, pady = 10, ipady = 5)
		
		ttk.Label(self.expenses_frame, text = 'Alimentación').grid(row = 0, column = 0, sticky = 'WE', padx = 5)
		self.feeding_spin = tk.Spinbox(self.expenses_frame, from_ = 0, to = 9999999999)
		self.feeding_spin.grid(row = 0, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.expenses_frame, text = 'Transporte').grid(row = 1, column = 0, sticky = 'WE', padx = 5)
		self.transport_spin = tk.Spinbox(self.expenses_frame, from_ = 0, to = 9999999999)
		self.transport_spin.grid(row = 1, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.expenses_frame, text = 'Educación').grid(row = 2, column = 0, sticky = 'WE', padx = 5)
		self.education_spin = tk.Spinbox(self.expenses_frame, from_ = 0, to = 9999999999)
		self.education_spin.grid(row = 2, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.expenses_frame, text = 'Salud').grid(row = 3, column = 0, sticky = 'WE', padx = 5)
		self.health_spin = tk.Spinbox(self.expenses_frame, from_ = 0, to = 9999999999)
		self.health_spin.grid(row = 3, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.expenses_frame, text = 'Servicios públicos').grid(row = 4, column = 0, sticky = 'WE', padx = 5)
		self.public_services_spin = tk.Spinbox(self.expenses_frame, from_ = 0, to = 9999999999)
		self.public_services_spin.grid(row = 4, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.expenses_frame, text = 'Celular').grid(row = 5, column = 0, sticky = 'WE', padx = 5)
		self.mobile_spin = tk.Spinbox(self.expenses_frame, from_ = 0, to = 9999999999)
		self.mobile_spin.grid(row = 5, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.expenses_frame, text = 'Arriendo').grid(row = 6, column = 0, sticky = 'WE', padx = 5)
		self.rent_spin = tk.Spinbox(self.expenses_frame, from_ = 0, to = 9999999999)
		self.rent_spin.grid(row = 6, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.expenses_frame, text = 'Otros gastos').grid(row = 7, column = 0, sticky = 'WE', padx = 5)
		self.other_expenses_spin = tk.Spinbox(self.expenses_frame, from_ = 0, to = 9999999999)
		self.other_expenses_spin.grid(row = 7, column = 1, sticky = 'WE', padx = 10)
		
		#-------------------------------------- Historia de la vivienda
		
		self.history_frame = ttk.Labelframe(self, text = 'Historia de la vivienda')
		self.history_frame.pack(fill = tk.X, expand = True, padx = 5, pady = 5, ipady = 5)
		
		ttk.Label(self.history_frame, text = 'Tiempo habitando la vivienda').grid(row = 0, column = 0, sticky = 'WE', padx = 5, pady = 5)
		self.living_time_combo = ttk.Combobox(self.history_frame, state = 'readonly')
		self.living_time_combo.grid(row = 0, column = 1, sticky = 'WE', padx = 10)
		self.living_time_combo['values'] = ['Menos de un año','Entre 1 y 5','Más de 5 y hasta 10 años','Más de 10 años']
		
		ttk.Label(self.history_frame, text = 'Inundaciones').grid(row = 1, column = 0, sticky = 'WE', padx = 5)
		self.floods_spin = tk.Spinbox(self.history_frame, from_ = 0, to = 10)
		self.floods_spin.grid(row = 1, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.history_frame, text = 'Avalanchas').grid(row = 2, column = 0, sticky = 'WE', padx = 5)
		self.avalanche_spin = tk.Spinbox(self.history_frame, from_ = 0, to = 10)
		self.avalanche_spin.grid(row = 2, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.history_frame, text = 'Terremoto').grid(row = 3, column = 0, sticky = 'WE', padx = 5)
		self.earthquake_spin = tk.Spinbox(self.history_frame, from_ = 0, to = 10)
		self.earthquake_spin.grid(row = 3, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.history_frame, text = 'Incendios').grid(row = 4, column = 0, sticky = 'WE', padx = 5)
		self.conflagration_spin = tk.Spinbox(self.history_frame, from_ = 0, to = 10)
		self.conflagration_spin.grid(row = 4, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.history_frame, text = 'Vendavales').grid(row = 5, column = 0, sticky = 'WE', padx = 5)
		self.storms_spin = tk.Spinbox(self.history_frame, from_ = 0, to = 10)
		self.storms_spin.grid(row = 5, column = 1, sticky = 'WE', padx = 10)
		
		ttk.Label(self.history_frame, text = 'Hundimiento del terreno').grid(row = 6, column = 0, sticky = 'WE', padx = 5)
		self.terrain_subsidence_spin = tk.Spinbox(self.history_frame, from_ = 0, to = 10)
		self.terrain_subsidence_spin.grid(row = 6, column = 1, sticky = 'WE', padx = 10)
		
		#---------------------------------
		
		ttk.Button(self, text = 'Siguiente ▶', command = lambda: self.message_data(parent)).pack(fill = tk.X, padx = 10, pady = 10)
		
	def message_data (self, parent):
		"""
		Saves information about the goods and expenses of a household.
		
		Parameters:
			parent: The parent frame that called this function.
		
		Returns:
			None
		"""
		message = f'''
Nevera: {'NO' if self.freezer.get() == 0 else 'SI'}
Lavadora: {'NO' if self.laundry.get() == 0 else 'SI'}
Computer: {'NO' if self.computer.get() == 0 else 'SI'}
Motocicleta: {'NO' if self.motorcicle.get() == 0 else 'SI'}
Tractor: {'NO' if self.tractor.get() == 0 else 'SI'}
Carro: {'NO' if self.car.get() == 0 else 'SI'}
Propiedades: {'NO' if self.realstate.get() == 0 else 'SI'}

Alimentación: {self.feeding_spin.get()}
Transporte: {self.transport_spin.get()}
Educación: {self.education_spin.get()}
Salud: {self.health_spin.get()}
Servicios públicos: {self.public_services_spin.get()}
Celular: {self.mobile_spin.get()}
Arriendo: {self.rent_spin.get()}
Otros gastos: {self.other_expenses_spin.get()}

Tiempo habitando la vivienda: {self.living_time_combo.get()}
Inundaciones: {self.floods_spin.get()}
Avalanchas: {self.avalanche_spin.get()}
Terremoto: {self.earthquake_spin.get()}
Incendios: {self.conflagration_spin.get()}
Vendabales: {self.storms_spin.get()}
Hundimiento del terreno: {self.terrain_subsidence_spin.get()}
		'''
		if self.living_time_combo.get() == '':
			messagebox.showwarning(message = 'Tiempo habitando la vivienda no eligió una opcion válida')
		else:
			if messagebox.askyesno(message = message, title = 'Salvar Información'):
				print('La informacion del hogar ha sido guardada satisfactoriamente') 
				save_ui.save_goods(self.freezer.get(), 
				self.laundry.get(), self.computer.get(), 
				self.motorcicle.get(), self.tractor.get(), 
				self.car.get(), self.realstate.get()) 
				
				save_ui.save_spends(self.feeding_spin.get(), 
				self.transport_spin.get(), self.education_spin.get(), 
				self.health_spin.get(), 
				self.public_services_spin.get(), 
				self.mobile_spin.get(), self.rent_spin.get(), 
				self.other_expenses_spin.get()) 
				
				save_ui.save_history(self.living_time_combo.get(), 
				self.floods_spin.get(), self.avalanche_spin.get(), 
				self.earthquake_spin.get(), 
				self.conflagration_spin.get(),self.storms_spin.get(), 
				self.terrain_subsidence_spin.get()) 
				
				# No puede avanzar porque necesita:
				# el nombre y apellido de la persona
				parent.switch_frame(persons_ui.Persons) 

class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Class initialiser.
		
		Initialises the Application class.
		
		Parameters:
			self (object): The instance of the class containing this method.
		
		Returns:
			None
		"""
		tk.Tk.__init__(self)
		self._frame = Goods(self)
		self._frame.pack()
		

	def switch_frame(self, frame_class):
		"""
		Switches the current frame to a new one.

		Parameters:
			self (object): The instance of the class containing this method.
			frame_class (class): The class of the new frame to switch to.

		Returns:
			None
		"""
		new_frame = frame_class(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()

# ====================================================== Program Entry

def main():
	"""
	The main function that runs the application.

	Args:
	    args (list): The command line arguments.

	Returns:
	    int: The exit code.

	"""
	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	main()
