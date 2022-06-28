import astropy.units as u
from astropy.coordinates import EarthLocation, SkyCoord, AltAz, get_sun
from astropy.time import Time
import numpy as np

refractive_finitesize_offset = -50*u.arcmin
burton_tower = EarthLocation(lat=43.66066*u.deg, lon=-79.39849*u.deg, height=(113+48)*u.m)
utcoffset = -4*u.hr

suntimesarr = np.zeros((365,2),dtype=object)
delta_midnight = np.linspace(4,28,10000,endpoint=False)*u.hr

for i in range(0,5):
    times = Time('2022-01-01T00:00:00') + i*u.day + delta_midnight

    frame = AltAz(obstime=times, location=burton_tower)
    sun_altaz = get_sun(times).transform_to(frame)

    # sun size and refractive effect combined near horizon
    sunrise_idx, sunset_idx = np.where(np.diff(np.sign(sun_altaz.alt - refractive_finitesize_offset)) != 0)[0]
    pfit1 = np.polyfit([times[sunrise_idx].mjd,times[sunrise_idx+1].mjd],[(sun_altaz.alt+ 50*u.arcmin)[sunrise_idx].value,(sun_altaz.alt+ 50*u.arcmin)[sunrise_idx+1].value], 1)
    t1 = Time(-pfit1[1]/pfit1[0], format='mjd') + utcoffset
    pfit2 = np.polyfit([times[sunset_idx].mjd,times[sunset_idx+1].mjd],[(sun_altaz.alt+ 50*u.arcmin)[sunset_idx].value,(sun_altaz.alt+ 50*u.arcmin)[sunset_idx+1].value], 1)
    t2 = Time(-pfit2[1]/pfit2[0], format='mjd') + utcoffset
    #t1 = (times[sunrise_idx] + np.diff(delta_midnight)[0]/2 + utcoffset)
    #t2 = (times[sunset_idx] + np.diff(delta_midnight)[0]/2 + utcoffset)

    suntimesarr[i] = t1.isot, t2.isot
    print(i,suntimesarr[i])

np.savetxt("suntimes.csv", suntimesarr.astype(str), delimiter=",", fmt='%s')
