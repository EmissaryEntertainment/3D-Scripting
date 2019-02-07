import os, pygame
import Constants

class Firebolt(pygame.sprite.Sprite):
    # This class represents the bullet
    def __init__(self):
        # Call the parent constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join("C:/School/11th Quarter/3D Scripting/3D-Scripting/Final_Project_PyGame/Practice_projects/Metal_Snail", "Firebolt.png")).convert_alpha()

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
