import pygame
from vehicle_interface import VehicleInterface


class Player(VehicleInterface):
    def __init__(self):
        VehicleInterface.__init__(self, 'unicorn.png', 3, 5, 5, 1, 3)