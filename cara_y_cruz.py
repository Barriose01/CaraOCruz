#--------------------------CARA Y CRUZ---------------------------------#
# 31/07/2021
# Santiago, Chile
# Eddie Casañas

import random as rd

def generadorRandom():
	numero = rd.randint(1,2)
	if numero == 1:
		return "cara"
	elif numero == 2:
		return "cruz"
		
def juego():
	while True:
		print("(1): Cara")
		print("(2): Cruz")
		opcion = input()
		if opcion.strip() != "1" and opcion.strip() != "2":
			continue
		else:
			break
	if opcion.strip() == "1":
		usuario = "cara"
		maquina = generadorRandom()
		if usuario == maquina:
			print("\nGANASTE. APARECIO CARA\n")
		elif usuario != maquina:
			print("\nLO SENTIMOS. APARECIO CRUZ\n")
			
	elif opcion.strip() == "2":
		usuario = "cruz"
		maquina = generadorRandom()
		if usuario == maquina:
			print("\nGANASTE. APARECIO CRUZ\n")
		elif usuario != maquina:
			print("\nLO SENTIMOS. APARECIO CARA\n")
				
def salida():
	print("(1): Volver a jugar")
	print("(2): Salir")
	
	salir = input()
	if salir.strip() == "1":
		juego()
	elif salir == "2":
		return 0
		

juego()
while True:
	salida2 = salida()
	if salida2 == 0:
		break
	else:
		continue
	
	
