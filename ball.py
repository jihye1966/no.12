from pathlib import Path

from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    SPEED = 10

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        image_path = Path(__file__).resolve().parent / 'ball21x21.png'
        self.image = load_image(str(image_path))

    def update(self):
        self.x += self.direction * self.SPEED
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
