import random
from pico2d import *
import gfw

RES_DIR = './res/'

def res(file):
	return RES_DIR + file

def rand(val):
    return val * random.uniform(0.9, 1.1)

def point_add(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return x1+x2, y1+y2

def move_obj(obj):
    obj.pos = point_add(obj.pos, obj.delta)

def collides_box(a, b,tpe):
    (la, ba, ra, ta) = a.get_bb()
    

    if tpe == 0 :
        for i in range(b.mcount) :
            (lb, bb, rb, tb) = b.get_bb(i)
            #print((la, ba, ra, ta),(lb, bb, rb, tb),la > rb,ra < lb,ba > tb,ta < bb)
            if la > rb: continue
            if ra < lb: continue
            if ba > tb: continue
            if ta < bb: continue

            return True

    else :
        (lb, bb, rb, tb) = b.get_bb()
  
    #print((la, ba, ra, ta),(lb, bb, rb, tb))


    if la > rb: return False
    if ra < lb: return False
    if ba > tb: return False
    if ta < bb: return False

    return True

def distance_sq(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return (x1-x2)**2 + (y1-y2)**2

def distance(point1, point2):
	math.sqrt(distance_sq(point1, point2))
	
def draw_collision_box():
   
    for obj in gfw.world.all_objects():
        if hasattr(obj, 'get_bb'):
            if hasattr(obj, 'mcount'):
                for i in range(obj.mcount):
                    draw_rectangle(*obj.get_bb(i))
            else:
                draw_rectangle(*obj.get_bb())

def mouse_xy(event):
    return event.x, get_canvas_height() - event.y - 1

def pt_in_rect(point, rect):
    (x, y) = point
    (l, b, r, t) = rect

    if x < l: return False
    if x > r: return False
    if y < b: return False
    if y > t: return False

    return True

class ImageObject:
    def __init__(self, imageName, pos):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.pos = pos
    def draw(self):
        self.image.draw(*self.pos)
    def update(self):
        pass
    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['image']
        return dict
    def __setstate__(self, dict):
        self.__dict__.update(dict)
        self.image = gfw.image.load(res(self.imageName))

if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")
