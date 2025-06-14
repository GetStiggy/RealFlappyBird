import pygame as pg
import sys
from bird import *
from pipes import *
from game_objects import *
from settings import *




class RealFlappyBird:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.load_assets()
        self.score = Score(self)
        self.new_game()

    def load_assets(self):
        # bird
        self.bird_images = pg.image.load('PythonProject/assets/images/bird.png').convert_alpha()
        bird_image = self.bird_images
        bird_size = bird_image.get_width() * BIRD_SCALE, bird_image.get_height() * BIRD_SCALE

        # background
        self.background_image = pg.image.load('PythonProject/assets/images/bg.jpg').convert()
        self.background_image = pg.transform.scale(self.background_image, RES)
        # pipes
        self.top_pipe_image = pg.image.load('PythonProject/assets/images/top_pipe.png').convert_alpha()
        self.top_pipe_image = pg.transform.scale(self.top_pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.bottom_pipe_image = pg.transform.flip(self.top_pipe_image, False, True)

    def new_game(self):
        self.all_sprites_group = pg.sprite.Group()
        self.pipe_group = pg.sprite.Group()
        self.bird = Bird(self)
        self.background = Background(self)
        self.pipe_handler = PipeHandler(self)

    def draw(self):
        self.background.draw()
        self.all_sprites_group.draw(self.screen)
        self.score.draw()
        pg.display.flip()

    def update(self):
        self.background.update()
        self.all_sprites_group.update()
        self.pipe_handler.update()
        self.clock.tick(FPS)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.bird.check_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = RealFlappyBird()
    game.run()




