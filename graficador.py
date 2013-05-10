from pylab import *
import matplotlib.pyplot as plt
import numpy as np

nCuerpos = 120


fig0 = plt.figure()
fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
fig4 = plt.figure()

for i in range(nCuerpos):
	data = np.loadtxt(open(str(i)+'.txt', 'r'))
	v = data[:,0]
	theta = data[:,1]
	radio = data[:,2]

	ax0 = fig0.add_axes([0.1,0.1,0.8,0.8],polar=True)
	ax0.scatter(theta[0], radio[0]) 

	ax1 = fig1.add_axes([0.1,0.1,0.8,0.8],polar=True)
	ax1.scatter(theta[1], radio[1]) 
	
	ax2 = fig2.add_axes([0.1,0.1,0.8,0.8],polar=True)
	ax2.scatter(theta[2], radio[2]) 
	
	ax3 = fig3.add_axes([0.1,0.1,0.8,0.8],polar=True)
	ax3.scatter(theta[3], radio[3]) 

	ax4 = fig4.add_axes([0.1,0.1,0.8,0.8],polar=True)
	ax4.scatter(theta[4], radio[4]) 
	

fig0.savefig('galaxiaT0.png')
fig1.savefig('galaxiaT1.png')
fig2.savefig('galaxiaT2.png')
fig3.savefig('galaxiaT3.png')
fig4.savefig('galaxiaT4.png')





