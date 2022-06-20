import astropy.units as u
from astropy.coordinates import EarthLocation, SkyCoord, AltAz, get_sun

burton_tower = EarthLocation(lat=43.66066*u.deg, lon=-79.39849*u.deg, height=(113+48)*u.m)
utcoffset = -4*u.hr

suntimesarr = np.zeros((365,2),dtype=object)
for i in range(0,365):
    delta_midnight = np.linspace(4,28,10000,endpoint=False)*u.hr
    times = Time('2022-01-01T00:00:00') + i*u.day + delta_midnight
    frame = AltAz(obstime=times, location=burton_tower)
    sun_altaz = get_sun(times).transform_to(frame)
    sunrise_idx,sunset_idx = np.where(np.diff(np.sign(sun_altaz.alt + 50*u.arcmin)) != 0)[0]
    t1 = (times[sunrise_idx] + np.diff(delta_midnight)[0]/2 + utcoffset)
    t2 = (times[sunset_idx] + np.diff(delta_midnight)[0]/2 + utcoffset)
    suntimesarr[i] = t1.isot, t2.isot
    print(i,suntimesarr[i])


np.savetxt("suntimes.csv", suntimesarr.astype(str), delimiter=",", fmt='%s')
