import pygame
from player import Player


class WerewolfWorries:
    def __init__(self):
        pygame.init()

        self.game_width = int(pygame.display.Info().current_w * .55)
        self.game_height = int(pygame.display.Info().current_h * .85)
        self.game_surface = pygame.display.set_mode((self.game_width, self.game_height))
        self.clock = pygame.time.Clock()
        self.background_color = (0, 0, 0)

        pygame.display.set_caption("Werewolf Worries!")

        self.player = Player()

    def quit_game(self):
        pygame.quit()
        quit()

    def game_intro(self):
        game_intro = True

        while game_intro:
            if pygame.event.get(pygame.QUIT):
                self.quit_game()

            self.game_surface.fill(self.background_color)
            self.game_surface.blit(
                self.player.image,
                ((self.game_width/2) - (self.player.width/2),
                 self.game_height - self.player.height))

            pygame.display.update()
            self.clock.tick(30)
            self.game_loop()

    def game_loop(self):
        # process_input, update_game_state, draw_screen
        exit_game = False

        while not exit_game:
            if pygame.event.get(pygame.QUIT):
                self.quit_game()
            self.clock.tick(60)
        self.quit_game()
