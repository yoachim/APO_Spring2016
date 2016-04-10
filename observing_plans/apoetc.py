import numpy as np

def spi_etc(mag, snr=10., filtername='r'):
    """
    Very simple etc based on spicam values

    stolen from Jim at: https://github.com/jradavenport/jradavenport_idl/blob/master/apoexpcal.pro
    """
    spi_filters = np.array(['u','g','r','i','z'])
    spi_c = np.array([21.38,24.92,24.93,24.72,23.43])
    spi_K = [.48,.19,.11,.04,.06]
    fm=np.where(spi_filters == filtername)[0]
    spi_flux = 10.**((mag-spi_c[fm])/(-2.5))
    exptime = snr**2./spi_flux
    return exptime
