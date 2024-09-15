import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import save_ui
import end_ui
import persons_ui

class Profesional(ttk.Frame):
	""" Class that get educative and professional info """
	
	def __init__ (self, parent):
		"""
		Initialises the Profesional class, creating a LabelFrame for professional information.
		Sets up various UI elements, including Checkbuttons, Comboboxes, and Labels, to collect 
		information about the user's professional and educational background.
		The function takes a parent parameter, which is the parent widget for the Profesional frame.
		No return value.
		"""
		ttk.Frame.__init__(self, parent)
		
		self.profession_frame = ttk.LabelFrame(parent, text = 'Información profesional')
		self.profession_frame.pack(fill = tk.X, padx = 5, pady = 5, ipady = 5)
		
		self.write = tk.IntVar()
		self.write_check = ttk.Checkbutton(self.profession_frame,text = '¿Sabe leer y escribir?', variable = self.write)
		self.write_check.grid(row = 0, column = 0, columnspan = 2, sticky = 'WE', padx = 5)
		
		self.educative_assistance = tk.IntVar()
		self.asistencia_educativa_check = ttk.Checkbutton(self.profession_frame, text = 'Asiste a una institucion educativa de forma presencial o virtual?',variable = self.educative_assistance)
		self.asistencia_educativa_check.grid(row = 1, column = 0, columnspan = 2, sticky = 'WE', padx = 5)
		
		ttk.Label(self.profession_frame, text = '¿Que tipo de instituto?').grid(row = 2, column = 0, sticky = 'WE', padx = 5)
		
		self.institute_type_combo = ttk.Combobox(self.profession_frame)
		self.institute_type_combo.grid(row = 2, column = 1, sticky = 'WE', padx = 5)
		self.institute_type_combo['state'] = 'readonly'
		self.institute_type_combo['values'] = ['Pre-escolar', 'Básica primaria', 'Básica secundaria', 'Media académica o clásica', 'Media técnica', 'Normalista', 'Técnica profesional', 'Tecnológica', 'Universitaria','Especialización','Maestría','Doctorado','Ninguno']
		
		ttk.Label(self.profession_frame, text = '¿Hasta que grado cursó?').grid(row = 3, column = 0, sticky = 'WE', padx = 5)
		
		self.grade_values = ['Hola']
		self.grade_institute_combo = ttk.Combobox(self.profession_frame)
		self.grade_institute_combo.grid(row = 3, column = 1, sticky = 'WE', padx = 5)
		self.grade_institute_combo['state'] = 'readonly'
		self.grade_institute_combo['values'] = self.grade_values
		self.grade_institute_combo.after(1000, self.update)
		
		ttk.Label(self.profession_frame,text = '¿Durante la semana pasada ...?').grid(row = 4, column = 0, sticky = 'WE', padx = 5)
		
		self.laboral_situation_combo = ttk.Combobox(self.profession_frame)
		self.laboral_situation_combo.grid(row = 4, column = 1, sticky = 'WE', padx = 5)
		self.laboral_situation_combo['state'] = 'readonly'
		self.laboral_situation_combo['values'] = ['Trabajó una hora en semana en una actividad que le generó un ingreso','Trabajó en un negocio por lo menos una hora sin que le pagaran', 'No trabajó, pero tenía un empleo, negocio por el que recibe ingresos','Buscó trabajo','Vivió de jubilacion, pensión o renta','Estudió','Realizó oficios del hogar','Es incapacitado permanente para trabajar','Estuvo en otra situación']
		
		ttk.Button(parent, text = 'Siguiente ▶', command=lambda: self.message_data(parent)).pack(fill = tk.X, padx = 10, pady = 5)
	
	def message_data (self, parent):
		"""
		Generates a message based on the input data and displays it to the user.
		The message contains information about the user's literacy and writing skills,
		educational assistance, type of institution, grade in institution, and laboral situation.
		If any of the required fields are empty, an error message is displayed.
		If the user confirms the information, it is saved to the database and the program proceeds to the next person's information.
		
		Parameters:
			parent (tkinter.Frame): The parent frame to switch to after saving the data.
		
		Returns:
			None
		"""
		
		message = f'''
Leer y Escribir: {'NO' if self.write.get() == 0 else 'SI'}
Asistencia educativa: {'NO' if self.educative_assistance.get() == 0 else 'SI'}
Tipo de instituto: {self.institute_type_combo.get()}
Grado en instituto: {self.grade_institute_combo.get()}
Situacion laboral: {self.laboral_situation_combo.get()}
		'''
		if self.institute_type_combo.get() == '':
			messagebox.showwarning(message = 'Tipo de instituto no tiene una selección válida', title = 'Error')
		elif self.grade_institute_combo.get() == '':
			messagebox.showwarning(message = 'Grado de instituto no tiene una selección válida', title = 'Error')
		elif self.laboral_situation_combo.get() == '':
			messagebox.showwarning(message = 'Situacion laboral no tiene una selección válida', title = 'Error')
		else:
			if messagebox.askyesno(message = message, title = 'Salvar información profesional'):
				save_ui.save_profesional(
					self.write.get(), self.educative_assistance.get(), 
					self.institute_type_combo.get(), self.grade_institute_combo.get(),
					self.laboral_situation_combo.get()
				)
				save_ui.person_index += 1
				if save_ui.person_index < save_ui.total_persons_amount:
					parent.switch_frame(persons_ui.Persons)
				else:
					parent.switch_frame(end_ui.End)
	
	def update (self):
		"""
		Updates the grade values for the institute type combo based on the selected institute type.
		Refreshes the grade values every 1000 milliseconds.
		"""
		print(f'tipo de instituto: {self.institute_type_combo.get()}')
		
		if 'Pre-escolar' == self.institute_type_combo.get():
			self.grade_values = ['Prejardin','Jardin','Transición']
		elif 'Básica primaria' == self.institute_type_combo.get():
			self.grade_values = ['1','2','3','4','5']
		elif 'Básica secundaria' == self.institute_type_combo.get():
			self.grade_values = ['6','7','8','9']
		elif 'Media académica o clásica' == self.institute_type_combo.get() or 'Media técnica' == self.institute_type_combo.get():
			self.grade_values = ['10',11]
		elif 'Normalista' == self.institute_type_combo.get():
			self.grade_values = ['10','11','12','13']
		elif 'Técnica profesional' == self.institute_type_combo.get() or 'Tecnológica' == self.institute_type_combo.get() or 'Maestría' == self.institute_type_combo.get():
			self.grade_values = ['1','2','3']
		elif 'Universitaria' == self.institute_type_combo.get() or 'Doctorado' == self.institute_type_combo.get():
			self.grade_values = ['1','2','3','4','5','6']
		elif 'Especialización' == self.institute_type_combo.get():
			self.grade_values = ['1','2']
		else:
			self.grade_values = ['0']
		self.grade_institute_combo['values'] = self.grade_values
		self.grade_institute_combo.after(1000, self.update)
		
		
class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Class initialiser.
		
		Initialises the Application class by calling the Tk class constructor and setting the initial frame.
		
		Parameters:
		None
		
		Returns:
		None
		"""
		tk.Tk.__init__(self)
		self._frame = Profesional(self)
		self._frame.pack()

def main():
	"""
	Run the main application loop.

	:return: 0 indicating successful execution.
	"""
	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	main()
