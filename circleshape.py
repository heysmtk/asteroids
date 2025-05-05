import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        # Tohle přidáme: vytvoření self.rect
        self.rect = pygame.Rect(0, 0, radius * 2, radius * 2)
        self.rect.center = self.position

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        pass

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius