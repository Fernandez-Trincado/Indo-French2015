#!/usr/bin/python


import numpy as np
import scipy as sc
import pylab as plt
from matplotlib import cm as CM

data = sc.genfromtxt('red.dat')
data1 = sc.genfromtxt('gal_line_dr7_v5_2.fit.txt')



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
levels = np.linspace(0., np.log10(masked.max()), 10)[1:]
CS     = a1.contour(np.log10(masked.T), levels, colors='k',linewidths=1,extent=[-1.2,1.2,-1.5,1.0])



#ax=f.add_subplot(1,1,1)
plt.plot(data[:,0],data[:,1],'s',mew=3,ms=15,fillstyle='none',color='red')
#hex=ax.hexbin(data[:,0],data[:,1],data[:,2],gridsize=5,cmap=CM.jet)
#cb=f.colorbar(hex)
#cb.set_label('Z',fontsize=N)
plt.plot(X, Y, '-',color='blue',lw=3,label='Kewley+01')
plt.xlim(-1.2, 1.0)
plt.ylim(-1.2, 1.0)
plt.xlabel(r'log([NII] $\lambda$ 6583/H$\alpha$)',fontsize=N)
plt.ylabel(r'log([OIII] $\lambda$ 5007/H$\beta$)',fontsize=N)
##
plt.plot(X3,Y3,'-.',color='blue',lw=3,label='Schawinski+07')
plt.plot(Xk, Yk,'--',color='blue',label='Kauffmann+03')
##ax.plot(X1,Y1,'s',ms=15, fillstyle='none')
plt.tick_params(labelsize = N)
plt.legend(loc=3)
#
#
#
#
plt.show()



