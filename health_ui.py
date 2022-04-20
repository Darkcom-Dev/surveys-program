import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Health(tk.Frame):
	""" Class doc """
	
	def __init__ (self, parent):
		""" Class initialiser """
		super().__init__(parent)
		self.illness_30_days_sentence = '''
¿En los ultimos 30 dias, tuvo alguna enfermedad, accidente, 
problema odontológico o algun otro problema de salud que no haya 
implicado hospitalización?
		'''
		self.limitation_sentence = '''
Dado su condición fisica y mental, y sin ningun tipo de ayuda,
¿en su vida diaria tiene dificultades para realizar actividades como:
Oir, hablar, ver, mover su cuerpo, caminar, agarrar objetos con sus 
manos, entender, aprender o recordar, comer o vestirse por si mismo e
interactuar con los demas?
		'''
		
		self.health_frame = ttk.LabelFrame(parent, text = 'Salud')
		self.health_frame.pack(fill = tk.X, padx = 5, pady = 5, ipady = 5)
		
		self.illness_30_days = tk.IntVar()
		self.illness_30_days_check = ttk.Checkbutton(self.health_frame, text = self.illness_30_days_sentence, variable = self.illness_30_days)
		self.illness_30_days_check.grid(row = 0, column = 0, columnspan = 2, sticky = 'WE', padx = 5)
		
		ttk.Label(self.health_frame,text = 'Para tratar ese problema de salud ¿Que hizo?').grid(row = 1, column = 0, sticky = 'WE', padx = 5)
		

		self.treatment_combo = ttk.Combobox(self.health_frame)
		self.treatment_combo.grid(row = 1, column = 1, sticky = 'WE', padx = 5)
		self.treatment_combo['state'] = 'readonly'
		self.treatment_combo['values'] = ['Acudió a la entidad de seguridad social en salud a la cual está afiliad@','Acudió a médico particular','Acudió a un boticario, farmaceuta, droguista','Asistió a terapias alternativas','Acudió a una autoridad indigena espiritual','Acudió a otro médico de un grupo etnico','Usó remedios caseros','Se autorrecetó','No hizo nada']
		
		self.attended = tk.IntVar()
		self.attended_check = ttk.Checkbutton(self.health_frame,text = '¿Lo atendieron?',variable = self.attended)
		self.attended_check.grid(row = 2, column = 0, sticky = 'WE', padx = 5)
		
		ttk.Label(self.health_frame,text = '¿Que tal fue la calidad del servicio de salud?').grid(row = 3, column = 0, sticky = 'WE', padx = 5)
		
		
		self.attention_quality_combo = ttk.Combobox(self.health_frame)
		self.attention_quality_combo.grid(row = 3, column = 1, sticky = 'WE', padx = 5)
		self.attention_quality_combo['state'] = 'readonly'
		self.attention_quality_combo['values'] = ['Muy bueno', 'Bueno', 'Malo', 'Muy malo']
		

		self.dificulties = tk.IntVar()
		self.dificulties_check = ttk.Checkbutton(self.health_frame,text = self.limitation_sentence, variable = self.dificulties)
		self.dificulties_check.grid(row = 5, column = 0, columnspan = 2, sticky = 'WE', padx = 5)
		
		self.handicap_button = ttk.Button(self.health_frame, text = 'Configurar handicap', command = self.configure_handicap)
		self.handicap_button.grid(row = 5, column = 1, sticky = 'SE', padx = 5)
		
		self.less10_frame = ttk.LabelFrame(parent, text = 'Para menores de 10 años')
		self.less10_frame.pack(fill = tk.X, padx = 5, pady = 5, ipady = 5)
		
		ttk.Label(self.less10_frame, text = '¿Con quién permanece durante la mayor parte del tiempo en semana?').pack(fill = tk.X, padx = 5, pady = 10)
		
		self.motive_combo = ttk.Combobox(self.less10_frame)
		self.motive_combo.pack(fill = tk.X, padx = 15)
		self.motive_combo['state'] = 'readonly'
		self.motive_combo['values'] = ['Asiste a un hogar comunitario, jardin, centro de desarrollo infantil', 'Con padre o madre en la vivienda','Con padre o madre en el trabajo','Con un pariente mayor de 18 años en la vivienda','Al cuidado de un pariente o persona menor de 18 años en la vivienda','Al cuidado de un pariente o de otra persona en otro lugar','En la vivienda solo']
		
		ttk.Button(parent, text = 'Siguiente ▶', command = self.message_data).pack(fill = tk.X, padx = 10, pady = 5)
		
	def configure_handicap (self):
		""" Function that call the Handicap Class """
		handicap = Handicap()
		
	def message_data (self):
		""" Function doc """
		message = f'''
Enfermedad en 30 dias: {'NO' if self.illness_30_days.get() == 0 else 'SI'}
Tratamiento: {self.treatment_combo.get()}
Atendido: {'NO' if self.attended.get() == 0 else 'SI'}
Calidad de atencion: {self.attention_quality_combo.get()}
Dificultades: {'NO' if self.dificulties.get() == 0 else 'SI'}
		
Motivo: {self.motive_combo.get()}
		'''
		if self.treatment_combo.get() == '':
			messagebox.showwarning(message = 'Tratamiento no tiene una selección válida', title = 'Error')
		elif self.attention_quality_combo.get() == '':
			messagebox.showwarning(message = 'Calidad de atención no tiene una selección válida', title = 'Error')
		elif self.motive_combo.get() == '':
			messagebox.showwarning(message = 'Motivo no tiene una selección válida', title = 'Error')
		else:
			messagebox.askyesno(message = message, title = 'Salvar salud')


class Handicap(tk.Toplevel):
	""" Class that get all handicaps data """
	
	def __init__ (self):
		""" Class initialiser """
		super().__init__()
		
		self.handicap_frame = ttk.LabelFrame(self, text = 'Discapacidades')
		self.handicap_frame.pack(fill = tk.X, padx = 5, pady = 5, ipady = 5)
		
		self.labels = ['Oir la voz o los sonidos','Hablar o conversar','Ver de cerca, de lejos o alrededor','Mover el cuerpo, caminar o subir y bajar escaleras','Agarrar o mover objetos con las manos','Entender, aprender, recordar o tomar decisiones por si mismo','Comer, vestirse o bañarse por si mismo','Relacionarse o interactuar con las demas personas','Hacer actividades diarias sin presentar problemas cardiacos, respiratorios']
		self.options = ['No puede hacerlo', 'Si, con mucha dificulties', 'Si, con alguna dificulties', 'Puede hacerlo sin dificulties']
		self.handicaps = []
		for l in range(len(self.labels)):
			ttk.Label(self.handicap_frame,text = self.labels[l]).grid(row = l, column = 0, columnspan = 2, sticky = 'WE', padx = 5)
			handicap = tk.StringVar()
			handicap_combo = ttk.Combobox(self.handicap_frame,textvariable = handicap)
			handicap_combo.grid(row = l , column = 1, sticky = 'WE', padx = 10)
			handicap_combo['state'] = 'readonly'
			handicap_combo['values'] = self.options
			self.handicaps.append(handicap)
		
		ttk.Label(self.handicap_frame, text = 'De las dificultades anteriores, ¿Cual es el que afecta su desempeño diario?').grid(row = len(self.labels) + 1, column = 0, sticky = 'WE', padx = 5, pady = 10)
		self.handicap = tk.StringVar()
		self.handicap_combo = ttk.Combobox(self.handicap_frame, textvariable = self.handicap)
		self.handicap_combo.grid(row = len(self.labels) + 1, column = 1, padx = 5)
		self.handicap_combo['state'] = 'readonly'
		self.handicap_combo['values'] = self.labels
		
		ttk.Label(self.handicap_frame, text = '¿Esta dificulties fue ocasionada por:?').grid(row = len(self.labels) + 2, column = 0, sticky = 'WE', padx = 5)
		self.motive = tk.StringVar()
		self.motive_combo = ttk.Combobox(self.handicap_frame, textvariable = self.motive)
		self.motive_combo.grid(row = len(self.labels) + 2, column = 1, sticky = 'WE', padx = 10)
		self.motive_combo['state'] = 'readonly'
		self.motive_combo['values'] = ['Porque nació así', 'Por enfermedad', 'Por accidente laboral o enfermedad profesional', 'Por otro tipo de accidente', 'Por edad avanzada', 'Por conflicto armado', 'Por violencia NO asociada al conflicto armado', 'Por otra causa', 'No sabe']
		
		
		ttk.Label(self.handicap_frame, text= 'Para esta dificultad usa permanentemente: ').grid(row = len(self.labels) + 3, column = 0, sticky = 'WE', padx = 5)
		
		self.ayudas_labels = ['Gafas, lentes, lupas, bastones, silla de ruedas, implantes, cocleares, entre otras','ayuda de otras personas', 'medicamentos o terapias', 'practicas de medicina ancestral']
		self.ayudas = []
		for l in range(len(self.ayudas_labels)):
			boolean = tk.IntVar()
			help_check = ttk.Checkbutton(self.handicap_frame,text = self.ayudas_labels[l], variable = boolean)
			help_check.grid(row = len(self.labels) + 4 + l, column = 0, sticky = 'WE', padx = 15)
			self.ayudas.append(boolean)
			
		

class Application(tk.Tk):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		tk.Tk.__init__(self)
		self._frame = Health(self)
		self._frame.pack()

def main(args):
	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
