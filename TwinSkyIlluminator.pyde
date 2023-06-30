from title import Title;
from main import Main;
from date import Date;
from postal import Postal;

def setup():
    global scene, scenes, bgImage;
    scene = 'title';
    scenes = { 'title': Title(), 'main': Main(), 'date': Date(), 'postal': Postal() };
    background('#ffffff');
    size(900, 600);
    font = createFont('BIZ-UDPGothic', 100);
    textFont(font);

def draw():
    try:
        global scenes, scene;
        s = scenes[scene].update(scenes);
        if s is not None and s in scenes.keys():
            scene = s;
        scenes[scene].draw();
    except Exception as e :
        print(e.message);
    
