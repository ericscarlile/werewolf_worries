import pygame


class VehicleInterface(pygame.sprite.Sprite):
    """
    This class is the abstractation of all other vehicles in the game eg. player and werewolf.
    The following methods need to be implemented by the inheriting class:
    move(), take_damage(), fire_missle()
    """
    def __init__(self, image, health, sheild, speed, missile_damage, fire_rate):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()

        self.health = health
        self.shield = sheild
        self.speed = speed
        self.missile_damage = missile_damage
        self.fire_rate = fire_rate

    def update(self):
        self.move()

    def check_collision(self):
        pass

    def move(self):
        raise NotImplementedError("VehicleInterface.move() has not been implemented.")

    def take_damage(self):
        raise NotImplementedError("VehicleInterface.take_damage() has not been implemented.")

    def fire_missile(self):
        raise NotImplementedError("VehicleInterface.fire_missile() has not been implemented.")