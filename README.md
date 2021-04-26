# Hubble Plots

This contains graphs of the variation of luminosity distance vs redshift for Type 1a supernovae for different cosmologies.

# Introduction

Type 1a supernovae serve as one of the rungs of the cosmic distance ladder by which distances can be estimated to objects. They serve as standard candles since their intrinsic luminosity and light curves are nearly uniform for all supernovae (or can be corrected for). 

The luminosity distance of an astronomical object is defined in terms of the distance modulus:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?D_L%20%3D%2010%5E%7B%5Cfrac%7Bm-M%7D%7B5%7D%20&plus;%201%7D" />
</p>

where ![](https://latex.codecogs.com/gif.latex?m) and ![](https://latex.codecogs.com/gif.latex?M) refer to *apparent* and *absolute* magnitudes respectively. 

It is also defined in terms of the flux and luminosity of the object:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?D_L%20%3D%20%5Csqrt%7B%5Cfrac%7BL%7D%7B4%5Cpi%20F%7D%7D" />
</p>

In terms of the scale factor and comoving distance for a particular cosmology, it is obtained as  

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?D_L%20%3D%20a_0r_%7Bem%7D%28z%29%281&plus;z%29" />
</p>

For a spatially flat cosmology, ![](https://latex.codecogs.com/gif.latex?r_%7Bem%7D%28z%29%20%3D%20S_k%28%5Calpha%29%20%3D%20%5Calpha), where 

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Calpha%20%3D%20%5Cint_0%5Ez%20%5Cfrac%7Bdz%7D%7Ba_0H%28z%29%7D" />
</p>
and ![](https://latex.codecogs.com/gif.latex?H%28z%29) and hence the comoving distance is obtained for different spatially flat, matter dominated cosmologies with a cosmological constant in terms of the density parameters today, i.e. ![](https://latex.codecogs.com/gif.latex?%5COmega_%7Bm0%7D) and ![](https://latex.codecogs.com/gif.latex?%5COmega_%7B%5CLambda0%7D). The luminosity distance then becomes

 <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?d_L%20%3D%20%5Cfrac%7Bc%281&plus;z%29%7D%7BH_0%7D%20%5Cint_0%5Ez%20%5Cfrac%7Bdz%7D%7B%5Csqrt%7B%5COmega_%7Bm0%7D%281&plus;z%29%5E3%20&plus;%201%20-%20%5COmega_%7Bm0%7D%7D%7D" />
</p>

# Procedure and Data

* The plot is obtained by assuming different values of ![](https://latex.codecogs.com/gif.latex?%5COmega_%7Bm0%7D), computing the luminosity distance and plotting it against the redshift of the said supernova. The [dataset](https://github.com/recaptcha-19/Luminosity-Distance-vs-Redshift/blob/master/SCPUnion2.1_mu_vs_z.txt) is obtained from the [Supernova Cosmology Project](http://www-supernova.lbl.gov/).

* Different curves corresponding to different ![](https://latex.codecogs.com/gif.latex?%5COmega_%7Bm0%7D) are obtained. Check ```lum_distance_vs_z.py```.

# Remarks

The plot assumes three different matter dominated cosmologies with a cosmological constant with arbitrary values of ![](https://latex.codecogs.com/gif.latex?%5COmega_%7Bm0%7D). Further scope would be to obtain a perfect value of ![](https://latex.codecogs.com/gif.latex?%5COmega_%7Bm0%7D) by performing regression and obtain the best estimate of the current cosmology and possibly the Hubble constant as well. 


