#importing the visual component of python
from vpython import *

q1 = 3e-9           #positive charge in coloumb
q2 = -3e-9          #negative charge in coloumb
k = 9e9             #electric constant
f = 1e-8            #scale factor
d = 1e-3            #distance between the charges

#creating spheres to represent the charges
#positive charge
qplus=sphere(pos=vector(d/2,0,0), radius=5e-4, color=color.red)
#negative charge
qminus=sphere(pos=vector(-d/2,0,0), radius=5e-4, color=color.blue)

#observation position vector
obs=vector(0,5e-3,0)

#relative postion of observation location from each charge
rplus=obs-qplus.pos
rminus=obs-qminus.pos

#electric field due to postive charge on observation position
Eplus=k*q1*rplus/mag(rplus)**3
#electric field due to negative charge on observation position
Eminus=k*q2*rminus/mag(rminus)**3

#electric field of dipole at the observation position
Edipole=Eplus+Eminus

#printing the result
print('The electric field of dipole at the position is E_dipole = ',Edipole, 'N/C')

Etotarrow=arrow(pos=obs, axis=f*Edipole, color=color.yellow)
