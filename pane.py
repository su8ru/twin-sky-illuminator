from lib import *;

BASE_H = 450;

class Pane:
    def __init__(self, x, y, postal):
        self.x = x;
        self.y = y;
        self.postal = postal;
        self.latitude, self.longitude, self.city = getLatitudeAndLongitude(postal);
        self.w = 450;
        self.h = 540;
        self.bgImg = loadImage('bg_natural_sougen.jpg');
        self.frontImg = loadImage('bg_natural_sougen_front.png');
        self.bgSeaImg = loadImage('bg_natural_umi.jpg');
        self.frontSeaImg = loadImage('bg_natural_umi_front.png');
        self.sunImg = loadImage('sun.png');
        
    def update(self):
        return None;
    
    def setPostal(self, postal):
        self.postal = postal;
        self.latitude, self.longitude, self.city = getLatitudeAndLongitude(postal);

    def draw(self, time, doy):
        sinh = calcSunAltitude(time, doy, self.latitude, self.longitude);
        noStroke();
        left = self.x;
        right = self.x + self.w;
        # sky
        fill('#d6e9ff');
        rect(left, self.y, right, self.y + self.h);
        image(self.bgSeaImg if self.latitude <= 30 else self.bgImg, left, self.y + 30);
        # draw sun
        fill('#fabc00');
        image(self.sunImg, self.x + self.w / 2 - 50, BASE_H - 800 * sinh - 50, 100, 100);
        # ground
        image(self.frontSeaImg if self.latitude <= 30 else self.frontImg, left, self.y + 30);
        # rect(left, self.y + BASE_H, right, self.y + self.h);
        line(left, BASE_H, right, BASE_H);
        # asayake / yu-yake
        fill(255, 127, 0, max((1 - sinh ** 2) * 511 - 448, 0));
        rect(left, self.y, right, self.y + self.h);
        # night dark
        if (sinh < 0):
            fill(0, 0, 0, min(-sinh * 511, 200));
            rect(left, self.y, right, self.y + self.h);
        # draw status bar
        fill('#000000');
        rect(left, self.y - 30, right, self.y + 30);
        # draw postal
        textAlign(CENTER);
        textSize(20);
        fill('#ffffff');
        text('{}-{} / N{:.3f} E{:.3f}'.format(self.postal[0:3], self.postal[3:8], self.latitude, self.longitude), self.x + self.w / 2, self.y + 20);
        text(u'{}'.format(self.city), self.x + self.w / 2, self.y - 7);
