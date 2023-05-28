#TODO: 
# 1. Меню 
# 2. Выбор сложности в меню
# 3. Подсчет очков в игре
# 4. Переход между игрой и меню (возможно меню загрузки или обратный отсчет)




import os 
from pynput import keyboard
import time
import os 
import random as rnd

LENTH = 150 
WIDTH = 30
SPACE = " "
BRICKS_TEXTURES_PATH = 'bricks/'
DEFAULT_DISTANCE = 40
MAX_JUMP = 15
    
def on_press(key, game):
    if key == keyboard.Key.up:
        game.jump()
        

def controle(game):
    listener = keyboard.Listener(
    on_press=lambda x: on_press(x, game))
    listener.start()
    return listener


class game_object:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path

    def get_x(self): # return x coordinate
        return self.x
    
    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y
        
    def set_y(self, new_y):
        self.y = new_y

    def get_path(self):
        return self.path
    
    def set_path(self,new_path):
        self.path = new_path

    def show(self):
        print('x =', self.x)
        print('y =', self.y)
        print('path =', self.path)

    def __square(self, s_lst):
        max_l = max([len(s) for s in s_lst])
        for i in range(len(s_lst)):
            if len(s_lst[i]) < max_l:
                s_lst[i] = s_lst[i][:-1] + " "
                while len(s_lst[i]) < max_l-1:
                    s_lst[i] += ' '
                s_lst[i] += '\n'
        return s_lst

    def get_view(self):
        file = open(self.path, 'r')
        s_lst = file.readlines()
        squared = self.__square(s_lst)
        return squared

    def get_points(self):
        points = []
        view = self.get_view()
        for i in range(len(view)):
            for j in range(len(view[0])-1):
                if view[i][j] != SPACE:
                    points.append(
                        (self.get_x() + j,
                        self.get_y() + (len(view)-i))
                        )
        return points


class Game:
    def __init__(self, player, lst_bricks):
        self.__player = player
        self.__lst_bricks = lst_bricks
        self.__is_jumping = False
        self.__going_up = False 
        self._fps = 0
        self.__gameover = False

    def get_player(self):
        return self.__player

    def is_gameover(self):
        return self.__gameover

    def get_bricks(self):
        return self.__lst_bricks


    def get_fps(self):
        return self._fps

    def jump(self):
        if not(self.__is_jumping):
            self.__is_jumping = True
            self.__going_up = True

    def __in_jump(self, to):
        if self.__is_jumping:
            if self.__going_up:
                if self.__player.get_y() < to:
                    self.__player.set_y(self.__player.get_y() + 1)
                else:
                    self.__going_up = False
            else:
                if self.__player.get_y() > 0:
                    self.__player.set_y(self.__player.get_y() - 1)
                else:
                    self.__is_jumping = False

    def is_intersection(self, points_a, points_b):
        for a in points_a:
            for b in points_b:
                if a[0] == b[0] and a[1] == b[1]:
                    return True

    def check_hit(self):
        print(set(self.get_bricks()[0].get_points()).intersection(set(self.get_player().get_points())))
        for brick in self.__lst_bricks:
            if self.is_intersection(self.get_player().get_points(), brick.get_points()):
                self.__gameover = True

    


    def __make_a_brick(self):
        textures = os.listdir(BRICKS_TEXTURES_PATH)
        idx = rnd.randint(0, len(textures)-1)
        return game_object(LENTH, 0, BRICKS_TEXTURES_PATH + textures[idx])

    def __check_bricks(self, default_distance):
        if self.__lst_bricks[0].get_x() + len(self.__lst_bricks[0].get_view()[0]) < 0:
            self.__lst_bricks.pop(0)
        
        if LENTH - self.__lst_bricks[-1].get_x()  > default_distance:
            self.__lst_bricks.append(self.__make_a_brick())

    def __move_bricks(self):
        for item in self.__lst_bricks:
            item.set_x(item.get_x()-1)
            

    
    def step(self):
        if self.__is_jumping:
            self.__in_jump(MAX_JUMP)

        self.__check_bricks(DEFAULT_DISTANCE)
        self.__move_bricks()
        self.check_hit()
        # вставить код с проверкой удара об препятствие 
        #
        self._fps += 1

        # осталась только проверка на соударение


class Engine:
    def __init__(self, l, w, game):
        self.__l = l
        self.__w = w
        self.__game = game
        

    def get_scene(self):
        scene = []
        for i in range(self.__w):
            tmp = ''
            for j in range(self.__l):
                tmp += SPACE
            scene.append(tmp + '\n')
        return scene

    def check_boundaries(self, y_len, x_len, curr_y, curr_x):
        if curr_x >= 0 and curr_x < x_len:
            if curr_y >= 0 and curr_y < y_len:
                return True
        return False

    def draw_item(self, item, scene):
        view = item.get_view()
        view_l = len(view[0])
        view_w = len(view)

        x_start = item.get_x()
        y_start = len(scene) - 1 - item.get_y()
        for i in  range(view_w-1, -1, -1):
            for j in range(view_l-1):
                args = [len(scene), len(scene[0]), y_start - (view_w-1 - i), x_start +j]
                if self.check_boundaries(*args):
                    scene[y_start - (view_w-1 - i)]  = scene[y_start - (view_w-1 - i)][:x_start +j] + view[i][j] + scene[y_start - (view_w-1 - i)][x_start +j+1:]
        
        return scene

    def frame(self):
        
        scene = self.get_scene()

        scene = self.draw_item(self.__game.get_player(), scene)
        
        for brick in self.__game.get_bricks():
            scene = self.draw_item(brick, scene)

        return scene


#adress
#по мере ухода из кадра препятсвий - удалять их
def main():
    player = game_object(0,0,'player.txt')
    brick = game_object(LENTH-3, 0, 'bricks/brick.txt')
    
    game = Game(player, [brick])
    engine = Engine(LENTH, WIDTH, game)
    thrd = controle(game)
    while not(game.is_gameover()):
        os.system('clear')
        game.step()
        print("".join(engine.frame()))
        time.seep(0.05)
    thrd.stop()
    
        
main()

