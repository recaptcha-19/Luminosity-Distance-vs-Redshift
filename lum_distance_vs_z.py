import astropy.units as u
from astropy.constants import c
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.integrate import quad

rc('text', usetex = True)
def f(x, omega_m):
    return 1/(omega_m*(1+x)**3 + 1 - omega_m)

Mpc = 10**6*u.pc
data = np.genfromtxt('SCPUnion2.1_mu_vs_z.txt')
z = data.T[1]
dm = data.T[2]
error_dm = data.T[3]

lum_distance = 10**(dm/5 + 1)
lum_distance *= u.pc
lum_distance = lum_distance.to(Mpc)
#obtaining Hubble plots
c = c.to(u.km/u.s)
H0 = 72*u.km/(u.s*u.Mpc)
dL = np.zeros(len(z))

def luminosity_distance(omega_m):
    for i in range(len(z)):
        rem = quad(f, 0, z[i], args = (omega_m))
        dL_value = (1 + z[i])*rem[0]*c.value/H0.value
        dL[i] = dL_value
    return dL

plt.scatter(z, lum_distance.value, s = 3, c = 'black', label = 'Observed $d_L$')
omega_m = [0, 0.1, 0.5, 1]
for omega in omega_m:
    dL = luminosity_distance(omega)
    indices = np.argsort(dL)
    z = z[indices]
    dL = dL[indices]
    plt.plot(z, dL, label = '$\Omega_m = {}$'.format(omega))
plt.xlabel('Redshift(z)')
plt.ylabel('Luminosity distance $d_L$ (Mpc)')
plt.title('Luminosity distance vs redshift for type 1a supernovae')
plt.legend()
plt.savefig('Luminosity_distance_vs_redshift.png')
plt.show()
