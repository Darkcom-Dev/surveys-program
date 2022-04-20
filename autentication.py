#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ====================================================== Imports
import pandas as pd
# ====================================================== Class


# ====================================================== Program Entry

def authenticate_password (user, password):
	""" Function doc """
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
	
	df = pd.read_json('assets/passwords.json')
	df_user = df.loc[df['user'] == user]
	
	return df_user.empty

def create_user(user, password):
	
	df = pd.read_json('assets/passwords.json')
	
	
	if authenticate_user(user):
		df.loc[len(df.index)] = [user, password]
		df.to_json(r'assets/passwords.json')
	else:
		print('El usuario ya existe')

def change_password(user, password):
	pass

def main(args):
	create_user('Jose', 'Asdf')
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
