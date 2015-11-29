#!/usr/bin/python


import numpy as np
import scipy as sc
import pylab as plt

data = sc.genfromtxt('shift.dat', dtype=str) 

lines_ = [r'H$\alpha$',r'H$\beta$','[OIII]','[NII]']
N = 30


LWL = [10., 20.]

for i in np.arange(len(data[:,0])):

	#Ha, Hb, OIII, NII
	corr = (1.+float(data[i,2])) 
	line_ = [float(data[i,3])*corr, float(data[i,4])*corr, float(data[i,6])*corr, float(data[i,5])*corr]

	if data[i,0] == "NODATA": pass

	else:
		ratio = []
		f = plt.figure(int(i)+1,(15,25))


		sp = sc.genfromtxt(data[i,0])
		ax = f.add_subplot(5,1,1)
		ax.plot(sp[:,0], sp[:,1]-1,color='blue')
		ax.tick_params(labelsize = N)
#		ax.legend(prop={'size':35})
		ax.set_title('Galaxy '+str(int(i)+1)+'\n Z='+data[i,2],fontsize=N)
	
		for ko in np.arange(len(line_)): 
			ax.axvline(x=line_[ko],color='red')
			
			if (ko == 0) | (ko==2):	
				ax.text(line_[ko],np.max(sp[:,1]-1)-0.5,lines_[ko])
			
			if (ko == 1) | (ko==3):
				ax.text(line_[ko],np.max(sp[:,1]-1)-1.5,lines_[ko])

		for k in np.arange(len(lines_)):

			ax = f.add_subplot(5,1,k+2)
			ax.plot(sp[:,0], sp[:,1]-1.)	
			ax.axvline(x=line_[k],color='red')

			if i == 9: 
				LWL2 = LWL[1]
			else: 
				LWL2 = LWL[0]			

			mask  = (sp[:,0] >= (float(line_[k])-LWL2) ) & ( sp[:,0] < float(line_[k]) )
			flux  = sp[mask,1]-1
			wlmin = sp[mask,0]
			wlmin = wlmin[np.argsort(flux)][0]

			mask  = (sp[:,0] > (float(line_[k])) ) & ( sp[:,0] <= float(line_[k]) + LWL2 )
			flux  = sp[mask,1]-1
			wlmax = sp[mask,0]
			wlmax = wlmax[np.argsort(flux)][0]

			integrate = (sp[:,0] >= wlmin) & (sp[:,0] <= wlmax)
			integrate_flux = np.sum(sp[integrate,1]-1)


			ax.plot(sp[:,0],sp[:,1]-1)		
			ax.set_xlim(float(line_[k])-100.,float(line_[k])+100.)
			ax.axvspan(wlmin,wlmax,facecolor='pink',alpha=0.4)
			ax.text(wlmax+30, np.max(sp[:,1]-1)-0.5,lines_[k]+' = '+str( '%3.2f' %(integrate_flux)),fontsize=25)

			ax.tick_params(labelsize = N)

			ratio = np.append(ratio, np.sum(sp[integrate,1]))

			if k == 3:

				OIIIHbeta, NIIHalpha = '%3.2f' %(np.log(ratio[3]/ratio[1])/np.log(10.)), '%3.2f' %(np.log(ratio[2]/ratio[0])/np.log(10.))		
				ax.text(wlmin-80, np.max(sp[:,1]-1)-1.5,'log([OIII]/Hbeta) = '+str(OIIIHbeta)+'\n log([NII]/Halpha) = '+str(NIIHalpha),fontsize=25)
				ax.set_xlabel(r'$\lambda$ (Angstrom)',fontsize=N)
				print NIIHalpha, OIIIHbeta, data[i,2]

#		plt.show()
		plt.savefig(data[i,0]+'.png')





