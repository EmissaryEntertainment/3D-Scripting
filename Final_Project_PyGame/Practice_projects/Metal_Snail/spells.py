import os, pygame, sys
import Constants

class Firebolt(pygame.sprite.Sprite):
    # This class represents the bullet
    def __init__(self):
        # Call the parent constructor
        pygame.sprite.Sprite.__init__(self)

        directory_name = (sys.path[0] + "\Assets")
        self.image = pygame.image.load(os.path.join(directory_name, "Firebolt.png")).convert_alpha()

        self.shoot_speed = 0

        self.damage = 1

        self.rect = self.image.get_rect()

    def update(self):
        # Move the spell
        self.rect.x += self.shoot_speed

    def shoot_right(self):
        self.shoot_speed = 5

    def shoot_left(self):
        self.shoot_speed = -5

    def get_damage(self):
        return self.damage

class Enemy_Firebolt(pygame.sprite.Sprite):
    # This class represents the bullet
    def __init__(self):
        # Call the parent constructor
        pygame.sprite.Sprite.__init__(self)

        directory_name = (sys.path[0] + "\Assets")
        self.image = pygame.image.load(os.path.join(directory_name, "Enemy_Firebolt.png")).convert_alpha()

        self.shoot_speed = 0

        self.damage = 1

        self.rect = self.image.get_rect()

    def update(self):
        # Move the spell
        self.rect.x += self.shoot_speed

    def shoot_right(self):
        self.shoot_speed = 5

    def shoot_left(self):
        self.shoot_speed = -5

    def get_damage(self):
        return self.damage
