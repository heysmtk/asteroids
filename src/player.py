import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        """Initializes the player with a starting position, rotation, and shooting cooldown."""
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        """Draws the player as a triangle on the screen."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        """
        Calculates the three points of the player's triangle shape based on position and rotation.
        Returns a list of three vectors representing the triangle's corners.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        """
        Handles keyboard input and updates the player's state.
        W/S to move forward/backward, A/D to rotate, SPACE to shoot.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def shoot(self):
        """
        Fires a shot in the direction the player is facing if the cooldown has expired.
        Resets the shooting timer after firing.
        """
        if self.shoot_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def rotate(self, dt):
        """Rotates the player based on turn speed and delta time."""
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Moves the player forward in the direction they are currently facing."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt