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


if __name__ == '__main__':

    step = 0.2
    mags = np.arange(21.5, 24.5+step, step)
    print 'mag, exptime (snr 20) g, r, i ,z'
    for mag in mags:
        print '%.1f, %.1f, %.1f, %.1f, %.1f' % (mag, spi_etc(mag, snr=20., filtername='g')[0], spi_etc(mag, snr=20., filtername='r')[0],
                                    spi_etc(mag, snr=20., filtername='i')[0],spi_etc(mag, snr=15., filtername='z')[0])
