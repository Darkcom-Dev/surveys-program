import json
import configparser as cp

config = cp.ConfigParser()
config.read('assets/config.cfg')


def save_dwelling_basic(normalized, direction, homes_amount, edification_use):
	dwelling_basic = {
		'normalized': normalized,
		'direction': direction,
		'homes': homes_amount,
		'edification': edification_use
					}

	print(f'Dwelling Basic: {dwelling_basic}')

def save_services (energy, stratum, sewerage, gas, garbage, garbage_times, aqueduct, toilette):
	""" Function doc """
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
	""" Function doc """
	# Mejorar el diseño de los datos
	
	characteristics = {
		'dwelling_type': dwelling_type,
		'predominant_material': predominant_material,
		'floors_material': floors_material
		}

	
	print(f'Caracteristicas: {characteristics}')

def save_georreferenciation (latitude, longitude):
	""" Function doc """
	georeferenciation = {
		'latitude': latitude,
		'longitude': longitude
	}
	print(f'Georeferentiation: {georeferenciation}')

def save_home(rooms, bedrooms, kitchen, water_source,deceased):
	home = {
		'rooms': rooms,
		'bedrooms': bedrooms,
		'kitchen': kitchen,
		'water_source': water_source,
		'deceased': deceased
	
	}
	print(f'Hogar: {home}')

def save_ticket(autoincrement,departament,province ):
	""" Function doc """
	ticket = {
	'ticket': autoincrement,
	'departament': departament,
	'province': province
	}
	print(f'Ticket: {ticket}')

def save_geopolitical(class_, aco, ao, ucr, location, neighborhood):
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

def save_history(living_time, floods, avalanche, earthquake, conflagration, storms, terrain_subsidence):
	history = {
		'time': living_time,
		'floods': floods,
		'earthquake': earthquake,
		'conflagration': conflagration,
		'storm': storms,
		'subsidence': terrain_subsidence
	}

def save_config (route):
	""" Function doc """
	config['Preconfig']['divipola'] = str(route)
	with open('assets/config.cfg', 'w') as cfg:
		config.write(cfg)

def load_config ():
	""" Function doc """
	
	print(f'Sections {config.sections()}')
	divipola = config.get('Preconfig', 'divipola')
	with open(divipola, 'r') as json_file:
		return json.load(json_file)
		
	

def main(args):
	
	# ~ save_dwelling_basic(True, 'CL 9b KR 8-12', 1, 'Vivienda Ocupada')
	# ~ save_dwelling_data('Casa','Marmol','Madera',1,'Medio-bajo',1,1,1,2,1,'Conectado al acueducto')
	# ~ save_georreferenciation(640 ,480)
	# ~ save_home(4,3, 'Rama al aire libre', 'Carrotanque', 1)
	
	# ~ save_location(12, 'Antioquia', 'El peñol', 'Urbano', '001', 196, '01', 'Centro', 'Sector Uno')
	
	return 0
	
geo_data = load_config()

if __name__ == '__main__':
	import sys
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
	

	
	sys.exit(main(sys.argv))
