import os 
from pynput import keyboard
import time

LENTH = 150 
WIDTH = 30

    
def on_press(key, game):
    try:
        if key == keyboard.Key.up:
            game.jump()
    except AttributeError:
        print("Whoops... something went wrong!")
        

def controle(game):
    listener = keyboard.Listener(
    on_press=lambda x: on_press(x, game))
    listener.start()

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

    def square(self, s_lst):
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
        squared = self.square(s_lst)
        return squared


class Game:
    def __init__(self, player, lst_bricks):
        self.__player = player
        self.__lst_bricks = lst_bricks
        self.__is_jumping = False
        self.__going_up = False 
        self._fps = 0

    def get_player(self):
        return self.__player

    def get_bricks(self):
        return self.__lst_bricks


    def __move_bricks(self):
        pass
        # for brick in self.__lst_bricks:
        #     brick.set_x(brick.get_x - 1)

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

    def check_hit(self):
        pass
        #TODO



    
    def step(self):
        #self.move_bricks()
        if self.__is_jumping:
            self.__in_jump(2)

        #move_bricks()

        self._fps += 1
        

        

        
        #is jump pressed
        #if jump is pressed
        #is there hit

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
                tmp += '_'
            scene.append(tmp + '\n')
        return scene

    def check_boundaries(self, y_len, x_len, curr_y, curr_x):
        if curr_x >= 0 and curr_x < x_len:
            if curr_y >= 0 and curr_y < y_len:
                return True
        return False


    def frame(self):
        scene = self.get_scene()

        view = self.__game.get_player().get_view()
        view_l = len(view[0])
        view_w = len(view)

        x_start = self.__game.get_player().get_x()
        y_start = len(scene) - 1 - self.__game.get_player().get_y()
        for i in  range(view_w-1, 0, -1):
            for j in range(view_l-1):
                args = [len(scene), len(scene[0]), y_start - (view_w-1 - i), x_start +j]
                if self.check_boundaries(*args):
                    scene[y_start - (view_w-1 - i)]  = scene[y_start - (view_w-1 - i)][:x_start +j] + view[i][j] + scene[y_start - (view_w-1 - i)][x_start +j+1:]

        view = self.__game.get_bricks()[0].get_view()
        view_l = len(view[0])
        view_w = len(view)

        for i in  range(view_w-1, 0, -1):
            for j in range(view_l-1):
                args = [len(scene), len(scene[0]), y_start - (view_w-1 - i), x_start +j]
                if self.check_boundaries(*args):
                    scene[y_start - (view_w-1 - i)]  = scene[y_start - (view_w-1 - i)][:x_start +j] + view[i][j] + scene[y_start - (view_w-1 - i)][x_start +j+1:]


        return scene



    
#adress
#по мере ухода из кадра препятсвий - удалять их
def main():
    player = game_object(-5,0,'player.txt')
    brick = game_object(LENTH-2, 0, 'brick.txt')
    game = Game(player, [brick])
    engine = Engine(LENTH, WIDTH, game)
    controle(game)
    while True:
        game.step()
        print("".join(engine.frame()))
        time.sleep(0.1)
        os.system('clear')
        
main()


# 150 x 30
# 150 -> 160 -> 170 -> 




# 10, 20, 150, 20
def generate(n, fps, max_x, start_distance): # -> Исмаил и Адам
    # -> Генерировать объекты класса game_object  - препятсвтвия. Генерует n-штук препятсвий, start_distance - fps//100. 
    # Координата первого препятсвия в списке = max_x. 
    # [game_obj, game_obj1, ... ]



def check_hit(player, lst_bricks): # сделать список из координат и проверять поточечно
    pass
    # -> Амир 