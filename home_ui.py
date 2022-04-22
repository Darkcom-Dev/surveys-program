# ============================================================ Imports

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import save_ui
# Ventana 5
import goods_ui

# ============================================================ Classes

class Home(ttk.Frame):
	""" Graphical interface class dedicated to get home data """
	
	def __init__ (self, parent):
		""" Class initialiser """
		ttk.Frame.__init__(self, parent)
		
		self.font = ('Iosevka 11')
		
		# --------------------------------------------- Caracteristicas
		self.features_house = ttk.Labelframe(self, text = 'Caracteristicas de la vivienda')
		self.features_house.pack(fill = tk.X, padx = 5, pady = 5)
		
		# ~ 21. Número de rooms
		ttk.Label(self.features_house, text = '¿Cuantos cuartos, incluyendo sala-comedor, cuenta la vivienda?').pack(fill = tk.X, padx = 5, pady = 5)
		
		self.rooms_spin = tk.Spinbox(self.features_house,  from_ = 1, to = 10)
		self.rooms_spin.configure(font = self.font)
		self.rooms_spin.pack(fill = tk.X, padx = 10, pady = 5)
		
		# ~ 22. Cuartos para dormir
		ttk.Label(self.features_house, text = '¿Cuantos cuartos usan las personas del hogar para dormir?').pack(fill = tk.X, padx = 5, pady = 5)
		
		self.bedrooms_spin = tk.Spinbox(self.features_house, from_ = 0, to = self.rooms_spin.get()) # Numero de habitaciones no puede exceder el # de rooms
		self.bedrooms_spin.configure(font = self.font)
		self.bedrooms_spin.pack(fill = tk.X, padx = 10, pady = 5)
		self.bedrooms_spin.after(1000, self.update)
		
		# ~ 24. Cocina
		ttk.Label(self.features_house, text = '¿En donde preparan los alimentos las personas de este hogar?:').pack(fill = tk.X, padx = 5, pady = 5)
		
		self.kitchen_combo = ttk.Combobox(self.features_house, state = 'readonly')
		self.kitchen_combo.configure(font = self.font)
		self.kitchen_combo.pack(fill = tk.X, padx = 10, pady = 5)
		
		# Ultima opcion desabilita la pregunta 25 
		self.kitchen_combo['values'] = [
		'En un cuarto usado solo para cocinar', 
		'En un cuarto usado tambien para dormir', 
		'En una sala-comedor con lavaplatos', 
		'En una sala-comedor sin lavaplatos', 
		'En un patio, corredor, enramada o al aire libre', 
		'No preparan alimentos en la vivienda']
		
		# ~ 25. Fuente de agua
		ttk.Label(self.features_house, text = '¿Donde obtiene el agua para preparar los alimentos?').pack(fill = tk.X, padx = 5, pady = 5)
		
		
		self.water_source_combo = ttk.Combobox(self.features_house, state = 'readonly')
		self.water_source_combo.configure(font = self.font)
		self.water_source_combo.pack(fill = tk.X, padx = 10, pady = 5)
		self.water_source_combo['values'] = [
		'Acueducto publico', 
		'Acueducto veredal', 
		'Red de distribucion comunitaria', 
		'Pozo con bomba', 
		'Pozo sin bomba, algibe, jagüey o barreno', 
		'Agua lluvia', 'Rio, quebrada, manantial o nacimiento', 
		'Pila publica', 
		'Carrotanque', 
		'Aguatero', 
		'Agua embotellada o en bolsa']
		
		# ---------------------------------------------------- Personas
		
		self.persons_frame = ttk.Labelframe(self, text = 'Personas')
		self.persons_frame.pack(fill = tk.X, padx = 5, pady = 5)
		
		# ~ 26. Cantidad personas
		ttk.Label(self.persons_frame, text = '¿Cuantas personas que eran miembros de este hogar fallecieron en año pasado?').grid(row = 8, column = 0, columnspan = 2, sticky = 'WE', padx = 5, pady = 5)
		
		
		self.deceased_amount_spin = tk.Spinbox(self.persons_frame, from_ = 0, to = 5)
		self.deceased_amount_spin.configure(font = self.font)
		self.deceased_amount_spin.grid(row = 9, column = 0, sticky = 'WE', padx = 10, pady = 5)
		
		self.deceased_amount_button = ttk.Button(self.persons_frame, text = 'Configurar fallecidos', command = self.deceased)
		self.deceased_amount_button.grid(row = 9, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		
		ttk.Label(self.persons_frame, text = 'Total de personas en el hogar').grid(row = 10, column = 0, columnspan = 2, sticky = 'WE', padx = 5, pady = 5)
		
		self.persons_amount = tk.IntVar()
		self.persons_amount_spin = tk.Spinbox(self.persons_frame,textvariable = self.persons_amount, from_ = 1, to = 99)
		self.persons_amount_spin.configure(font = self.font)
		self.persons_amount_spin.grid(row = 11, column = 0, sticky = 'WE', padx = 10, pady = 5)
		
		self.home_button = ttk.Button(self.persons_frame, text = 'Configurar hogar', command = self.home)
		self.home_button.grid(row = 11, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		self.next_button = ttk.Button(self, text = 'Siguiente ▶', command = lambda: self.message_data(parent))#.grid(row = 12, column = 0, columnspan = 2, sticky = 'WE', padx = 10, pady = 5)
		self.next_button.pack()

		
		
	def update (self):
		""" Update the interface """
		self.bedrooms_spin.configure(to = self.rooms_spin.get())
		self.bedrooms_spin.after(1000, self.update)
		if self.deceased_amount_spin.get() == '0':
			self.deceased_amount_button.state(['disabled'])
		else:
			self.deceased_amount_button.state(['!disabled'])
		
	def message_data (self, parent):
		""" Get data and show in the screen """
		
		if self.kitchen_combo.get() == '':
			message = 'Cocina no tiene una elección válida'
		elif self.water_source_combo.get() == '':
			message = 'Fuente de agua no tiene una elección válida'
		else:
			message = f'''
Cuartos: {self.rooms_spin.get()}
Cuartos para dormir: {self.bedrooms_spin.get()}
Cocina: {self.kitchen_combo.get()}
Fuente agua: {self.water_source_combo.get()}
Personas: {self.deceased_amount_spin.get()}

¿Seguro que los datos son correctos?
		'''
		
		if self.kitchen_combo.get() == '' or self.water_source_combo.get() == '':
			messagebox.showwarning(message = message, title = 'Error')
		else:
			if messagebox.askyesno(message = message, title = 'Salvar información home'):
				print('Los datos del hogar han sido guardados satisfactoriamente') 
				save_ui.save_home(self.rooms_spin.get(), 
					self.bedrooms_spin.get(), self.kitchen_combo.get(), 
					self.water_source_combo.get(), self.deceased_amount_spin.get()) 
				parent.switch_frame(goods_ui.Goods)
		
	def deceased (self):
		""" Function that invoke Deceased window class """
		fallen_window = Deceased_window(int(self.deceased_amount_spin.get()))

	def home (self):
		''' Function that invoke Home window class '''
		hogar_window = Home_window(self.persons_amount.get())

class Deceased_window(tk.Toplevel):
	""" Class that get descesed persons in the last year """
	
	def minion_validation (self):
		# Esta funcion debe obtener los datos de deseased data dentro del bucle y devolver un diccionario
		""" Function doc """
		pass
	
	def __init__ (self, deceased, *args, **kwargs):
		""" Class initialiser """
		super().__init__(*args, **kwargs)
		self.title('Registro de fallecidos.')
		self.config(width = 300, height = 200)
		self.deceased = deceased
		
		self.font = ('Iosevka 11')

		self.fallen_labelf = ttk.Labelframe(self,text = f'Total fallecidos: {self.deceased}')
		self.fallen_labelf.pack(fill = tk.X, padx = 5, pady = 5)
		
		self.deseaseds = []
		
		for p in range(self.deceased):
			allrow = p * 5
			
			gender = tk.IntVar()
			gender_button = ttk.Checkbutton(self.fallen_labelf, text = '¿Es Mujer?', variable = gender)
			gender_button.grid(row = 0 + allrow, column = 0, sticky = 'WE', padx = 5, pady = 5)
			
			ttk.Label(self.fallen_labelf, text = 'Edad al morir').grid(row = 1 + allrow, column = 0, sticky = 'WE', padx = 5, pady = 5)
			
			age_spin = tk.Spinbox(self.fallen_labelf, from_ = 0, to = 999, font = self.font)
			age_spin.grid(row = 1 + allrow, column = 1, sticky = 'WE', padx = 10, pady = 5)
			
			ttk.Label(self.fallen_labelf, text = '¿Se expidió certificado?').grid(row = 2 + allrow, column = 0, sticky = 'WE', padx = 5, pady = 5)
			
			death_certificate_combo = ttk.Combobox(self.fallen_labelf)
			death_certificate_combo.configure(font = self.font)
			death_certificate_combo.grid(row = 2 + allrow, column = 1, sticky = 'WE', padx = 10, pady = 5)
			death_certificate_combo['values'] = ['Si', 'No', 'No sabe']
			death_certificate_combo['state'] = 'readonly'
			
			ttk.Separator(self.fallen_labelf).grid(row = 4 + allrow, column = 0, columnspan = 2, sticky = 'WE', padx = 5, pady = 5)
			
			deseased_data = {'genero' : gender, 'edad' : age_spin, 'certificado' : death_certificate_combo}
			self.deseaseds.append(deseased_data)
			
		close_button = ttk.Button(self.fallen_labelf, text = 'Cerrar', command = self.validate_info).grid(row = 5 * (self.deceased), column = 0, columnspan = 2, sticky = 'WE', padx = 10, pady = 5)
		
		self.focus()
		self.grab_set()
		self.protocol('WM_DELETE_WINDOW', disable_event)
		# ~ self.transient(1)
	
	def validate_info (self):
		""" Function doc """
		
		deseaseds_list = list()
		complete = True
		
		for deseased in self.deseaseds:
			if deseased['edad'].get() == '0':
				complete = False
				messagebox.showinfo(message = 'Revise la edad', title = 'Error')
			elif deseased['certificado'].get() == '':
				coplete = False
				messagebox.showinfo(message = 'Escoja una opcion valida de certificado', title = 'Error')
			else:
				deseased_data = {'genero': deseased['genero'].get(), 'edad': deseased['edad'].get(), 'certificado': deseased['certificado'].get()}
				deseaseds_list.append(deseased_data)
			
		if complete:
			print(*deseaseds_list)
			save_ui.deseased_list = deseaseds_list
			self.destroy()
		
class Home_window(tk.Toplevel):
	""" Class for secondary float window, this window get complete names of the home members """
	
	def __init__ (self, total, *args, **kwargs):
		""" Class initialiser """
		super().__init__(*args, **kwargs)
		self.title('Registro del home.')
		self.config(width = 300, height = 200)
		self.total_hogar = total
		
		self.font = ('Iosevka 11')

		self.persons_frame = ttk.Labelframe(self,text = f'Total personas: {self.total_hogar}')
		self.persons_frame.pack(fill = tk.X, padx = 5, pady = 5)
		home_sentence = '''
¿Cuales son los nombres y apellidos de las personas que conforman este hogar.?
Residentes habituales, presentes o no. Comience por el/la jefe de home.'''
		
		home_out_sentence ='''
¿Hay personas que hagan parte de este home y que no hayan sido anotadas 
en la lista anterior?
(Niños menores de edad, anciano, personas internadas en clinicas, 
personas secuestradas, personas en vacaciones fuera del hogar, etc)'''
		living_out_sentence = '''
¿Alguna persona listada vive en otra residencia?'''
		
		ttk.Label(self.persons_frame, text = f'{home_sentence}\n{home_out_sentence}\n{living_out_sentence}').pack(fill = tk.X, padx = 5, pady = 5)
		
		self.persons_list = list()
		
		for p in range(self.total_hogar):
			
			person_frame = ttk.Labelframe(self.persons_frame,text = f'Persona {p}')
			person_frame.pack(fill = tk.X, padx = 5, pady = 5)
		
			ttk.Label(person_frame,text = '1er nombre').grid(row = 0, column = 0, sticky = 'WE',padx = 5, pady = 5)
			first_name_entry = ttk.Entry(person_frame)
			first_name_entry.configure(font = self.font)
			first_name_entry.grid(row = 0, column = 1, sticky = 'WE', padx = 5, pady = 5)
			
			ttk.Label(person_frame,text = '2do nombre').grid(row = 0, column = 2, sticky = 'WE',padx = 5)
			second_name_entry = ttk.Entry(person_frame)
			second_name_entry.configure(font = self.font)
			second_name_entry.grid(row = 0, column = 3, sticky = 'WE', padx = 5)
			
			ttk.Label(person_frame,text = '1er apellido').grid(row = 1, column = 0, sticky = 'WE', padx = 5, pady = 5)
			first_surname_entry = ttk.Entry(person_frame)
			first_surname_entry.configure(font = self.font)
			first_surname_entry.grid(row = 1, column = 1, sticky = 'WE', padx = 5, pady = 5)
			
			ttk.Label(person_frame,text = '2do apellido').grid(row = 1, column = 2, sticky = 'WE', padx = 5)
			second_surname_entry = ttk.Entry(person_frame)
			second_surname_entry.configure(font = self.font)
			second_surname_entry.grid(row = 1, column = 3, sticky = 'WE', padx = 5)
			
			person = {'f_name' : first_name_entry, 's_name' : second_name_entry, 'f_surname' : first_surname_entry, 's_surname' : second_surname_entry}
			self.persons_list.append(person)

		close_button = ttk.Button(self.persons_frame, text = 'Cerrar', command = self.recoger_datos).pack(fill = tk.X, padx = 5, pady = 5)
		self.focus()
		self.grab_set()
		self.protocol('WM_DELETE_WINDOW', disable_event)
		# ~ self.transient(1)
		
	def recoger_datos (self):
		""" Function doc """
		# ~ TODO: Crear una funcion que recoge los datos y los envia a la ventana principal apenas cierre esta ventana
		# ~ Eliminar la posibilidad de cerrar esta ventana si los datos no estan completos
		
		persons_formated_list = list()
		
		complete = True
		
		for person in self.persons_list:
			
			if person['f_name'].get() == '':
				complete = False
				messagebox.showinfo(message = 'Falta el primer nombre', title = 'Error')
			elif person['f_surname'].get() == '':
				complete = False
				messagebox.showinfo(message = 'Falta el primer apellido', title = 'Error')
			else:
				person = {	'first name' : person['f_name'].get(),
							'second name': person['s_name'].get(),
							'first surname': person['f_surname'].get(),
							'second surname':person['s_surname'].get()}
				persons_formated_list.append(person)
				
				
		
		if complete:
			save_ui.person_list = persons_formated_list
			print(*save_ui.person_list)
			self.destroy()

class Application(tk.Tk):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		self._frame = Home(self)
		self._frame.pack()

# ====================================================== Program Entry

def main(args):
	root = Application()
	root.mainloop()
	return 0

def disable_event ():
	""" Function doc """
	pass

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
