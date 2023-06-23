#TODO: 
# 1. Меню 
# 2. Выбор сложности в меню 
# 3. Подсчет очков в игре - поставить на центр экрана
# 4. Переход между игрой и меню (возможно меню загрузки или обратный отсчет)




import os 
from pynput import keyboard
import time
import os 
import random as rnd
import colorama

LENTH = 150
WIDTH = 30
SPACE = " "
BRICKS_TEXTURES_PATH = 'bricks/'
DEFAULT_DISTANCE = 40
MAX_JUMP = 10
NUMBERS_PATH = 'numbers/'
    
def on_press(key, game):
    if key == keyboard.Key.up:
        game.jump()

def menu_on_press(key, menu):
    if key == keyboard.Key.up:
        menu.up()
    elif key == keyboard.Key.down:
        menu.down()
    elif key == keyboard.Key.space:
        menu.is_chosen = True

def controle(game):
    listener = keyboard.Listener(
    on_press=lambda x: on_press(x, game))
    listener.start()
    return listener

def menu_controle(menu):
    listener = keyboard.Listener(
    on_press=lambda x: menu_on_press(x, menu))
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
        self.__jump_peak = 0

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
                elif self.__player.get_y() == to and self.__jump_peak < 4:
                    self.__jump_peak += 1
                else:
                    self.__going_up = False
            else:
                if self.__player.get_y() > 0:
                    self.__player.set_y(self.__player.get_y() - 1)
                else:
                    self.__is_jumping = False
                    self.__jump_peak = 0

    def is_intersection(self, points_a, points_b):
        for a in points_a:
            for b in points_b:
                if a[0] == b[0] and a[1] == b[1]:
                    return True

    def check_hit(self):
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

    def make_points(self, points):
        digits = []
        while points > 0:
            digits.append(points % 10)
            points = points // 10
        
        views = []
        for i in range(len(digits)-1, -1, -1):
            path = NUMBERS_PATH + str(digits[i]) + '.txt'
            file = open(path, 'r')
            lines = file.readlines()
            views.append(lines)
            file.close()
        

        out = ""
        for i in range(7):
            row = ""
            for j in range(len(views)):
                row += views[j][i][:-1]
            out += row + '\n'

        file = open('numbers/points.txt', 'w')
        file.write(out)
        

    def points_position(self):
        return LENTH // 2 - len(str(self.__game.get_fps())) * 7 // 2, WIDTH - 10


    def frame(self):
        
        scene = self.get_scene()

        scene = self.draw_item(self.__game.get_player(), scene)
        
        for brick in self.__game.get_bricks():
            scene = self.draw_item(brick, scene)
        
        self.make_points(self.__game.get_fps() // 10)
        points = game_object(*self.points_position(), 'numbers/points.txt')
        scene = self.draw_item(points, scene)

        return scene
    


class menu: 
    def __init__(self, l, w):
        self.__l = l
        self.__w = w
        self.curr_id = 0
        self.white = colorama.Fore.WHITE
        self.back = colorama.Back.BLACK
        self.bwhite = colorama.Back.WHITE
        self.black = colorama.Fore.BLACK
        self.is_chosen = False
        colorama.init(autoreset=True)
        self.varid = 0
        self.isChoosed = False
        self.variants = [
            {
                "text":open('start.txt').read(),
                "data": "print(1, 'var')",
            },
            {
                "text":open('exit.txt').read(),
                "data": "print(2, 'var')",
            }
                    ]   
    
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

    def up(self):
        if self.curr_id == 0:
            self.curr_id = 1
        else:
             self.curr_id = 0

    def down(self):
        if self.curr_id == 1:
            self.curr_id = 0
        else:
             self.curr_id = 1


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
    
    def printVariants(self, variants, variant):
        for varId, var in enumerate(variants):
            if varId == variant:
                print(self.back+self.bwhite+self.black+var["text"])
            else:
                print("", self.back+var["text"]) 


    def frame(self):
        start = None
        exit = None
        left_arrow = None
        right_arrow = None
        if self.curr_id == 0:
            start = game_object(15, 15+1, "start.txt")
            exit = game_object(30, 5, "exit.txt")
            left_arrow = game_object(5, 18, "arrow.txt")
            right_arrow = game_object(87, 18, "arrow.txt")
        else:
            start = game_object(15, 15, "start.txt")
            exit = game_object(30, 5+1, "exit.txt")
            left_arrow = game_object(20, 8, "arrow.txt")
            right_arrow = game_object(70, 8, "arrow.txt")
        
    
        scene = self.get_scene()
        scene = self.draw_item(start, scene)
        scene = self.draw_item(exit, scene)
        scene = self.draw_item(left_arrow, scene)
        scene = self.draw_item(right_arrow, scene)
        scene = self.draw_item(game_object(0,0, 'tip.txt'), scene)
        return scene



    
    
    




    



def main():
    

    #while(not_exit):
    #if menu
    #menu loop
    #else
    #game loop

    while True:
        player = game_object(0,0,'player.txt')
        brick = game_object(LENTH-3, 0, 'bricks/cactus.txt')
    
        game = Game(player, [brick])
        engine = Engine(LENTH, WIDTH, game)
        mn = menu(LENTH, WIDTH)
        thrd = menu_controle(mn)

        while not(mn.is_chosen):
            os.system('clear')
            print("".join(mn.frame()))  
            time.sleep(0.1)

        thrd.stop()
        if mn.curr_id == 0:
            engine.make_points(123)
            thrd = controle(game)
            counter = 0
            while not(game.is_gameover()):
              os.system('clear')
              game.step()
              print("".join(engine.frame()))
              time.sleep(0.025)
              counter += 1
            thrd.stop()
            os.system('clear')
            game_over = engine.draw_item(game_object(20, 5, 'game_over.txt'), engine.frame())
            for i in range(5):
                if i % 2 == 0:
                    print(''.join(game_over))
                else: 
                    print(''.join(engine.frame()))
                time.sleep(1)
                os.system('clear')


        else:
            break

    
        
main() 

