#!/usr/bin/python


import numpy as np
import scipy as sc
import pylab as plt
from matplotlib import cm as CM

data = sc.genfromtxt('lines_ratios.dat')
data1 = sc.genfromtxt('gal_line_dr7_v5_2.fit.txt') # Input --->

'''Input ---> SDSS Line-ratio Diagram. The gray shading represents the entire galaxy sample from http://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/SDSS_line.html#Line_Name, and "The spectroscopic data is in gal_line and the content is described here. This file contain line fluxes (in units of 1e-17 erg/s/cm^2), equivalent widths and continuum fluxes. 678Mb" http://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/raw_data.html while the red square open symbols are the AGN sample analized in this project.
'''

N =20

f=plt.figure(1)

X = np.linspace(-1.5,0.3)

Y = (0.61/( X  - 0.47  )) + 1.19

X3 = np.linspace(-0.180,1.5)
Y3 = 1.05*X3 + 0.45

Xk = np.linspace(-1.5,0.)
Yk = 0.61/(Xk -0.05) + 1.3

yy, xx = np.log(data1[:,1]/data1[:,0])/np.log(10.) ,  np.log(data1[:,3]/data1[:,2])/np.log(10.)

#plt.plot(xx,yy,'.')

a1=f.add_subplot(1,1,1)

hist,xedges,yedges = np.histogram2d(xx,yy,bins=(60,60),range=[[-1.2,1.2],[-1.5,1.0]])
aspectratio = 1.0*(2.5)/(2.4)
masked = np.ma.masked_where(hist==0, hist)
a=a1.imshow(masked.T,extent=[-1.2,1.2,-1.5,1.0],interpolation='nearest',origin='lower', aspect=aspectratio,cmap=plt.cm.gray_r)
#a_=plt.colorbar(a,shrink=1.)
levels = np.linspace(0., np.log10(masked.max()), 5)[1:]
CS     = a1.contour(np.log10(masked.T), levels, colors='k',linewidths=1,extent=[-1.2,1.2,-1.5,1.0])



#ax=f.add_subplot(1,1,1)
#hex=ax.hexbin(data[:,0],data[:,1],data[:,2],gridsize=5,cmap=CM.jet)
#cb=f.colorbar(hex)
#cb.set_label('Z',fontsize=N)
a1.plot(X, Y, '-',color='magenta',lw=3,label='Kewley+01')
a1.set_xlim(-1.2, 1.0)
a1.set_ylim(-1.2, 1.0)
a1.set_xlabel(r'log([NII] $\lambda$ 6583/H$\alpha$)',fontsize=N)
a1.set_ylabel(r'log([OIII] $\lambda$ 5007/H$\beta$)',fontsize=N)
##
a1.plot(X3,Y3,'-.',color='magenta',lw=5,label='Schawinski+07')
a1.plot(Xk, Yk,'--',color='magenta',lw=5,label='Kauffmann+03')
##ax.plot(X1,Y1,'s',ms=15, fillstyle='none')
a1.tick_params(labelsize = N)

shape = ['s','o','+','x','^']

for i in np.arange(len(shape)):

	a1.plot(data[i,0],data[i,1],shape[i],mew=3,ms=15,fillstyle='none',color='blue',label='Galaxy'+str(int(i)+1))

a1.legend(numpoints=1,loc=4)


a1.text(-1.0,-1.0,'star-forming'+'\n dominated',color='black',fontsize=25)
a1.text(0.5,0.,'LINER',color='black',fontsize=25)
a1.text(-0.25,0.75,'Seyfert 2',color='black',fontsize=25)

plt.show()
