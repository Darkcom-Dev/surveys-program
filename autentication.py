#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ====================================================== Imports
import pandas as pd
# ====================================================== Class
# TODO: Eliminar pandas por json
def authenticate_password (user, password):
	"""
	Authenticates a user by checking their username and password against a JSON database.

	Parameters:
		user (str): The username to be authenticated.
		password (str): The password to be authenticated.

	Returns:
		bool: True if the user is authenticated, False otherwise.
	"""
	df = pd.read_json('assets/passwords.json')
	
	df_user = df.loc[df['user'] == user]
	
	if df_user.empty:
		print('Usuario no encontrado')
		return False
	else:
		print('Usuario encontrado')
		df_pass = df_user.loc[df_user['password'] == password]
		if df_pass.empty:
			print('Contraseña incorrecta')
			return False
			
		else:
			print('Usuario autenticado')
			return True

def authenticate_user(user):
	"""
	Checks if a user exists in the passwords.json file.

	Parameters:
		user (str): The username to be checked.

	Returns:
		bool: True if the user does not exist, False otherwise.
	"""
	
	df = pd.read_json('assets/passwords.json')
	df_user = df.loc[df['user'] == user]
	
	return df_user.empty

def create_user(user, password):
	"""
	Creates a new user by adding their username and password to the passwords.json file.

	Parameters:
		user (str): The username of the new user.
		password (str): The password of the new user.

	Returns:
		None
	"""
	
	df = pd.read_json('assets/passwords.json')
	
	if authenticate_user(user):
		df.loc[len(df.index)] = [user, password]
		df.to_json(r'assets/passwords.json')
	else:
		print('El usuario ya existe')

def change_password(user, password):
	pass
# ====================================================== Program Entry
def main():
	"""
	The main function that creates a user and returns an exit status.

	This function calls the `create_user` function to create a new user with the username 'Jose' and the password 'Asdf'. It then returns 0 as the exit status.

	Parameters:
		None

	Returns:
		int: The exit status of the program.
	"""

	create_user('Jose', 'Asdf')
	return 0

if __name__ == '__main__':
	main()
