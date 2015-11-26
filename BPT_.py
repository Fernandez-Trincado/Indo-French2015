#!/usr/bin/python                                                                                                                                                                                                                                                                             

# Created by: J. G. Fernandez-Trincado, Ayesha Anjum, Pritesh Ranadive
# Program description: ...


import numpy as np
import scipy as sc
import pylab as plt

data = sc.genfromtxt('shift.dat', dtype=str)

lines_ = [r'H$\alpha$',r'H$\beta$','[NII]','[OIII]']
N = 30

for i in np.arange(len(data[:,0])):

        #Ha, Hb, OIII, NII                                                                                                                                                                                                                                                                    
        line_ = [data[i,4], data[i,6], data[i,8], data[i,10]]

        if data[i,0] == "NODATA": pass

        else:
                print data[i,0]
                ratio = []
                f = plt.figure(int(i)+1,(15,25))


                sp = sc.genfromtxt(data[i,0])
                ax = f.add_subplot(5,1,1)
                ax.plot(sp[:,0], sp[:,1]-1,color='blue')
                ax.tick_params(labelsize = N)
#               ax.legend(prop={'size':35})                                                                                                                                                                                                                                                   
                ax.set_title(data[i,0]+'\n Z='+data[i,2],fontsize=N)

                for k in np.arange(len(lines_)):

                        print k+2
                        ax = f.add_subplot(5,1,k+2)
                        ax.plot(sp[:,0], sp[:,1]-1.)
                        ax.axvline(x=line_[k],color='red')

                        mask  = (sp[:,0] >= (float(line_[k])-12.) ) & ( sp[:,0] < float(line_[k]) )
                        flux  = sp[mask,1]-1
                        wlmin = sp[mask,0]
                        wlmin = wlmin[np.argsort(flux)][0]

                        mask  = (sp[:,0] > (float(line_[k])) ) & ( sp[:,0] <= float(line_[k]) + 12 )
                        flux  = sp[mask,1]-1
                        wlmax = sp[mask,0]
                        wlmax = wlmax[np.argsort(flux)][0]

                        integrate = (sp[:,0] >= wlmin) & (sp[:,0] <= wlmax)

                        ax.plot(sp[:,0],sp[:,1]-1)
                        ax.set_xlim(float(line_[k])-100.,float(line_[k])+100.)
                        ax.axvspan(wlmin,wlmax,facecolor='pink',alpha=0.4)
                        ax.text(wlmax+30, np.max(sp[:,1]-1)-0.5,lines_[k]+' = '+str( '%3.2f' %(np.sum(sp[integrate,1]))),fontsize=25)

                        ax.tick_params(labelsize = N)

                        ratio = np.append(ratio, np.sum(sp[integrate,1]))

                        if k == 3:

                                OIIIHbeta, NIIHalpha = '%3.2f' %(np.log(ratio[3]/ratio[1])/np.log(10.)), '%3.2f' %(np.log(ratio[2]/ratio[0])/np.log(10.))
                                ax.text(wlmin-80, 0.5,'log([OIII]/Hbeta) = '+str(OIIIHbeta)+'\n log([NII]/Halpha) = '+str(NIIHalpha),fontsize=25)


                #plt.show()                                                                                                                                                                                                                                                                   
                plt.savefig(data[i,0]+'.png')


