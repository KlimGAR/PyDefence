import sqlite3
from time import time

import pygame
from pygame import Vector2
import pygame_gui

# Инициализация окна и подключение базы данных
Base_Data = sqlite3.connect('PyDefenceBaseData.sqlite')
cur = Base_Data.cursor()
total = Base_Data.execute("""SELECT total FROM Total""").fetchone()[0]
print(total)
pygame.init()
pygame.display.set_caption("PyDefense")

# Размер окна устройства
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h
window_size = (screen_width, screen_height)

# Установка размеров
window_surface = pygame.display.set_mode(window_size)
ui_manager = pygame_gui.UIManager(window_size)

# информ текстa
PyDefence = pygame_gui.elements.UIImage(
    relative_rect=pygame.Rect((screen_width // 2 - 175, screen_height // 2 - 270),
                              (350, 60)),
    image_surface=pygame.image.load('C:/TESTpy/PyDefence/pics/PYDEFENSE.png'),
    manager=ui_manager
)

Score = pygame_gui.elements.UITextBox(
    html_text=f'  TOTAL:\n{total}',
    relative_rect=pygame.Rect((screen_width // 2 - 50, screen_height // 2 + 100), (100, 100)),
    manager=ui_manager
)


# уровнi(1-3)
class FirstLVL:
    def __init__(self):
        bg_first_lvl = pygame.image.load('C:/TESTpy/PyDefence/pics/loc/Enviroment.png')
        x, y = bg_first_lvl.get_size()
        self.kof_x, self.kof_y = x / window_size[0], y / window_size[1]
        self.bg_first_lvl = pygame.transform.scale(bg_first_lvl, (x / self.kof_x, y / self.kof_y))
        window_surface.blit(self.bg_first_lvl, (0, 0))
        pygame.display.flip()
        inf = cur.execute('''SELECT * FROM FirstLVL''').fetchone()
        self.blue, self.green = inf[0], inf[1]
        pygame.display.update()

    def get_surface(self):
        return self.bg_first_lvl

    def update_bg(self):
        window_surface.blit(self.bg_first_lvl, (0, 0))

    def get_kof(self):
        return (self.kof_x, self.kof_y)

    def first_way(self):
        amount_g = 15
        self.green -= amount_g
        return {'A': (amount_g - 5, 0, 0, 0), 'B': (amount_g - 10, 0, 0, 0)}

    def second_way(self):
        amount_g = 5
        self.green -= amount_g
        amount_b = 2
        self.blue -= amount_b
        return {'C': (amount_g, amount_b, 0, 0), 'A': (amount_g, amount_b, 0, 0), 'B': (amount_g, amount_b, 0, 0)}

    def third_way(self):
        amount_g = 30
        self.green -= amount_g
        amount_b = 28
        self.blue -= amount_b
        return {'C': (amount_g, amount_b, 0, 0), 'A': (amount_g, amount_b, 0, 0), 'B': (amount_g, amount_b, 0, 0)}


class SecondLVL:
    def __init__(self):
        bg_second_lvl = pygame.image.load('C:/TESTpy/PyDefence/pics/loc/Map-summer.png')
        x, y = bg_second_lvl.get_size()
        self.kof_x, self.kof_y = x / window_size[0], y / window_size[1]
        self.bg_second_lvl = pygame.transform.scale(bg_second_lvl, (x / self.kof_x, y / self.kof_y))
        window_surface.blit(self.bg_second_lvl, (0, 0))
        pygame.display.flip()
        inf = cur.execute('''SELECT * FROM SecondLVL''').fetchone()
        self.blue, self.green, self.red = inf[0], inf[1], inf[2]
        pygame.display.update()

    def get_surface(self):
        return self.bg_second_lvl

    def update_bg(self):
        window_surface.blit(self.bg_second_lvl, (0, 0))

    def get_kof(self):
        return (self.kof_x, self.kof_y)

    def first_way(self):
        amount_g = 15
        self.green -= amount_g
        return {'A': (amount_g, 0, 0, 0)}

    def second_way(self):
        amount_g = 25
        self.green -= amount_g
        amount_b = 15
        self.blue -= amount_b
        return {'C': (amount_g - 10, amount_b - 10, 0, 0), 'A': (amount_g - 20, amount_b - 10, 0, 0),
                'B': (amount_g - 20, amount_b - 10, 0, 0)}

    def third_way(self):
        amount_b = 28
        self.blue -= amount_b
        amount_r = 10
        self.red -= amount_r
        return {'C': (0, amount_b - 10, amount_r - 7, 0), 'A': (0, amount_b - 20, amount_r - 5, 0),
                'B': (0, amount_b - 10, amount_r - 8, 0)}


class ThirstLVL:
    def __init__(self):
        bg_third_lvl = pygame.image.load('C:/TESTpy/PyDefence/pics/loc/Map-hell.png')
        x, y = bg_third_lvl.get_size()
        self.kof_x, self.kof_y = x / window_size[0], y / window_size[1]
        self.bg_third_lvl = pygame.transform.scale(bg_third_lvl, (x / self.kof_x, y / self.kof_y))
        window_surface.blit(self.bg_third_lvl, (0, 0))
        pygame.display.flip()
        inf = cur.execute('''SELECT * FROM ThirstLVL''').fetchone()
        self.blue, self.green, self.red, self.purple = inf[0], inf[1], inf[2], inf[3]
        pygame.display.update()

    def get_surface(self):
        return self.bg_third_lvl

    def update_bg(self):
        window_surface.blit(self.bg_third_lvl, (0, 0))

    def get_kof(self):
        return (self.kof_x, self.kof_y)

    def first_way(self):
        amount_g = 15
        self.green -= amount_g
        return {'C': (amount_g, 0, 0, 0)}

    def second_way(self):
        amount_r = 5
        self.red -= amount_r
        amount_b = 20
        self.blue -= amount_b
        return {'C': (0, amount_b - 15, amount_r - 2, 0), 'A': (0, amount_b - 10, 0, 0),
                'B': (0, amount_b - 15, amount_r - 3, 0)}

    def third_way(self):
        amount_b = 20
        self.blue -= amount_b
        amount_r = 15
        self.red -= amount_r
        amount_p = 2
        self.purple -= amount_p
        return {'C': (0, amount_b - 15, amount_r - 12, amount_p - 1),
                'A': (0, amount_b - 10, amount_r - 13, amount_p - 1), 'B': (0, amount_b - 15, amount_r - 5, 0)}


class arch:
    def __init__(self, pos):
        self.pos = (pos[0] - 60, pos[1] - 120)
        # self.area = x
        self.ammo = pygame.transform.scale(pygame.image.load('C:/TESTpy/PyDefence/pics/effects/Arrow.png'), (30, 10))
        self.image = pygame.image.load('C:/TESTpy/PyDefence/pics/arch.png')
        x, y = self.image.get_size()
        kof_x, kof_y = x / window_size[0], y / window_size[1]
        self.image = pygame.transform.scale(self.image, (x / kof_x - 1770, y / kof_y - 900))
        window_surface.blit(self.image, self.pos)
        pygame.display.flip()
        self.damage = 10

    def get_dam(self):
        return self.damage

    def draw(self):
        window_surface.blit(self.image, self.pos)


class magic:
    def __init__(self, pos):
        self.pos = (pos[0] - 60, pos[1] - 140)
        # self.area = x
        self.ammo = pygame.transform.scale(pygame.image.load('C:/TESTpy/PyDefence/pics/effects/Magic.png'), (30, 10))
        self.image = pygame.image.load('C:/TESTpy/PyDefence/pics/magic.png')
        x, y = self.image.get_size()
        kof_x, kof_y = x / window_size[0], y / window_size[1]
        self.image = pygame.transform.scale(self.image, (x / kof_x - 1760, y / kof_y - 875))
        window_surface.blit(self.image, self.pos)
        pygame.display.flip()
        self.damage = 25

    def get_dam(self):
        return self.damage

    def draw(self):
        window_surface.blit(self.image, self.pos)


class martira:
    def __init__(self, pos):
        self.pos = (pos[0] - 65, pos[1] - 95)
        # self.area = x
        self.ammo = pygame.transform.scale(pygame.image.load('C:/TESTpy/PyDefence/pics/effects/Shell.png'), (30, 10))
        self.explosion = pygame.transform.scale(pygame.image.load('C:/TESTpy/PyDefence/pics/effects/Explotion.png'),
                                                (160, 170))
        self.image = pygame.image.load('C:/TESTpy/PyDefence/pics/martira.png')
        x, y = self.image.get_size()
        kof_x, kof_y = x / window_size[0], y / window_size[1]
        self.image = pygame.transform.scale(self.image, (x / kof_x - 1770, y / kof_y - 930))
        window_surface.blit(self.image, self.pos)
        pygame.display.flip()
        self.damage = 10

    def get_dam(self):
        return self.damage

    def draw(self):
        window_surface.blit(self.image, self.pos)


def panel():
    bg = pygame.Color(180, 180, 180, 90)

    rect = pygame.draw.rect(window_surface, bg, (0, 0, window_size[0], window_size[1]))
    rect = pygame.draw.rect(window_surface, (60, 60, 60), (screen_width // 2 - 105, screen_height // 2 - 65, 210, 130))

    button_resume = pygame.image.load('C:/TESTpy/PyDefence/pics/Resume.png')
    button_exit_menu = pygame.image.load('C:/TESTpy/PyDefence/pics/Exit.png')
    div = pygame.image.load('C:/TESTpy/PyDefence/pics/Pause.png')

    div = pygame.transform.scale(div, (350, 160))
    button_resume = pygame.transform.scale(button_resume, (200, 50))
    button_exit_menu = pygame.transform.scale(button_exit_menu, (200, 50))

    window_surface.blit(div, (screen_width // 2 - 175, screen_height // 2 - 400))
    window_surface.blit(button_resume, (screen_width // 2 - 100, screen_height // 2 - 60))
    window_surface.blit(button_exit_menu, (screen_width // 2 - 100, screen_height // 2 + 10))

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if min(x, screen_width // 2 - 100) != x and max(x, screen_width // 2 + 100) != x:
                    if min(y, screen_height // 2 - 60) != y and max(y, screen_height // 2 - 10) != y:
                        button_resume = pygame.image.load('C:/TESTpy/PyDefence/pics/Pressed button/Resume.png')
                        button_resume = pygame.transform.scale(button_resume, (200, 50))
                        window_surface.blit(button_resume, (screen_width // 2 - 100, screen_height // 2 - 60))
                        pygame.display.flip()
                        pygame.time.wait(100)
                        return True
                    elif min(y, screen_height // 2 + 10) != y and max(y, screen_height // 2 + 60) != y:
                        button_exit_menu = pygame.image.load('C:/TESTpy/PyDefence/pics/Pressed button/Exit.png')
                        button_exit_menu = pygame.transform.scale(button_exit_menu, (200, 50))
                        window_surface.blit(button_exit_menu, (screen_width // 2 - 100, screen_height // 2 + 10))
                        pygame.display.flip()
                        pygame.time.wait(100)
                        return False


def start_window():
    # Фон меню
    background_image = pygame.image.load("""C:/TESTpy/PyDefence/pics/bg.jpg""")  # Загружаем изображение фона
    x, y = background_image.get_size()
    kof_x, kof_y = x / window_size[0], y / window_size[1]
    background_image = pygame.transform.scale(background_image,
                                              (x / kof_x, y / kof_y))  # Масштабируем изображение до размера окна
    window_surface.blit(background_image, (0, 0))

    # Кнопки
    button_play = pygame.image.load('C:/TESTpy/PyDefence/pics/Play.png')
    button_exit = pygame.image.load('C:/TESTpy/PyDefence/pics/Exit.png')
    button_play = pygame.transform.scale(button_play, (200, 50))
    button_exit = pygame.transform.scale(button_exit, (200, 50))
    window_surface.blit(button_play, (screen_width // 2 - 100, screen_height // 2 - 60))
    window_surface.blit(button_exit, (screen_width // 2 - 100, screen_height // 2 + 10))

    # выбор уровня(кнопки)
    pygame.draw.circle(window_surface, 'white', (screen_width // 2 - 100, screen_height // 2 + 80), 5)
    pygame.draw.circle(window_surface, 'white', (screen_width // 2, screen_height // 2 + 80), 5)
    pygame.draw.circle(window_surface, 'white', (screen_width // 2 + 100, screen_height // 2 + 80), 5)
    levels = pygame.font.Font(None, 30)
    Lvl_text_first = levels.render('Lvl 1', True, (212, 175, 55))
    Lvl_text_second = levels.render('Lvl 2', True, (212, 175, 55))
    Lvl_text_thirst = levels.render('Lvl 3', True, (212, 175, 55))
    window_surface.blit(Lvl_text_first, (screen_width // 2 - 85, screen_height // 2 + 80))
    window_surface.blit(Lvl_text_second, (screen_width // 2 + 15, screen_height // 2 + 80))
    window_surface.blit(Lvl_text_thirst, (screen_width // 2 + 115, screen_height // 2 + 80))

    # tools
    levels = {'Lvl 1': FirstLVL,
              'Lvl 2': SecondLVL,
              'Lvl 3': ThirstLVL}
    is_running = True
    selected_level = None

    while is_running:
        time_delta = pygame.time.Clock().tick(60) / 1000.0

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # НАЖАТИЕ ОСНОВНЫХ КНОПОК
                x, y = pygame.mouse.get_pos()
                if min(x, screen_width // 2 - 100) != x and max(x, screen_width // 2 + 100) != x:
                    if min(y, screen_height // 2 - 60) != y and max(y, screen_height // 2 - 10) != y:
                        BPpress = pygame.image.load('C:/TESTpy/PyDefence/pics/Pressed button/Play.png')
                        BPpress = pygame.transform.scale(BPpress, (200, 50))
                        window_surface.blit(BPpress, (screen_width // 2 - 100, screen_height // 2 - 60))
                        pygame.display.flip()
                        pygame.time.wait(100)
                        if selected_level is not None:
                            start = levels[selected_level]()
                            start_game(start)
                    elif min(y, screen_height // 2 + 10) != y and max(y, screen_height // 2 + 60) != y:
                        BEpress = pygame.image.load('C:/TESTpy/PyDefence/pics/Pressed button/Exit.png')
                        BEpress = pygame.transform.scale(BEpress, (200, 50))
                        window_surface.blit(BEpress, (screen_width // 2 - 100, screen_height // 2 + 10))
                        pygame.time.wait(100)
                        is_running = False
                else:
                    button_play = pygame.image.load('C:/TESTpy/PyDefence/pics/Play.png')
                    button_exit = pygame.image.load('C:/TESTpy/PyDefence/pics/Exit.png')
                    button_play = pygame.transform.scale(button_play, (200, 50))
                    button_exit = pygame.transform.scale(button_exit, (200, 50))
                    window_surface.blit(button_play, (screen_width // 2 - 100, screen_height // 2 - 60))
                    window_surface.blit(button_exit, (screen_width // 2 - 100, screen_height // 2 + 10))

                if min(y, screen_height // 2 + 75) != y and max(y, screen_height // 2 + 85) != y:  # ВЫБОР УРОВНЯ
                    if min(x, screen_width // 2 - 105) != x and max(x, screen_width // 2 - 95) != x:  # lvl 1
                        pygame.draw.circle(window_surface, (255, 133, 133),
                                           (screen_width // 2 - 100, screen_height // 2 + 80), 3)
                        selected_level = 'Lvl 1'
                        pygame.draw.circle(window_surface, 'white', (screen_width // 2, screen_height // 2 + 80), 5)
                        pygame.draw.circle(window_surface, 'white', (screen_width // 2 + 100, screen_height // 2 + 80),
                                           5)

                    if min(x, screen_width // 2 - 5) != x and max(x, screen_width // 2 + 5) != x:  # lvl 2
                        pygame.draw.circle(window_surface, 'white', (screen_width // 2 - 100, screen_height // 2 + 80),
                                           5)
                        pygame.draw.circle(window_surface, (255, 133, 133),
                                           (screen_width // 2, screen_height // 2 + 80), 3)
                        selected_level = 'Lvl 2'
                        pygame.draw.circle(window_surface, 'white', (screen_width // 2 + 100, screen_height // 2 + 80),
                                           5)
                    if max(x, screen_width // 2 + 105) != x and min(x, screen_width // 2 + 95) != x:  # lvl 3
                        pygame.draw.circle(window_surface, 'white', (screen_width // 2 - 100, screen_height // 2 + 80),
                                           5)
                        pygame.draw.circle(window_surface, 'white', (screen_width // 2, screen_height // 2 + 80), 5)
                        pygame.draw.circle(window_surface, (255, 133, 133),
                                           (screen_width // 2 + 100, screen_height // 2 + 80), 3)
                        selected_level = 'Lvl 3'
            ui_manager.process_events(event)

        ui_manager.update(time_delta)
        window_surface.blit(PyDefence.image, PyDefence.rect)  # Отображение изображения на экране

        ui_manager.draw_ui(window_surface)
        pygame.display.update()
    exit()


class Hummer:
    def __init__(self, pos):
        self.pos = (pos[0] - 30, pos[1] - 30)
        self.way_image = 'C:/TESTpy/PyDefence/pics/hummer.png'
        hum = pygame.transform.scale(pygame.image.load(self.way_image), (60, 60))
        window_surface.blit(hum, self.pos)
        self.pressed = False

    def action(self):
        self.pressed = not self.pressed
        self.way_image = ['C:/TESTpy/PyDefence/pics/hummer.png', 'C:/TESTpy/PyDefence/pics/hummer_pressed.png'][
            self.pressed]

    def is_pressed(self):
        return self.pressed

    def get_pos(self):
        return self.pos

    def draw(self):
        hum = pygame.transform.scale(pygame.image.load(self.way_image), (60, 60))
        window_surface.blit(hum, self.pos)


class Skull:
    def __init__(self, image, pos):
        self.pos = (pos[0] - 20, pos[1] - 30)
        kx, ky = screen_width / 2540, screen_height / 1600
        self.size = (150 * kx, 150 * ky)
        skull_image = pygame.transform.scale(image, self.size)
        window_surface.blit(skull_image, self.pos)

    def draw(self, img):
        skull_image = pygame.transform.scale(img, self.size)
        window_surface.blit(skull_image, (self.pos, self.size))

    def get_rect(self):
        return self.pos[0], self.pos[1], self.size[0], self.size[1]


# class Coin(sprite.):
#    def __init__(self):


class Green:
    def __init__(self, pos, way):
        self.im_npc_gree = (
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Green/Green slime 4.png'),
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Green/Green slime 3.png'),
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Green/Green slime 1.png')
        )
        self.kx, self.ky = screen_width / 2540, screen_height / 1600
        size = (70 * self.kx, 50 * self.ky)
        self.im_npc_green = [pygame.transform.scale(i, size) for i in self.im_npc_gree]
        self.cost = 1
        self.way = way
        self.direction = 0
        self.speed = 10
        self.hp = 20
        self.center = [pos[0], pos[1]]
        self.pos = [pos[0] - size[0] // 2, pos[1] - size[1] // 2]
        window_surface.blit(self.im_npc_green[self.direction], self.pos)
        pygame.draw.line(window_surface, 'red', (self.pos[0], self.pos[1]), (self.hp + self.pos[0], self.pos[1]))
        cor = self.way[0]
        for i in self.way[1:]:
            pygame.draw.line(window_surface, 'red', cor, i, 5)
            cor = i
        print(f'путь {self.way}')
        pygame.time.wait(10)

    def get_way(self):
        return self.way

    def move(self, dt: float | int):
        if self.way: # Должен бфть урон ТУТ
            cor = self.way[0]
            for i in self.way[1:]:
                pygame.draw.circle(window_surface, 'black', (cor[0], cor[1]), 5)
                pygame.draw.line(window_surface, 'red', cor, i, 5)
                cor = i
            print(f'путь {self.way}')
            pygame.time.wait(10)
            if min(self.way[0][0] + 2, self.center[0]) != max(self.way[0][0] - 2, self.center[0]) and min(self.way[0][1] + 2, self.center[1]) != max(self.way[0][1] - 2, self.center[1]):
                if min(self.way[0][0] + 2, self.center[0]) != max(self.way[0][0] - 2, self.center[0]):

                #    a = 1 if self.center[1] < self.way[0][1] else -1
                #    self.pos[1] += dt * self.speed * a
                #    self.center[1] += dt * self.speed * a
                if min(self.way[0][1] + 2, self.center[1]) != max(self.way[0][1] - 2, self.center[1]):
                    
                #    a = 1 if self.center[0] < self.way[0][0] else -1
                #    self.pos[0] += dt * self.speed * a
                #    self.center[0] += dt * self.speed * a
                window_surface.blit(self.im_npc_green[self.direction], self.pos)
                pygame.draw.line(window_surface, 'red', (self.pos[0], self.pos[1]),
                                 (self.hp + self.pos[0], self.pos[1]))
                return
            print(f'удалил {self.way[0]}')
            self.way = self.way[1:]
            self.move(dt)



class Blue:
    def __init__(self, pos, way):
        self.im_npc_blu = (
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Blue/Blue slime 4.png'),
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Blue/Blue slime 3.png'),
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Blue/Blue slime 1.png')
        )
        kx, ky = screen_width / 2540, screen_height / 1600
        size = (130 * kx, 100 * ky)
        self.im_npc_blue = [pygame.transform.scale(i, size) for i in self.im_npc_blu]
        self.way = way
        self.direction = 0
        self.speed = 6
        self.hp = 40
        self.pos = [pos[0] - size[0] / 2, pos[1] - size[1] / 2]
        window_surface.blit(self.im_npc_blue[self.direction], self.pos)
        pygame.draw.line(window_surface, 'red', (self.pos[0], self.pos[1]), (self.hp + self.pos[0], self.pos[1]))

    def move(self, dt):
        if self.pos != self.way[0]:
            a = 1 if self.pos[1] < self.way[-1][1] else -1
            self.pos[1] += dt * self.speed * a
            a = 1 if self.pos[0] < self.way[-1][0] else -1
            self.pos[0] += dt * self.speed * a
            window_surface.blit(self.im_npc_blue[self.direction], self.pos)
            pygame.draw.line(window_surface, 'red', (self.pos[0], self.pos[1]), (self.hp + self.pos[0], self.pos[1]))
            return
        self.way.remove(self.way[0])
        self.move(dt)


class Red:
    def __init__(self, pos, way):
        self.im_npc_re = (
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Red/Red slime 4.png'),
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Red/Red slime 3.png'),
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Red/Red slime 1.png')
        )
        kx, ky = screen_width / 2540, screen_height / 1600
        size = (130 * kx, 100 * ky)
        self.im_npc_red = [pygame.transform.scale(i, size) for i in self.im_npc_re]
        self.way = way
        self.direction = 0
        self.speed = 5
        self.hp = 60
        self.pos = [pos[0], pos[1]]
        window_surface.blit(self.im_npc_red[self.direction], self.pos)
        pygame.draw.line(window_surface, 'red', (self.pos[0], self.pos[1]), (self.hp + self.pos[0], self.pos[1]))

    def move(self, dt):
        if self.pos != self.way[0]:
            a = 1 if self.pos[1] < self.way[-1][1] else -1
            self.pos[1] += dt * self.speed * a
            a = 1 if self.pos[0] < self.way[-1][0] else -1
            self.pos[0] += dt * self.speed * a
            window_surface.blit(self.im_npc_red[self.direction], self.pos)
            pygame.draw.line(window_surface, 'red', (self.pos[0], self.pos[1]), (self.hp + self.pos[0], self.pos[1]))
            return
        self.way.remove(self.way[0])
        self.move(dt)


class Purple:
    def __init__(self, pos, way):
        self.im_npc_purpl = (
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Purple/Purple slime 4.png'),
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Purple/Purple slime 3.png'),
            pygame.image.load('C:/TESTpy/PyDefence/pics/units/Purple/Purple slime 1.png')
        )
        kx, ky = screen_width / 2540, screen_height / 1600
        size = (130 * kx, 100 * ky)
        self.im_npc_purple = [pygame.transform.scale(i, size) for i in self.im_npc_purpl]
        self.way = way
        self.direction = 0
        self.speed = 2
        self.hp = 100
        self.pos = [pos[0], pos[1]]
        window_surface.blit(self.im_npc_purple[self.direction], self.pos)
        pygame.draw.line(window_surface, 'red', (self.pos[0], self.pos[1]), (self.hp + self.pos[0], self.pos[1]))

    def move(self, dt):
        if self.pos != self.way[0]:
            a = 1 if self.pos[1] < self.way[-1][1] else -1
            self.pos[1] += dt * self.speed * a
            a = 1 if self.pos[0] < self.way[-1][0] else -1
            self.pos[0] += dt * self.speed * a
            window_surface.blit(self.im_npc_purple[self.direction], self.pos)
            pygame.draw.line(window_surface, 'red', (self.pos[0], self.pos[1]), (self.hp + self.pos[0], self.pos[1]))
            return
        self.way.remove(self.way[0])
        self.move(dt)


class first_way:
    def __init__(self, amount):
        self.npc = {
            0: Green,
            1: Blue,
            2: Red,
            3: Purple
        }
        self.inp_units = [i for i in amount]
        kx, ky = screen_width / 2540, screen_height / 1600
        self.start_point_im = (620 * kx, 1090 * ky)
        self.pathway = [self.start_point_im, (kx * 660, ky * 1070), (kx * 861, ky * 645), (kx * 805, ky * 410)]

    def get_start(self):
        return self.start_point_im

    def get_pathway(self):
        return self.pathway

    def get_npc(self):
        return self.inp_units

    def spawn(self):
        for i in range(4):
            if self.inp_units[i]:
                self.inp_units[i] -= 1
                return self.npc[i](self.start_point_im, self.pathway)


class second_way:
    def __init__(self, amount):
        self.npc = {
            0: Green,
            1: Blue,
            2: Red,
            3: Purple
        }
        self.inp_units = [i for i in amount]
        kx, ky = (screen_width / 2540), (screen_height / 1600)
        self.start_point_im = (1740 * kx, 1180 * ky)
        self.pathway = [self.start_point_im, (1560 * kx, 1090 * ky), (1467 * kx, 910 * ky), (1440 * kx, 633 * ky),
                        (1539 * kx, 480 * ky), (1755 * kx, 405 * ky)]

    def get_start(self):
        return self.start_point_im

    def get_pathway(self):
        return self.pathway

    def get_npc(self):
        return self.inp_units

    def spawn(self):
        for i in range(4):
            if self.inp_units[i]:
                self.inp_units[i] -= 1
                return self.npc[i](self.start_point_im, self.pathway)

    def get_pathway(self):
        return self.pathway


class third_way:
    def __init__(self, amount):
        self.npc = {
            0: Green,
            1: Blue,
            2: Red,
            3: Purple
        }
        print(amount)
        self.inp_units = [i for i in amount]
        kx, ky = (screen_width / 2540), (screen_height / 1600)
        self.start_point_im = (2110 * kx, 590 * ky)
        self.pathway = [
            self.start_point_im, (2040 * kx, 783 * ky), (1764 * kx, 900 * ky), (1300 * kx, 910 * ky),
            (576 * kx, 744 * ky),
            (390 * kx, 600 * ky)]

    def get_start(self):
        return self.start_point_im

    def get_npc(self):
        return self.inp_units

    def spawn(self):
        for i in range(4):
            if self.inp_units[i]:
                self.inp_units[i] -= 1
                return self.npc[i](self.start_point_im, self.pathway)

    def get_pathway(self):
        return self.pathway


def start_game(level: FirstLVL | SecondLVL | ThirstLVL):
    game = level
    skull_and_way = {
        'A': first_way,
        'B': second_way,
        'C': third_way}

    # получения информации по начальной волне
    wave = game.first_way()
    skull_image = pygame.image.load('C:/TESTpy/PyDefence/pics/Skull.png')
    skulls = []
    working_paths: list[first_way, second_way, third_way] = []
    next = [game.second_way(), game.third_way()]
    print(wave)

    for i in wave.keys():
        pathway = skull_and_way[i](wave[i])
        working_paths.append(skull_and_way[i](wave[i]))
        skulls.append(Skull(skull_image, pathway.get_start()))

    x, y = game.get_kof()
    zones_ = [(i[0] / x, i[1] / y) for i in [(447, 876), (977, 687), (1128, 446), (1308, 998), (1708, 1006)]]
    hummers = [Hummer(pos) for pos in zones_]
    zones = {hummers[i].get_pos(): zones_[i] for i in range(5)}

    towers = []
    mobs: list[Green, Blue, Red, Purple] = []

    selected_zone = None
    clock = pygame.time.Clock()
    max_fps = 60
    delta_time = 1 / max_fps
    timer = 0
    # Проверка
    #for i in working_paths:
    #    print(f'{i}: {i.get_pathway()}')
    while True:
        clock.tick(max_fps)
        st_t = time()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if panel():
                        continue
                    start_window()

                if (event.mod & pygame.KMOD_CTRL) and (event.key == pygame.K_z):
                    for i in hummers:
                        if i.is_pressed():
                            i.action()
                            i.draw()
                    selected_zone = None

                if event.key == pygame.K_1 and (selected_zone is not None):
                    hummers.remove(hummers[hummers.index(selected_zone)])
                    towers.append(arch(zones[selected_zone.get_pos()]))
                    selected_zone = None

                if event.key == pygame.K_2 and (selected_zone is not None):
                    hummers.remove(hummers[hummers.index(selected_zone)])
                    towers.append(magic(zones[selected_zone.get_pos()]))
                    selected_zone = None

                if event.key == pygame.K_3 and (selected_zone is not None):
                    hummers.remove(hummers[hummers.index(selected_zone)])
                    towers.append(martira(zones[selected_zone.get_pos()]))
                    selected_zone = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_zone is None:
                    x, y = pygame.mouse.get_pos()
                    for hum in hummers:
                        h = hum.get_pos()
                        if (min(y, h[1]) != y and max(y, h[1] + 60) != y) and (
                                min(x, h[0]) != x and max(x, h[0] + 60) != x):
                            if not hummers[hummers.index(hum)].is_pressed():
                                hummers[hummers.index(hum)].action()
                                for i in hummers:
                                    i.draw()
                                selected_zone = hum
                if wave is not True:
                    x, y = pygame.mouse.get_pos()
                    for i in skulls:
                        cor = (i.get_rect())
                        if (min(y, int(cor[1])) != y and max(y, int(cor[1]) + int(cor[3])) != y) and (
                                min(x, int(cor[0])) != x and max(x, int(cor[2]) + int(cor[0])) != x):
                            skulls = []
                            wave = True
        level.update_bg()
        for i in hummers:
            i.draw()
        if wave is True:
            # задержку в 2 секунды НУЖНО
            for i in working_paths:
                if any(i.get_npc()):
                    mobs.append(i.spawn())
        for i in mobs:
            i.move(delta_time)
        for i in towers:
            i.draw()
        for i in skulls:
            i.draw(skull_image)
        pygame.display.flip()
        timer += delta_time
        delta_time = time() - st_t


start_window()
Base_Data.close()
pygame.quit()
