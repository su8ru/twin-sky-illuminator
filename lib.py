import datetime;

def calcSunAltitude(time, dn, latitude, longitude):
    # http://www.es.ris.ac.jp/~nakagawa/met_cal/solar.html
    latitude = latitude / 180 * PI;
    longitude = (longitude - 135) / 180 * PI;
    theta = 2 * PI * (dn - 1) / 365;
    delta = 0.006918 - 0.399912 * cos(theta) + 0.070257 * sin(theta) - 0.006758 * cos(2 * theta) + 0.000907 * sin(2 * theta) - 0.002697 * cos(3 * theta) + 0.001480 * sin(3 * theta);
    eq = 0.000075 + 0.001868 * cos(theta) - 0.032077 * sin(theta) - 0.014615 * cos(2 * theta) - 0.040849 * sin(2 * theta);
    h = (float(time) / 60 - 12) * PI / 12 + longitude + eq;
    return sin(latitude) * sin(delta) + cos(latitude) * cos(delta) * cos(h);

def getLatitudeAndLongitude(postal):
    res = loadStrings('https://twinsky-illuminator.cf.su8.run/?postal={}'.format(postal));
    if res[0] == 'error':
        return None;
    else:
        return map(float, res[0].split(',')) + [res[1]];

def doyToDate(doy):
    date = datetime.date(2023, 1, 1) + datetime.timedelta(doy - 1);
    return date.month, date.day;
    
def dateToDoy(m, d):
    return (datetime.date(2023, m, d) - datetime.date(2023, 1, 1)).days + 1;
