import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        """
        Initializes an Asteroid at the given position and radius.
        Optionally accepts a velocity vector.
        """
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        """Draws the asteroid as a white circle outline."""
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """Updates the asteroid's position based on its velocity and delta time."""
        self.position += self.velocity * dt

    def split(self):
        """
        Splits the asteroid into two smaller ones when destroyed.
        - If the asteroid is already at or below the minimum size, it is simply removed.
        - Otherwise, it is destroyed and replaced by two smaller asteroids.
        - The two new asteroids move in opposite directions, rotated from the original velocity.
        - Their size is reduced, and speed slightly increased.
        """
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vect1 = self.velocity.rotate(random_angle)
            vect2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, new_radius, vect1 * 1.2)
            Asteroid(self.position.x, self.position.y, new_radius, vect2 * 1.2)