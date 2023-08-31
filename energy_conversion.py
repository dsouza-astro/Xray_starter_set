# This code will convert any Armstron values to KeV for Xray fluxes. This is just for sanity reasons. 

from astropy import constants as const

wavelength= input("please enter the value in Amstrongs: ")

freq= (const.c*10**10)/wavelength
print("The frequency is: ", freq)

joule_energy = 6.625E+34 *freq

kev_energy = joule_energy * 6.242E+15

print("Energy is ",joule_energy, "J or ",kev_energy,"KeV")
