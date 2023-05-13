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

    def get_player(self):
        return self.__player


    def __move_bricks(self):
        for brick in self.__lst_bricks:
            brick.set_x(brick.get_x - 1)

    def jump(self):
        if not(self.__is_jumping):
            self.__is_jumping = True
            self.__going_up = True

    def __in_jump(self, to):
        if self.__is_jumping:
            if self.__going_up:
                if self.__player.get_x() < to:
                    self.__player.set_x(self.__player.get_x() + 1)
                else:
                    self.__going_up = False
            else:
                if self.__player.get_x() > 0:
                    self.__player.set_x(self.__player.get_x() - 1)
                else: 
                    self.__is_jumping = False

    def check_hit(self):
        pass
        #TODO

    
    def step(self):
        #self.move_bricks()
        if self.__is_jumping:
            self.__in_jump(2)
        
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

    def frame(self):
        pass
        #takes info from game and returns new frame
        scene = self.get_scene()
        x_start = self.__game.get_player().get_x() 
        y_start = 30 - self.__game.get_player().get_y()
        view = self.__game.get_player().get_view()
        view_l = len(view[0])
        view_w = len(view)
        for i in  range(view_w, 0, -1):
            for j in range(view_l-1):
                print(f"{i} {j}")
                scene[y_start - (view_w-i)]  = scene[y_start - (view_w-i)][:x_start +j] + view[i][j] + scene[y_start - (view_w-i)][x_start +j+1:]
        return scene
        

        
        



def main():
    player = game_object(0,0,'player.txt')
    game = Game(player, [])
    engine = Engine(LENTH, WIDTH, game)
    print(engine.frame())
    #controle(game)
    # while True:
    #     game.step()
    #     game.get_player().show()
    #     time.sleep(1)
        
main()




