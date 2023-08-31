# This code will convert any Armstron values to KeV for Xray fluxes. This is just for sanity reasons. 

from astropy import constants as const

wavelength= float(input("please enter the value in Amstrongs: "))
wavelength= wavelength/10**10
freq= (3e+8)/wavelength
print("The frequency is: ", freq)

joule_energy = 6.625e-34 *freq

kev_energy = joule_energy / 1.6022e-19

print("Energy is ",joule_energy, "J or ",kev_energy,"KeV")
