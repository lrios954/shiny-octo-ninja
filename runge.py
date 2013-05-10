
import pylab
import numpy

#X es velocidad angular y Y es angulo

data1 = numpy.loadtxt(open('radios.txt', 'r'))
radios = data1[:]
data2 = numpy.loadtxt(open('angulos.txt', 'r'))
theta = data2[:]
data3 = numpy.loadtxt(open('velocidades.txt', 'r'))
v = data3[:]

tMax = 2000000000 #Para diferenciales de tiempo de 100 mil anios
h = 100000 #Diferencial de tiempo
   
x = range(tMax)
y = range(tMax)
t = range(tMax)

G=4.3025e-3 #En parsecs, masas solares y km/s
M=10e12

def v_prime(x, y, r):
	return G*M/(r**2)

def r_prime(x, y, r):
	return x

def rungekutta(x, y, i, t, r):

	#X corresponde a la velocidad angular
  	kx1 = v_prime(x[i-1],y[i-1], r)
	#Y corresponde al angulo
	ky1 = r_prime(x[i-1],y[i-1], r)
  
  
 	#first step
	t1 = t[i-1] + (h/2.0)
	x1 = x[i-1] + (h/2.0) * kx1
	y1 = y[i-1] + (h/2.0) * ky1
  
	kx2 = v_prime(x1, y1, r)
	ky2 = r_prime(x1, y1, r)
  
	#second step
	t2 = t[i-1] + (h/2.0);
	x2 = x[i-1] + (h/2.0) * kx2
	y2 = y[i-1] + (h/2.0) * ky2
  
	kx3 = v_prime(x2, y2, r)
	ky3 = r_prime(x2, y2, r)
  
	#third step
	t3 = t[i-1] + h
	x3 = x[i-1] + h * kx3
	y3 = y[i-1] + h * ky3
  
	kx4 = v_prime(x3, y3, r)
	ky4 = r_prime(x3, y3, r)
  
  
	#fourth step
	average_kx = (1.0/6.0)*(kx1 + 2.0*kx2 + 2.0*kx3 + kx4)
	average_ky = (1.0/6.0)*(ky1 + 2.0*ky2 + 2.0*ky3 + ky4)
  
  
	t[i] = t[i-1] + h
	x[i] = x[i-1] + h * average_kx
	y[i] = y[i-1] + h * average_ky


for j in range(0, 120):
	x[0] = v[j]
	y[0] = theta[j]
	r = radios[j]
	
	f = open(str(j) + ".txt", "w")
	for i in range(5):
		rungekutta(x, y, i, t, r)
		f.write("%f %f \n" % (x[0], y[0]))
	f.close()
	
	
