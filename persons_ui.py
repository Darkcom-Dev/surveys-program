import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import ttk_utils as ttku
import save_ui
import health_ui as hui
import ethnicity as eth

class Persons(tk.Frame):
	""" Persons data tk.frame Class """
	
	def __init__ (self, parent):
		"""
		Initializes a new instance of the class, setting up the UI components and their respective layouts.

		Parameters:
			parent (tkinter widget): The parent widget of the current instance.

		Returns:
			None
		"""
		tk.Frame.__init__(self, parent)
		self.name = save_ui.person_list[0]['first name']
		self.surname = save_ui.person_list[0]['first surname']
		
		# ------------------------------------------------ Personas
		self.person_frame = ttk.Labelframe(self, text = f'{self.name} {self.surname}')
		self.person_frame.pack(padx = 5, pady = 5, fill = tk.X)
		
		self.gender = tk.IntVar()
		self.gender_check = ttk.Checkbutton(self.person_frame, text = '¿Es mujer?', variable = self.gender)
		self.gender_check.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = 'WE')
		
		self._age = 0
		
		ttk.Label(self.person_frame, text = '¿Cual es la fecha de nacimiento?').grid(row = 1, column = 0, sticky = 'WE')
		
		self.age = ttk.Label(self.person_frame, text = f'Años cumplidos: ')
		self.age.grid(row = 1, column = 1, sticky = 'WE', padx = 5) # Esto se calcula con la fecha de nacimiento
		
		self.unknow_birth = tk.IntVar()
		self.unknow_birth_check = ttk.Checkbutton(self.person_frame, text = 'Sabe la fecha', variable = self.unknow_birth)
		self.unknow_birth_check.grid(row = 2, column = 0, sticky = 'WE', padx = 5)
		self.unknow_birth_check.after(1000,self.update)
		
		
		self.born_date = DateEntry(self.person_frame, selectmode ='none', year = 2000, month = 1, day = 1, date_pattern ='yyyy-MM-dd')
		self.born_date.grid(row = 2, column = 1, sticky = 'WE', padx = 10, pady = 5)
		

		
		ttk.Label(self.person_frame, text = 'Tipo de documento').grid(row = 3, column = 0, sticky = 'WE', padx = 5, pady = 5)
		ttk.Label(self.person_frame, text = 'Número de documento').grid(row = 3, column = 1, sticky = 'WE', padx = 5, pady = 5)
		
		self.document_type = tk.StringVar()
		self.document_type_combo = ttk.Combobox(self.person_frame, textvariable = self.document_type, state = 'readonly')
		self.document_type_combo.grid(row = 4, column = 0, sticky = 'WE', padx = 10, pady = 5)
		self.document_type_combo['values'] = ['Registro civil de nacimiento', 'Tarjeta de identidad', 'Cédula de cuidadanía', 'Cédula de extrangería']
		
		self.document_number = tk.IntVar()
		self.document_number_spin = tk.Spinbox(self.person_frame,textvariable = self.document_number)
		self.document_number_spin.grid(row = 4, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		
		ttk.Label(self.person_frame, text = f'¿Cual es la relación de {self.name} con el jefe del hogar?').grid(row = 5, column = 0, sticky = 'WE', padx = 5)
		
		self.head_household_realtionship = tk.StringVar()
		self.head_household_realtionship_combo = ttk.Combobox(self.person_frame, textvariable = self.head_household_realtionship, state = 'readonly')
		self.head_household_realtionship_combo.grid(row = 5, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		self.head_household_realtionship_combo['values'] = ['Jefe de hogar','Pareja(Conyuge, Compañer@, Espos@)', 'Hij@', 'Yerno o nuera', 'Padre o madre', 'Padrastro o madrastra','Suegr@','Herman@','Hermanastr@','Cuñad@','Niet@','Abuel@','Otro pariente','Emplead@ del servicio doméstico', 'No pariente']
		
		# ~ Grupos etnicos y culturales
		# Creo que es conveniente hacer una ventana aparte para este tema
		# ----------------------------------------------------- Cultura
		self.culture_frame = ttk.Labelframe(self, text = 'Cultura')
		self.culture_frame.pack(padx = 5, pady = 5, fill = tk.X)
		
		ttk.Label(self.culture_frame,text = f'¿De acuero con su cultura, {self.name} se reconoce como?').grid(row = 7, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.culture = tk.StringVar()
		self.culture_combo = ttk.Combobox(self.culture_frame, textvariable = self.culture, state = 'readonly')
		self.culture_combo.grid(row = 7, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		self.culture_combo['values'] = ['Indigena','Gitan@ o Rrom', 'Raizal del archipielago de san Andres, Providencia, Santa Catalina','Palenquer@ de san Basilio','Negr@, mulat@, afrodescendiente, afrocolombian@','Ningun grupo étnico']
		
		self.ethnicity_button = ttk.Button(self.culture_frame, text = 'Informacion cultural', command = self.configure_ethnicity)
		self.ethnicity_button.grid(row = 7, column = 2, sticky = 'WE', padx = 10, pady = 5)
		
		# ---------------------------------------------------- Movement
		self.movement_frame = ttk.Labelframe(self, text = 'Movilidad')
		self.movement_frame.pack(padx = 5, pady = 5, fill = tk.X)
		## ~ ¿Donde nació?
		
		ttk.Label(self.movement_frame, text = '¿Donde nació?').grid(row = 2, column = 0, sticky = 'WE', padx = 5)
		
		self.site_born = tk.StringVar()
		self.site_born_combo = ttk.Combobox(self.movement_frame, textvariable = self.site_born, state = 'readonly')
		self.site_born_combo.grid(row = 2, column = 1, sticky = 'WE', padx = 10, pady = 5)
		self.site_born_combo['values'] = ['En este municipio','En otro municipio colombiano','En otro pais']
		
		self.site_born_button = ttk.Button(self.movement_frame, text = 'Configurar Sitio', command = self.configure_born_site)
		self.site_born_button.grid(row = 2, column = 2, sticky = 'WE', padx = 10, pady = 5)

		## ~ ¿Donde estaba hace 5 años?
		
		ttk.Label(self.movement_frame, text = '¿Donde vivía hace 5 años?').grid(row = 3, column = 0, sticky = 'WE', padx = 5)
		
		self._5_years_back = tk.StringVar()
		self._5_years_back_combo = ttk.Combobox(self.movement_frame, textvariable = self._5_years_back, state = 'readonly')
		self._5_years_back_combo.grid(row = 3, column = 1, sticky = 'WE', padx = 10)
		self._5_years_back_combo['values'] = ['En este municipio','En otro municipio colombiano','En otro pais','No había nacido']
		
		self._5_years_back_button = ttk.Button(self.movement_frame, text = 'Configurar Sitio', command = self.configure_5_months_back)
		self._5_years_back_button.grid(row = 3, column = 2, sticky = 'WE', padx = 10, pady = 5)

		## ~ ¿Donde estaba hace 12 meses?
		
		ttk.Label(self.movement_frame, text = '¿Donde vivia hace 12 meses?').grid(row = 4, column = 0, sticky = 'WE', padx = 5)
		
		self._12_months_back = tk.StringVar()
		self._12_months_back_combo = ttk.Combobox(self.movement_frame, textvariable = self._12_months_back, state = 'readonly')
		self._12_months_back_combo.grid(row = 4, column = 1, sticky = 'WE', padx = 10)
		self._12_months_back_combo['values'] = ['En este municipio','En otro municipio colombiano','En otro pais','No había nacido']
		
		self._12_months_back_button = ttk.Button(self.movement_frame, text = 'Configurar Sitio', command = self.configure_12_months_back)
		self._12_months_back_button.grid(row = 4, column = 2, sticky = 'WE', padx = 10, pady = 5)
		
		# Frame --------------------------------------------- greater 10
		self.greater10_frame = ttk.LabelFrame(self, text = 'Estado civil para mayores de 10 años.')
		self.greater10_frame.pack(padx = 5, pady = 5, fill = tk.X)
		
		self.civil_state_label = ttk.Label(self.greater10_frame, text = '¿Actualmente cual es su estado civil?')
		self.civil_state_label.grid(row = 0, column = 0, sticky = 'WE', padx = 5)
		
		self.civil_state = tk.StringVar()
		self.civil_state_combo = ttk.Combobox(self.greater10_frame, textvariable = self.civil_state, state = 'readonly')
		self.civil_state_combo.grid(row = 0, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		self.civil_state_combo['values'] = ['Unión libre','Casad@','Divorciad@','Separad@ de unión libre','Separad@ de matrimonio','Viud@','Solter@']
		
		# Frame ---------------------------------------------Womens
		self.women_frame = ttk.Labelframe(self, text = 'Para mujeres mayores de 10 años.')
		self.women_frame.pack(padx = 5, pady = 5, fill = tk.X)
		
		self.sons_button = ttk.Button(self.women_frame,text = 'Hijos', command = self.sons)
		self.sons_button.pack()
		
		# Next --------------------------------------------- >>>>
		ttk.Button(self, text = 'Siguiente ▶', command = lambda: self.message_data(parent)).pack(fill = tk.X, padx = 10, pady=5)
		
	def sons (self):
		"""
		Initializes a new instance of the Sons class.

		Parameters:
			self (object): A reference to the current instance of the class.

		Returns:
			None
		"""
		sons = Sons()
		
	def configure_5_months_back (self):
		"""
		Configures the site settings for the 5 months back period.

		Parameters:
			None

		Returns:
			None
		"""
		_5_years_back = Site()

	def configure_12_months_back (self):
		"""
		Configures the site settings for the 12 months back period.

		Parameters:
			None

		Returns:
			None
		"""
		_12_months_back = Site()
		
	def configure_born_site (self):
		"""
		Configures the born site settings.

		Parameters:
			None

		Returns:
			None
		"""
		born_site = Site()
	
	def configure_ethnicity (self):
		"""
		Configures the ethnicity settings.

		Parameters:
			None

		Returns:
			None
		"""
		born = eth.Ethnicity()

	def update (self):
		"""
		Updates the state and configuration of various UI elements based on the value of the `unknow_birth` variable.
		
		Parameters:
			None
		
		Returns:
			None
		"""
		if self.unknow_birth.get() == 1:
			self.born_date.state(['!disabled'])
		else:
			self.born_date.state(['disabled'])
			
		self.date = save_ui.today.date()
		born_formated = datetime.strptime(self.born_date.get(),'%Y-%m-%d').date()
		self._age = (self.date - born_formated).days // 365
		self.age.configure(text = f'Años cumplidos: {self._age}')
				
		if self._age > 10:
			self.greater10_frame.state(['!disabled'])
			self.civil_state_combo.state(['!disabled'])
			self.civil_state_label.state(['!disabled'])
			if self.gender.get() == 0:
				self.women_frame.state(['disabled'])
				self.sons_button.state(['disabled'])
			else:
				self.women_frame.state(['!disabled'])
				self.sons_button.state(['!disabled'])
		else:
			self.civil_state_combo.set('Solter@')
			self.civil_state_combo.state(['disabled'])
			self.civil_state_label.state(['disabled'])
			self.greater10_frame.state(['disabled'])
			self.women_frame.state(['disabled'])
			
		#------------------------------------------------------------

		# -----------------------------------------------------------
		if self.site_born_combo.get() == 'En este municipio' or self.site_born_combo.get() == 'No había nacido':
			self.site_born_button.state(['disabled'])
		else:
			self.site_born_button.state(['!disabled'])
		# -----------------------------------------------------------
		if self._5_years_back_combo.get() == 'En este municipio' or self._5_years_back_combo.get() == 'No había nacido':
			self._5_years_back_button.state(['disabled'])
		else:
			self._5_years_back_button.state(['!disabled'])
		# -----------------------------------------------------------
		if self._12_months_back_combo.get() == 'En este municipio' or self._12_months_back_combo.get() == 'No había nacido':
			self._12_months_back_button.state(['disabled'])
		else:
			self._12_months_back_button.state(['!disabled'])
		#------------------------------------------------------------
		self.unknow_birth_check.after(1000,self.update)
		
	def message_data (self, parent):
		"""
		Generates a message containing the person's data and checks if the information is correct.
		
		Parameters:
			parent (object): The parent object that called this function.
		
		Returns:
			None
		"""
		
		message = f"""
{self.name} {self.surname} es {'mujer' if self.gender.get() == 1 else 'hombre'}
sabe la fecha de nacimiento {self.unknow_birth.get()} y la fecha es {self.born_date.get()}
Tipo de documento: {self.document_type_combo.get()} con numero: {self.document_number_spin.get()}
Su relacion con el jefe de hogar es: {self.head_household_realtionship_combo.get()}
Se reconoce asi mismo como: {self.culture_combo.get()}
		"""
		
		if self.document_type.get() == '':
			messagebox.showinfo(message = 'Elige una opcion válida en el tipo de documento', title = 'Error')
		elif self.document_number_spin.get() == '0':
			messagebox.showinfo(message = 'Ingresa el numero de documento', title = 'Error')
		elif self.head_household_realtionship_combo.get() == '':
			messagebox.showinfo(message = '¿Qué relación tiene con el jefe de hogar?', title = 'Error')
		elif self.culture_combo.get() == '':
			messagebox.showinfo(message = 'Elige una opcion valida para el tipo de cultura', title = 'Error')
		else:
			if messagebox.askyesno(message = message, title = '¿Es la informacion correcta?'):
				print('La informacion ha sido guardada satisfactoriamente')
				save_ui.save_persons(self.gender.get(), self.unknow_birth.get(), 
					self.born_date.get(), self.document_type_combo.get(), 
					self.document_number_spin.get(), 
					self.head_household_realtionship_combo.get(), 
					self.culture_combo.get())
				save_ui.age = self._age
				parent.switch_frame(hui.Health)

class Sons(tk.Toplevel):
	""" Sons top level Class """
	
	def __init__ (self):
		"""
		Initializes the sons information frame, including labels, checkboxes, spinboxes, and comboboxes for user input.
		Sets up the layout and configuration for each widget, including grid positions, sticky options, and padding.
		No parameters are taken, and no return value is provided.
		"""
		super().__init__()
		
		self.sons_frame = ttk.LabelFrame(self, text = 'Información de los sons')
		self.sons_frame.pack(fill = tk.X, padx = 5, pady = 5, ipady = 5)
		
		self.total_sons = tk.IntVar()
		self.total_sons_check = ttk.Checkbutton(self.sons_frame,text = '¿Ha tenido algún hijo o hija que haya nacido vivo?', variable = self.total_sons)
		self.total_sons_check.grid(row = 0, column = 0, columnspan = 3, sticky = 'WE', padx = 5)
		
		ttk.Label(self.sons_frame, text = '¿Cuantos?').grid(row = 1, column = 0, sticky = 'WE', padx = 5)
		self.total_amount_sons = tk.IntVar()
		self.total_amount_sons_spin = tk.Spinbox(self.sons_frame, textvariable = self.total_amount_sons, from_ = 0, to = 99)
		self.total_amount_sons_spin.grid(row = 1, column = 1, sticky = 'WE', padx = 5)
		self.total_amount_sons_spin.after(1000, self.update)
		
		ttk.Label(self.sons_frame, text = '¿Cuantos hombres?').grid(row = 2, column = 0, sticky = 'WE', padx = 5)
		self.total_men = tk.IntVar()
		self.total_men_spin = tk.Spinbox(self.sons_frame, textvariable = self.total_men, from_ = 0, to = self.total_amount_sons.get())
		self.total_men_spin.grid(row = 2, column = 1, sticky = 'WE', padx = 5)
		
		ttk.Label(self.sons_frame, text = '¿Cuantas mujeres?').grid(row = 3, column = 0, sticky = 'WE', padx = 5)
		self.total_women = tk.IntVar()
		self.total_women_spin = tk.Spinbox(self.sons_frame, textvariable = self.total_women, from_ = 0, to = self.total_amount_sons.get() - self.total_men.get())
		self.total_women_spin.grid(row = 3, column = 1, sticky = 'WE', padx = 5)
		
		
		self.sons_lives = tk.IntVar()
		self.sons_lives_check = ttk.Checkbutton(self.sons_frame,text = '¿Cuantos sons estan vivos actualmente?',variable = self.sons_lives)
		self.sons_lives_check.grid(row = 4, column = 0, columnspan = 3, sticky = 'WE', padx = 5)
		
		ttk.Label(self.sons_frame, text = '¿Cuantos?').grid(row = 5, column = 0, sticky = 'WE', padx = 5)
		self.total_sons_lives = tk.IntVar()
		self.total_sons_lives_spin = tk.Spinbox(self.sons_frame, textvariable = self.total_sons_lives, from_ = 0, to = 99)
		self.total_sons_lives_spin.grid(row = 5, column = 1, sticky = 'WE', padx = 5)
		self.total_sons_lives_spin.after(1000, self.update)
		
		ttk.Label(self.sons_frame, text = '¿Cuantos hombres?').grid(row = 6, column = 0, sticky = 'WE', padx = 5)
		self.total_men_lives = tk.IntVar()
		self.total_men_lives_spin = tk.Spinbox(self.sons_frame, textvariable = self.total_men_lives, from_ = 0, to = self.total_sons_lives.get())
		self.total_men_lives_spin.grid(row = 6, column = 1, sticky = 'WE', padx = 5)
		
		ttk.Label(self.sons_frame, text = '¿Cuantas mujeres?').grid(row = 7, column = 0, sticky = 'WE', padx = 5)
		self.total_women_lives = tk.IntVar()
		self.total_women_lives_spin = tk.Spinbox(self.sons_frame, textvariable = self.total_women_lives, from_ = 0, to = self.total_sons_lives.get() - self.total_men_lives.get())
		self.total_women_lives_spin.grid(row = 7, column = 1, sticky = 'WE', padx = 5)
		
		
		self.sons_foreign = tk.IntVar()
		self.sons_foreign_check = ttk.Checkbutton(self.sons_frame,text = '¿Tiene hijos que viven actualmente en el exterior?',variable = self.sons_foreign)
		self.sons_foreign_check.grid(row = 8, column = 0, columnspan = 3, sticky = 'WE', padx = 5)
		
		ttk.Label(self.sons_frame, text = '¿Cuantos?').grid(row = 9, column = 0, sticky = 'WE', padx = 5)
		self.total_sons_foreign = tk.IntVar()
		self.total_sons_foreign_spin = tk.Spinbox(self.sons_frame, textvariable = self.total_sons_foreign, from_ = 0, to = 99)
		self.total_sons_foreign_spin.grid(row = 9, column = 1, sticky = 'WE', padx = 5)
		self.total_sons_foreign_spin.after(1000, self.update)
		
		ttk.Label(self.sons_frame, text = '¿Cuantos hombres?').grid(row = 10, column = 0, sticky = 'WE', padx = 5)
		self.total_men_foreign = tk.IntVar()
		self.total_men_foreign_spin = tk.Spinbox(self.sons_frame, textvariable = self.total_men_foreign, from_ = 0, to = self.total_sons_foreign.get())
		self.total_men_foreign_spin.grid(row = 10, column = 1, sticky = 'WE', padx = 5)
		
		ttk.Label(self.sons_frame, text = '¿Cuantas mujeres?').grid(row = 11, column = 0, sticky = 'WE', padx = 5)
		self.total_women_foreign = tk.IntVar()
		self.total_women_foreign_spin = tk.Spinbox(self.sons_frame, textvariable = self.total_women, from_ = 0, to = self.total_sons_foreign.get() - self.total_men_foreign.get())
		self.total_women_foreign_spin.grid(row = 11, column = 1, sticky = 'WE', padx = 5)
		
		
		self.know_born = tk.IntVar()
		self.unknow_birth_check = ttk.Checkbutton(self.sons_frame, text = 'Sabe mes y año de nacimiento del ultimo hijo nacido vivo',variable = self.know_born)
		self.unknow_birth_check.grid(row = 12, column = 0, columnspan = 3, sticky = 'WE', padx = 5)
		
		ttk.Label(self.sons_frame, text = 'Mes').grid(row = 13, column = 0, sticky = 'WE', padx = 5)
		self.month_born = tk.StringVar()
		self.month_born_combo = ttk.Combobox(self.sons_frame, textvariable = self.month_born)
		self.month_born_combo.grid(row = 13, column = 1, sticky = 'WE', padx = 5)
		self.month_born_combo['state'] = 'readonly'
		self.month_born_combo['values'] = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
		
		self.born_year = tk.IntVar()
		self.born_year_spin = tk.Spinbox(self.sons_frame, textvariable = self.born_year, from_ = 1950, to = 2023) # Maximo hasta el año actual
		self.born_year_spin.grid(row = 13, column = 2, sticky = 'WE', padx = 5)
		
	def update (self):
		"""
		Updates the state and configuration of various UI elements based on the current values of other UI elements.

		Enables or disables spinboxes and comboboxes depending on the values of associated checkboxes and spinboxes.
		Configures the maximum value of certain spinboxes based on the values of other spinboxes.

		Parameters:
			self: The instance of the class containing this method.

		Returns:
			None
		"""
		self.total_amount_sons_spin['state'] = 'disabled' if self.total_sons.get() == 0 else 'normal'
		self.total_men_spin['state'] = 'disabled' if self.total_sons.get() == 0 else 'normal'
		self.total_women_spin['state'] = 'disabled' if self.total_sons.get() == 0 else 'normal'
		self.total_men_spin.config(to = self.total_amount_sons.get() - self.total_women.get())
		self.total_women_spin.config(to = self.total_amount_sons.get() - self.total_men.get())
		
		self.total_sons_lives_spin['state'] = 'disabled' if self.sons_lives.get() == 0 else 'normal'
		self.total_men_lives_spin['state'] = 'disabled' if self.sons_lives.get() == 0 else 'normal'
		self.total_women_lives_spin['state'] = 'disabled' if self.sons_lives.get() == 0 else 'normal'
		self.total_men_lives_spin.config(to = self.total_sons_lives.get() - self.total_women_lives.get())
		self.total_women_lives_spin.config(to = self.total_sons_lives.get() - self.total_men_lives.get())
		
		self.total_sons_foreign_spin['state'] = 'disabled' if self.sons_foreign.get() == 0 else 'normal'
		self.total_men_foreign_spin['state'] = 'disabled' if self.sons_foreign.get() == 0 else 'normal'
		self.total_women_foreign_spin['state'] = 'disabled' if self.sons_foreign.get() == 0 else 'normal'
		self.total_men_foreign_spin.config(to = self.total_sons_foreign.get() - self.total_women_foreign.get())
		self.total_women_foreign_spin.config(to = self.total_sons_foreign.get() - self.total_men_foreign.get())
		
		self.month_born_combo['state'] = 'disabled' if self.know_born.get() == 0 else 'readonly'
		self.born_year_spin['state'] = 'disabled' if self.know_born.get() == 0 else 'normal'
		
		self.total_amount_sons_spin.after(1000, self.update)
		


class Site(tk.Toplevel):
	""" Site top level class """
	
	def __init__ (self):
		"""
		Initializes the object by setting up the UI components, including the site frame, 
		department, municipality, country, arrival year, locality type, and close button.
		
		Parameters:
			None
		
		Returns:
			None
		"""
		super().__init__()
		self.font = ('Iosevka 10')
		
		site_frame = ttk.LabelFrame(self, text = 'Site')
		site_frame.pack(fill = tk.X, padx = 5, pady = 5)
		
		# Esto debe ir en otra interfaz
		ttk.Label(site_frame, text = 'Departamento').grid(row = 0, column = 0, sticky = 'WE', padx = 5, pady = 5)
		self.departament_entry = ttk.Entry(site_frame, font = self.font)
		self.departament_entry.grid(row = 0, column = 1, sticky = 'WE', padx = 10, pady = 5)

		ttk.Label(site_frame, text = 'Municipio').grid(row = 1, column = 0, sticky = 'WE', padx = 5)
		self.municipality_entry = ttk.Entry(site_frame, font = self.font)
		self.municipality_entry.grid(row = 1, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		ttk.Label(site_frame, text = 'Pais').grid(row = 2, column = 0, sticky = 'WE', padx = 5)
		self.country_entry = ttk.Entry(site_frame, font = self.font)
		self.country_entry.grid(row = 2, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		ttk.Label(site_frame, text = '¿En que año llegó a Colombia').grid(row = 3, column = 0, sticky = 'WE', padx = 5)
		self.arrival_year = tk.Spinbox(site_frame,from_ = 1950, to = 2150)
		self.arrival_year.grid(row = 3, column = 1, sticky = 'WE', padx = 10, pady = 5)
		
		## ~ ¿Vivia en?
		self.locality_type = tk.StringVar()
		ttk.Label(site_frame, text = '¿Vivia en?').grid(row = 4, column = 0, sticky = 'WE', padx = 5)
		self.locality_type_combo = ttk.Combobox(site_frame, textvariable = self.locality_type, font = self.font)
		self.locality_type_combo.grid(row = 4, column = 1, sticky = 'WE', padx = 10)
		self.locality_type_combo['state'] = 'readonly'
		self.locality_type_combo['values'] = ['Cabecera municipal','Un centro poblado','Rural disperso']
		
		self.close_button = ttk.Button(site_frame, text = 'Cerrar', command = self.message_data)
		self.close_button.grid(row = 5, column = 0, columnspan = 2, sticky = 'WE', padx = 10, pady = 10, )
		

	def message_data (self):
		""" Function doc """
		
		message = f'''
Departamento: {self.departament_entry.get()}
Municipio: {self.municipality_entry.get()}
Pais: {self.country_entry.get()}
Año de llegada: {self.arrival_year.get()}
Localidad: {self.locality_type_combo.get()}
		'''
		
		if self.departament_entry.get() == '':
			messagebox.showinfo(message = 'Ingrese el departamento', title = 'Error')
		elif self.municipality_entry.get() == '':
			messagebox.showinfo(message = 'Ingrese el municipio', title = 'Error')
		elif self.country_entry.get() == '':
			messagebox.showinfo(message = 'Ingrese el pais', title = 'Error')
		elif self.arrival_year.get() == '':
			messagebox.showinfo(message = 'Ingrese el año de llegada al pais', title = 'Error')
		elif self.locality_type_combo.get() == '':
			messagebox.showinfo(message = 'Elija una opcion valida para localidad', title = 'Error')
		else:
			if messagebox.askyesno(message = message, title = 'Salvar información'):
				print('La informacion de configuración de localidad ha sido guardada satisfactoriamente')
				
		


class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Initializes the Tkinter window and sets the title.

		Parameters:
			None

		Returns:
			None
		"""
		tk.Tk.__init__(self)
		self.title('Personas')
		self._frame = Persons(self)
		self._frame.pack()

def main():
	"""
	Main function of the application, responsible for initializing the UI and adding a test person to the person list.
	
	Parameters:
		None
	
	Returns:
		int: 0 on successful execution
	"""
	test_person = {'first name':'Jose', 'second name':'Maria', 'first surname':'Cordoba', 'second surname':'Velasquez'}
	save_ui.person_list.append(test_person)
	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	main()
