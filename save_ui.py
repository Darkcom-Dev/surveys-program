import json
import configparser as cp
from datetime import datetime

config = cp.ConfigParser()
config.read('assets/config.cfg')
today = datetime.today()

person_list = list()
personal_data_list = list()
health_list = list()
profesional_list = list()
age = 0
total_persons_amount = 0
person_index = 0

def save_dwelling_basic(normalized, direction, homes_amount, edification_use):
	"""
	Saves the basic information of a dwelling.

	Parameters:
		normalized (str): The normalized value of the dwelling.
		direction (str): The direction of the dwelling.
		homes_amount (int): The amount of homes in the dwelling.
		edification_use (str): The edification use of the dwelling.

	Returns:
		None
	"""
	dwelling_basic = {
		'normalized': normalized,
		'direction': direction,
		'homes': homes_amount,
		'edification': edification_use
					}

	print(f'Dwelling Basic: {dwelling_basic}')

def save_services (energy, stratum, sewerage, gas, garbage, garbage_times, aqueduct, toilette):
	"""
	Saves the services information for a dwelling.

	Parameters:
		energy (str): The type of energy used in the dwelling.
		stratum (str): The stratum of the dwelling.
		sewerage (str): The type of sewerage system used in the dwelling.
		gas (str): The type of gas used in the dwelling.
		garbage (str): The type of garbage collection used in the dwelling.
		garbage_times (str): The schedule for garbage collection.
		aqueduct (str): The type of aqueduct system used in the dwelling.
		toilette (str): The type of toilette system used in the dwelling.

	Returns:
		None
	"""
	services = {
		'energy': energy,
		'stratum': stratum,
		'sewerage': sewerage,
		'gas':gas,
		'garbage': garbage,
		'garbage': garbage_times,
		'aqueduct': aqueduct,
		'toilette': toilette
	}
	
	print(f'Servicios: {services}')

def save_dwelling_characteristics (dwelling_type, predominant_material, floors_material):
	"""
	Saves the characteristics of a dwelling.

	Parameters:
		dwelling_type (str): The type of dwelling.
		predominant_material (str): The predominant material of the dwelling.
		floors_material (str): The material of the floors.

	Returns:
		None
	"""
	
	characteristics = {
		'dwelling_type': dwelling_type,
		'predominant_material': predominant_material,
		'floors_material': floors_material
		}
	
	print(f'Caracteristicas: {characteristics}')

def save_georreferenciation (latitude, longitude):
	"""
	Saves georeferenciation data.

	Parameters:
		latitude (float): The latitude coordinate.
		longitude (float): The longitude coordinate.

	Returns:
		None
	"""
	georeferenciation = {
		'latitude': latitude,
		'longitude': longitude
	}
	print(f'Georeferentiation: {georeferenciation}')

def save_home(rooms, bedrooms, kitchen, water_source,deceased):
	"""
	Saves a home with its characteristics.

	Parameters:
		rooms (int): The number of rooms in the home.
		bedrooms (int): The number of bedrooms in the home.
		kitchen (str): The type of kitchen in the home.
		water_source (str): The source of water for the home.
		deceased (str): The information about deceased people in the home.

	Returns:
		None
	"""
	home = {
		'rooms': rooms,
		'bedrooms': bedrooms,
		'kitchen': kitchen,
		'water_source': water_source,
		'deceased': deceased
	}
	print(f'Hogar: {home}')

def save_ticket(autoincrement,departament,province ):
	"""
	Saves a ticket with the provided autoincrement, departament, and province values.

	Parameters:
		autoincrement (int): The auto-incremented ID of the ticket.
		departament (str): The departament associated with the ticket.
		province (str): The province associated with the ticket.

	Returns:
		None
	"""
	ticket = {
	'ticket': autoincrement,
	'departament': departament,
	'province': province
	}
	print(f'Ticket: {ticket}')

def save_geopolitical(class_, aco, ao, ucr, location, neighborhood):
	"""
	Saves a dictionary of geopolitical data with the following categories: class, aco, ao, ucr, location, and neighborhood.

	Parameters:
		class_ (any): The value of the class.
		aco (any): The value of the aco.
		ao (any): The value of the ao.
		ucr (any): The value of the ucr.
		location (any): The value of the location.
		neighborhood (any): The value of the neighborhood.

	Returns:
		None
	"""
	geopolitical = {
	'class': class_,
	'aco': aco,
	'ao': ao,
	'ucr': ucr,
	'location': location,
	'neighborhood': neighborhood
	}
	
	print(f'Geopolitico: {geopolitical}')

def save_goods(freezer, laundry, computer, motorcycle, tractor, car, realstate):
	"""
	Saves a dictionary of goods with the following categories: freezer, laundry, computer, motorcycle, tractor, car, and realstate.

	Parameters:
		freezer (any): The value of the freezer.
		laundry (any): The value of the laundry.
		computer (any): The value of the computer.
		motorcycle (any): The value of the motorcycle.
		tractor (any): The value of the tractor.
		car (any): The value of the car.
		realstate (any): The value of the realstate.

	Returns:
		None
	"""
	goods = {
		'freezer': freezer,
		'laundry': laundry,
		'computer': computer,
		'motorcycle': motorcycle,
		'tractor': tractor,
		'car': car,
		'realstate': realstate
	}

def save_spends(feeding, transport, education, health, public_services, mobile, rent, other_expenses):
	"""
	Saves a dictionary of spends with the following categories: feeding, transport, education, health, public services, mobile, rent, and other expenses.

	Parameters:
		feeding (any): The amount spent on feeding.
		transport (any): The amount spent on transport.
		education (any): The amount spent on education.
		health (any): The amount spent on health.
		public_services (any): The amount spent on public services.
		mobile (any): The amount spent on mobile.
		rent (any): The amount spent on rent.
		other_expenses (any): The amount spent on other expenses.

	Returns:
		dict: A dictionary containing the spends with their respective categories.
	"""
	spends = {
		'feeding': feeding,
		'transport': transport,
		'education': education,
		'health': health,
		'public_services': public_services,
		'mobile': mobile,
		'rent': rent,
		'other': other_expenses
	}

def save_health(illness_30_days, treatment, attended, attention_quality, dificulties, motive):
	health = {
		'illness 30d' : illness_30_days,
		'treatment' : treatment,
		'attended' : attended,
		'attention quality' : attention_quality,
		'dificulties' : dificulties,
		'motive' : motive	
	}
	health_list.append(health)
	
def save_profesional (know_read, assist_institute, institute_type, grade, activity):
	"""
	Saves a profesional's information.

	Parameters:
		know_read (str): Whether the profesional knows how to read.
		assist_institute (str): The institute that the profesional assists.
		institute_type (str): The type of institute that the profesional assists.
		grade (str): The profesional's grade.
		activity (str): The profesional's activity.

	Returns:
		None
	"""
	profesional = {
		'read' : know_read,
		'assist institute' : assist_institute,
		'type' : institute_type,
		'grade' : grade,
		'activity' : activity
	}
	profesional_list.append(profesional)

def save_history(living_time, floods, avalanche, earthquake, conflagration, storms, terrain_subsidence):
	"""
	Saves the history data.

	Parameters:
		living_time (str): The time of living.
		floods (str): The number of floods.
		avalanche (str): The number of avalanches.
		earthquake (str): The number of earthquakes.
		conflagration (str): The number of conflagrations.
		storms (str): The number of storms.
		terrain_subsidence (str): The number of terrain subsidence.

	Returns:
		dict: A dictionary containing the history data.
	"""
	history = {
		'time': living_time,
		'floods': floods,
		'earthquake': earthquake,
		'conflagration': conflagration,
		'storm': storms,
		'subsidence': terrain_subsidence
	}

def save_config (route):
	"""
	Saves the configuration data to a file.

	Parameters:
		route (str): The route value to be saved in the configuration.

	Returns:
		None
	"""
	config['Preconfig']['divipola'] = str(route)
	with open('assets/config.cfg', 'w') as cfg:
		config.write(cfg)

def save_persons (gender, unknow_bird, born_date, document_type, document_number, head_household_relationship, culture):
	"""
	Saves a person's data into a dictionary and appends it to the personal_data_list.

	Parameters:
		gender (str): The person's gender.
		unknow_bird (str): The person's unknow bird.
		born_date (str): The person's born date.
		document_type (str): The person's document type.
		document_number (str): The person's document number.
		head_household_relationship (str): The person's head household relationship.
		culture (str): The person's culture.

	Returns:
		None
	"""
	person = dict()
	person['gender'] = gender
	person['unknow bird'] = unknow_bird
	person['born date'] = born_date
	person['document type'] = document_type
	person['document number'] = document_number
	person['head household relationship'] = head_household_relationship
	person['culture'] = culture
	
	personal_data_list.append(person)

def load_config ():
	"""
	Loads configuration from a file.

	Parameters:
		None

	Returns:
		A dictionary containing the configuration data.
	"""
	
	print(f'Sections {config.sections()}')
	divipola = config.get('Preconfig', 'divipola')
	with open(divipola, 'r') as json_file:
		return json.load(json_file)
		
	

def main():
	
	# ~ save_dwelling_basic(True, 'CL 9b KR 8-12', 1, 'Vivienda Ocupada')
	# ~ save_dwelling_data('Casa','Marmol','Madera',1,'Medio-bajo',1,1,1,2,1,'Conectado al acueducto')
	# ~ save_georreferenciation(640 ,480)
	# ~ save_home(4,3, 'Rama al aire libre', 'Carrotanque', 1)
	# ~ save_location(12, 'Antioquia', 'El peñol', 'Urbano', '001', 196, '01', 'Centro', 'Sector Uno')
	
	return 0
	
geo_data = load_config()

if __name__ == '__main__':

	history = None
	spends = None
	goods = None
	geopolitical = None
	ticket = None
	home = None
	georreferenciation = None
	characteristics = None
	services = None
	dwelling_basic = None
	deseased_list = None
	
	main()
