# food.py

import pygame
import random
from config import *

class Food:
    def __init__(self):
        self.position = (
            random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        )
        self.food_image = pygame.image.load("assets/food_image.jpg")
        self.food_image = pygame.transform.scale(self.food_image, (CELL_SIZE, CELL_SIZE))

    def draw(self, surface):
        surface.blit(self.food_image, self.position)
