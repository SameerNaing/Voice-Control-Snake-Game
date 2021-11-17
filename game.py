import pygame
from pygame.constants import KEYDOWN
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        # pygame display screen
        self.__screen = None
        # pygame fps clock
        self.__clock = None
        # user score
        self.__score = 0
        # setup for the game
        self.__setup()

    def __setup(self):
        """
        Function to make setup for the game
        """
        pygame.init()
        self.__screen = pygame.display.set_mode((600, 500))
        pygame.display.set_caption("Voice Control Snake Game")
        self.__clock = pygame.time.Clock()

    def __show_score(self):
        """
        Function to show score on the screen
        """
        score_font = pygame.font.Font(None, 30)
        score = score_font.render(
            f"Score: {self.__score}", True, "brown")
        score_rect = score.get_rect(topleft=(10, 10))
        self.__screen.blit(score, score_rect)

    def __collision_with_wall(self, snake_position: tuple):
        """
        Returns true if snake hit the wall else false
        """
        screen_width = self.__screen.get_width()
        screen_height = self.__screen.get_height()

        x_hit = snake_position[0] < 0 or snake_position[0] > screen_width-10
        y_hit = snake_position[1] < 0 or snake_position[1] > screen_height-10

        return x_hit or y_hit

    def __show_game_over_screen(self):
        """
        Function to show game over screen
        """
        screen_width_middle = self.__screen.get_width()/2
        screen_height_middle = self.__screen.get_height()/2

        replay_font = pygame.font.Font(None, 50)
        score_font = pygame.font.Font(None, 40)

        replay_text = replay_font.render(
            "You Lost! press 'R' to replay", True, "brown")
        score_text = score_font.render(
            f"Your score is {self.__score}", True, "brown")

        replay_text_rect = replay_text.get_rect(
            midbottom=(screen_width_middle, screen_height_middle))
        score_text_rect = score_text.get_rect(
            midtop=(screen_width_middle, screen_height_middle+70))

        self.__screen.blit(replay_text, replay_text_rect)
        self.__screen.blit(score_text, score_text_rect)

    def start(self):
        snake = Snake(self.__screen)
        food = Food(self.__screen)
        first_loop = True
        exit_game = False
        game_over = False
        game_over_loop = True

        while not exit_game:
            # if snake hit the wall or its body then game over
            if game_over:
                # Set game_over_loop = True, to show game over screen
                game_over_loop = True
                while game_over_loop:
                    # In game over screen listen events
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            # when user click cross button on window then stop the loop and close the pygame window
                            game_over_loop = False
                            exit_game = True
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                            # when user click 'R' and replay, reset everything
                            snake.set_snake()
                            food.generate_food_position()
                            self.__score = 0
                            # game_over_loop = False to remove game over screen
                            game_over_loop = False
                            # start game again
                            game_over = False
                    # only show game over screen and remove snake screen
                    self.__screen.fill("white")
                    self.__show_game_over_screen()
                    pygame.display.update()

            # listen events when user playing game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # when user click cross button on window close pygame window
                    exit_game = True
                elif event.type == pygame.KEYDOWN:
                    # change snake direction according to button press
                    snake.change_direction(event.key)

            self.__screen.fill("white")

            # if snake collide with food or not
            food_collide = snake.snake_position == food.food_position

            # if snake collide with food update score
            if food_collide:
                self.__score += 1

            # if snake collide with food or it is the first loop
            if food_collide or first_loop:
                # generate food new food position
                food.generate_food_position()
                # set first loop equal to false
                first_loop = False

            # show food at generated x and y position on screen
            food.show_food()
            # show current score on screen
            self.__show_score()
            # move the snake
            snake.move(food_collide)

            # if snake collide with wall then game over
            if self.__collision_with_wall(snake_position=snake.snake_position):
                game_over = True

            # if snake collide with its own body then game over
            if snake.collide_with_body():
                game_over = True

            pygame.display.update()
            self.__clock.tick(15)

        pygame.quit()
