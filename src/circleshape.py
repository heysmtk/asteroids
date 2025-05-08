import pygame


# Base class for all circular game objects (e.g., player, asteroids, shots)
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        """
        Initializes a circular game object with position, velocity, and radius.
        Automatically adds to sprite group if 'containers' attribute is defined.
        """
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Override this method to define how the shape is drawn."""
        pass

    def update(self, dt):
        """Override this method to define how the shape updates each frame."""
        pass

    def collides_with(self, other):
        """
        Checks for collision with another CircleShape object using simple distance-based detection.
        Returns True if the two circles overlap.
        """
        return self.position.distance_to(other.position) <= self.radius + other.radius