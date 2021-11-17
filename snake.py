import pygame


class Snake:
    def __init__(self, screen: object):
        self.__screen = screen
        self.__pos = list()
        self.__change_pos = list()
        self.__current_direction = None
        self.__segments = list()
        self.set_snake()

    @property
    def snake_position(self) -> tuple:
        """
        Returns current snake position in tuple 
        """
        return tuple(self.__pos)

    def set_snake(self):
        """
        Set snake initial-positions, snake initial segments and snake initial direction 
        """
        mid_width = self.__screen.get_width()/2
        mid_height = self.__screen.get_height()/2

        self.__pos = [mid_width, mid_height]
        self.__segments = [self.__pos.copy(), [mid_width-10, mid_height]]
        self.__change_pos = [10, 0]
        self.__current_direction = pygame.K_RIGHT

    def collide_with_body(self) -> bool:
        """
        Returns true if snake head collide with its body segment
        """
        snake_head = self.__segments[0]
        snake_body = self.__segments[1:]

        for i in snake_body:
            if i == snake_head:
                return True
            else:
                continue

        return False

    def move(self, food_collide: bool):
        """
        Function to move snake 
        """
        self.__pos = [self.__pos[0] + self.__change_pos[0],
                      self.__pos[1] + self.__change_pos[1]]

        self.__segments.insert(0, self.__pos.copy())

        if not food_collide:
            self.__segments.pop()

        for s in self.__segments:
            pygame.draw.rect(self.__screen, "black", [*s, 10, 10])

    def change_direction(self, direction):
        """
        Function to change snake direction
        """
        if direction == pygame.K_UP and self.__current_direction != pygame.K_DOWN:
            self.__current_direction = direction
            self.__change_pos = [0, -10]
        elif direction == pygame.K_DOWN and self.__current_direction != pygame.K_UP:
            self.__current_direction = direction
            self.__change_pos = [0, 10]
        elif direction == pygame.K_RIGHT and self.__current_direction != pygame.K_LEFT:
            self.__current_direction = direction
            self.__change_pos = [10, 0]
        elif direction == pygame.K_LEFT and self.__current_direction != pygame.K_RIGHT:
            self.__current_direction = direction
            self.__change_pos = [-10, 0]
