from lib import dateToDoy;

class Date:
    def __init__(self):
        self.d = { 'm1': None, 'm2': None, 'd1': None, 'd2': None };
        self.next = 'm1';
        self.beforePressed = False;
        self.status = 'INPUT';
        self.dn = None;
    
    def update(self, scenes):
        if keyPressed:
            if self.status == 'INPUT' and key == BACKSPACE and not self.beforePressed:
                self.__init__();
                return 'main';
            if self.status == 'INPUT' and '0' <= key <= '9' and not self.beforePressed:
                self.d[self.next] = key;
                if nextDict[self.next] is not None:
                    self.next = nextDict[self.next];
                else:
                    if self.validate():
                        self.status = 'CONFIRM';
                        self.dn = dateToDoy(self.getMonth(), self.getDay());
                    else:
                        self.status = 'ERROR';
            if self.status == 'CONFIRM':
                if key == 'y':
                    scenes['main'].setDoy(self.dn);
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
    
    def getMonth(self):
        return int(self.d['m1'] + self.d['m2']);
    
    def getDay(self):
        return int(self.d['d1'] + self.d['d2']);
    
    def validate(self):
        return 1 <= self.getMonth() <= 12 and 1 <= self.getDay() <= monthlyDays[self.getMonth() - 1];
    
    def draw(self):
        background('#ffffff');
        fill('#000000');
        textAlign(LEFT);
        textSize(50);
        text('Enter the date you will go:', 50, 100);
        
        stroke('#000000');
        strokeWeight(10);
        textAlign(CENTER);
        textSize(200);
        BASELINE = 350;
        line(100, BASELINE, 200, BASELINE) if self.d['m1'] is None else text(self.d['m1'], 150, BASELINE);
        line(250, BASELINE, 350, BASELINE) if self.d['m2'] is None else text(self.d['m2'], 300, BASELINE);
        line(550, BASELINE, 650, BASELINE) if self.d['d1'] is None else text(self.d['d1'], 600, BASELINE);
        line(700, BASELINE, 800, BASELINE) if self.d['d2'] is None else text(self.d['d2'], 750, BASELINE);

        line(480, BASELINE - 150, 420, BASELINE + 20);
        
        textAlign(LEFT);
        textSize(50);
        if self.status == 'CONFIRM':
            text('DOY: {}. Confirm? [y/n]:'.format(self.dn), 50, 500);
        if self.status == 'ERROR':
            text('Date not found. Re-enter? [y/n]:', 50, 500);
            
        textSize(20);
        textAlign(CENTER);
        text('[backspace]: return to main', 450, 593);


nextDict = { 'm1': 'm2', 'm2': 'd1', 'd1': 'd2', 'd2': None };
monthlyDays = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];
