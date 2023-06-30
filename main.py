from pane import Pane;
from lib import doyToDate;

class Main:
    def __init__(self):
        self.time = 0;
        self.speed = 1;
        self.left = Pane(0, 30, '0010021');
        self.right = Pane(450, 30, '1000001');
        self.doy = 180;

    def update(self, scenes):
        if keyPressed:
            if key == ' ':
                self.time += self.speed * 10;
            if key == BACKSPACE:
                self.time -= self.speed * 10;
        else:
            self.time += self.speed;

        # clamp
        if self.time > 1440:
            self.time = 0;
            self.doy += 1;
        if self.time < 0:
            self.time = 1440;
            self.doy -= 1;
        if self.doy > 365:
            self.doy = 1;
        if self.doy < 1:
            self.doy = 365;
        
        # scene
        if keyPressed:
            if key == 'd':
                return 'date';
            if key == 'p':
                return 'postal';

    def setDoy(self, doy):
        self.doy = doy;
        self.time = 0;
    
    def setTime(self, time):
        self.time = time;
    
    def setRPostal(self, postal):
        self.right.setPostal(postal);

    def draw(self):
        background('#ffffff');
        
        self.left.draw(self.time, self.doy);
        self.right.draw(self.time, self.doy);

        # draw pane border
        stroke('#000000');
        strokeWeight(2);
        line(450, 0, 450, 600);
        # draw status bar
        fill('#000000');
        # rect(0, 0, 900, 30);
        rect(0, 570, 900, 600);
        # draw time
        fill('#ffffff');
        textAlign(CENTER);
        textSize(25);
        m, d = doyToDate(self.doy);
        text('{}/{} {:0>2}:{:0>2}'.format(m, d, self.time // 60, self.time % 60), 450, 38);
        textSize(20);
        text('[space]: fast-forward  [backspace]: fast-return  [d]: choose date  [p]: choose place', 450, 593);
