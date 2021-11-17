import pygame
import random


class Food:
    def __init__(self, screen: object):
        self.__screen = screen
        self.food_position = tuple()

    def generate_food_position(self):
        """
        Function to generate random x,y position for food
        """
        screen_width = self.__screen.get_width()
        screen_height = self.__screen.get_height()

        self.food_position = (
            random.randrange(1, (screen_width//10)) * 10,
            random.randrange(1, (screen_height//10)) * 10
        )

    def show_food(self):
        """
        Function to show food on screen
        """
        pygame.draw.rect(self.__screen, "red", [
            *self.food_position, 10, 10])
