import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        """
        Initializes a Shot object at the given position with a fixed radius.
        Inherits position and velocity from CircleShape.
        """
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        """Draws the shot as a white circle outline on the screen."""
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """Updates the position of the shot based on its velocity and delta time."""
        self.position += self.velocity * dt