import numpy as np
from matplotlib import pyplot as plt
from astropy.io import fits

###############
###
###  INPUT REQUIRED: ...-noise-cube.fits (cube)
###  OUTPUT:         ascii-table and plot with noise spectrum.
###
###############


# User input
image_file = "SPT2349-CII-cy5cy8-cube-noise.fits"

# Load data
image_data = fits.getdata(image_file, ext=0, memmap=False)[0] # remove polarisation

hdu = fits.open(image_file)
image_header = hdu[0].header

### Get frequency grid from fits cube header info
def grid_from_header(header):
    n = int(header['NAXIS3']) # number of channels
    k = header['CDELT3'] # frequency step
    d = int(header['CRPIX3']) # channel offset
    y0 = header['CRVAL3'] # frequency offset
    x = np.linspace(1,n,n) # grid
    return k*(x-d)+y0

# Extract specturm
noise_spec = image_data[:,1,1]

# Convert frequency axis
freq = grid_from_header(image_header)/1E9

# Plot spectrum
fig,ax = plt.subplots()
ax.step(freq,noise_spec,where="pre",label=str(image_file))

# Show second as with numbered channels
ax2 = ax.twiny()
ax2.plot(np.linspace(1,len(freq),len(freq)),np.zeros(len(freq)))
#ax2.cla()

ax.set_ylim([np.min(noise_spec)*0.9,np.max(noise_spec)*1.03])
#ax.set_ylim([0.0,np.max(noise_spec)*1.03])

ax.legend()
plt.savefig(str(image_file)+"_diagnostic.png")

# Write ascii spectrum to disk
np.savetxt(image_file+".ascii",np.transpose([freq,noise_spec]), header="GHz           Jy" )