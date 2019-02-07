import os, pygame

import Constants
import platforms
import enemies

class Level():
    # Base class for all rooms

    # Each room has a list of walls, and of enemy sprites
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled to the left/right
    world_shift = 0
    level_limit = -1500

    # constructor to create our lists
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update the Level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self,screen):
        # Draw the Background
        screen.fill(Constants.blue)
        screen.blit(self.background,(self.world_shift // 3,0))

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        # When the user moves left/right, scroll the world

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

class Level_01(Level):
    # Definition for level 1
    def __init__(self,player):
        # Create level 1

        # Call parent constructor
        Level.__init__(self,player)

        # Limit for how far a level can scroll
        self.background = pygame.image.load(os.path.join("C:/School/11th Quarter/3D Scripting/3D-Scripting/Final_Project_PyGame/Practice_projects/Metal_Snail", "Background.png")).convert()
        self.background.set_colorkey(Constants.white)
        self.level_limit = -6050
        self.enemy = enemies.create_enemy()
        self.enemy.rect.x = 250
        self.enemy.rect.y = 499
        self.enemy.level = self
        self.enemy_list.add(self.enemy)
        self.enemy = enemies.create_enemy()
        self.enemy.rect.x = 550
        self.enemy.rect.y = 399
        self.enemy.level = self
        self.enemy_list.add(self.enemy)

        # Create array with type of platform, and x,y position of the platform
        level = [[platforms.purple_diamond,250,500],
                 [platforms.concrete,550,400]]

        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

    def get_enemy_list(self):
        return self.enemy_list
