# floating_snake.py
import random
from config import WIDTH, HEIGHT, CELL_SIZE
import pygame

class FloatingSnake:
    def __init__(self):
        self.length = random.randint(5, 10)
        self.segments = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(self.length)]
        self.direction = random.choice([(CELL_SIZE, 0), (-CELL_SIZE, 0), (0, CELL_SIZE), (0, -CELL_SIZE)])
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.timer = 0

    def move(self):
        self.timer += 1
        if self.timer % 10 == 0:
            new_head = (
                (self.segments[0][0] + self.direction[0]) % WIDTH,
                (self.segments[0][1] + self.direction[1]) % HEIGHT
            )
            self.segments.insert(0, new_head)
            self.segments.pop()

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, self.color, (*segment, CELL_SIZE, CELL_SIZE))
