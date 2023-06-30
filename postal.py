from lib import getLatitudeAndLongitude;

class Postal:
    def __init__(self):
        self.d = [ None ] * 7;
        self.next = 0;
        self.beforePressed = False;
        self.status = 'INPUT';
        self.latitude = None;
        self.longitude = None;
    
    def update(self, scenes):
        if keyPressed:
            if self.status == 'INPUT' and key == BACKSPACE and not self.beforePressed:
                if self.next > 0:
                    self.d[self.next - 1] = None;
                    self.next -= 1;
                else:
                    self.__init__();
                    return 'main';
            if self.status == 'INPUT' and '0' <= key <= '9' and not self.beforePressed:
                self.d[self.next] = key;
                if self.next < 6:
                    self.next += 1;
                else:
                    res = getLatitudeAndLongitude(self.getPostal());
                    if res is not None:
                        self.latitude, self.longitude, self.city = res;
                        self.status = 'CONFIRM';
                    else:
                        self.status = 'ERROR';
            if self.status == 'CONFIRM':
                if key == 'y':
                    scenes['main'].setRPostal(self.getPostal());
                    scenes['main'].setTime(0);
                    self.__init__();
                    return 'main';
                if key == 'n':
                    self.__init__();
            if self.status == 'ERROR':
                if key == 'y':
                    self.__init__();
                if key == 'n':
                    self.__init__();
                    return 'main';
            self.beforePressed = True;
        else:
            self.beforePressed = False;
            
    def getPostal(self):
        return "".join(self.d);
    
    def draw(self):
        background('#ffffff');
        fill('#000000');
        textAlign(LEFT);
        textSize(50);
        text('Enter the postal code you will go:', 50, 100);
        
        stroke('#000000');
        strokeWeight(10);
        textAlign(CENTER);
        textSize(160);
        BASELINE = 350;
        for i in range(3):
            line( 50 + 110 * i, BASELINE, 130 + 110 * i, BASELINE) if self.d[i] is None else text(self.d[i],  90 + 110 * i, BASELINE);
        for i in range(3, 7):
            line(110 + 110 * i, BASELINE, 190 + 110 * i, BASELINE) if self.d[i] is None else text(self.d[i], 150 + 110 * i, BASELINE);
        line(380, BASELINE - 50, 410, BASELINE - 50);
        
        textAlign(LEFT);
        textSize(50);
        if self.status == 'CONFIRM':
            text(u'{}\nConfirm? [y/n]:'.format(self.city), 50, 470);
        if self.status == 'ERROR':
            text('City not found. Re-enter? [y/n]:', 50, 500);
            
        textSize(20);
        textAlign(CENTER);
        text('[backspace]: return to main', 450, 593);
