import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Sprite groups for update and draw logic
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Register sprite containers for auto-management
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    # Initialize objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0  # Delta time between frames

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all game objects
        updatable.update(dt)

        # Check collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        # Clear screen
        screen.fill("black")

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Check collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()          # Remove shot from the game
                    asteroid.split()     # Split or destroy asteroid

        # Update display
        pygame.display.flip()

        # Limit the framerate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()