class Title:
    def __init__(self):
        self.flameCount = 128;
        self.yuuyakeImg = loadImage('yuuyake.png');
    
    def update(self, scenes):
        self.flameCount += 1;
        if keyPressed and (key == ENTER or key == RETURN):
            return 'main';
    
    def draw(self):
        background('#ffffff');
        fill('#f08201');
        image(self.yuuyakeImg, 10, 0, 220, 200);
        textAlign(CENTER);
        textSize(95);
        text("TwinSky Illuminator", width / 2, 300);
        fill(0, abs((self.flameCount % 255) - 128));
        textSize(50);
        text('press enter to continue', width / 2, 500);
