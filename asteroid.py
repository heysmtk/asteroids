import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    # Překryjte metodu draw(), aby se asteroid vykreslil jako pygame.draw.circle. Použijte jeho polohu, poloměr a šířku 2.
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    # Překryjte metodu update() tak, aby se pohybovala po přímce konstantní rychlostí. Na každém snímku by měl ke své poloze přičíst (self.velocity * dt) (získejte self.velocity z jeho rodičovské třídy CircleShape).    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position