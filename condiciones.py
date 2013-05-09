import numpy as np


#Genera las condiciones iniciales para los 120 cuerpos

No1=12.0
No2=18.0
No3=24.0
No4=30.0
No5=36.0
n1 =12
n2 =30
n3 =54
n4 =84
n5 =120

NoCuerpos = 120

G=4.3025e-3 #En parsecs, masas solares y km/s
M=10e12

radios = range(NoCuerpos)
angulos = range(NoCuerpos)
velocidades = range(NoCuerpos)

for i in range(0, n1):

	radios[i] = 1.0
	angulos[i] = i*2.0*np.pi/No1
	velocidades[i] = np.sqrt(G*M/1.0)

for i in range(n1, n2):
	
	radios[i] = 2.0
	angulos[i] = (i - n1)*2.0*np.pi/No2
	velocidades[i] = np.sqrt(G*M/2.0)

for i in range(n2, n3):
	
	radios[i] = 3.0
	angulos[i] = (i - n2)*2.0*np.pi/No3
	velocidades[i] = np.sqrt(G*M/3.0)

for i in range(n3, n4):
	
	radios[i] = 4.0
	angulos[i] = (i - n3)*2.0*np.pi/No4
	velocidades[i] = np.sqrt(G*M/4.0)

for i in range(n4, n5):
	
	radios[i] = 5.0
	angulos[i] = (i - n4)*2.0*np.pi/No5
	velocidades[i] = np.sqrt(G*M/5.0)

fx = open("radios.txt", "w")
for item in radios:
	fx.write("%f \n" % item)
fx.close()

fy = open("angulos.txt", "w")
for item in angulos:
	fy.write("%f \n" % item)
fy.close()

fz = open("velocidades.txt", "w")
for item in velocidades:
	fz.write("%f \n" % item)
fz.close()



