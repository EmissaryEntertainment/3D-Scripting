import os, pygame

import Constants

from platforms import Platform
from Spritesheet_Functions import Spritesheet

class create_player(pygame.sprite.Sprite):

    # Player movement speed vars
    change_x = 0
    change_y = 0

    # Store the images for the player animation
    walking_frames_r = []
    walking_frames_l = []

    # What direction is the player facing
    direction = "R"

    # List of sprites we can collide with
    level = None

    # constructor
    def __init__(self):
        #call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        # Load spritesheet
        sprite_sheet = Spritesheet("Character.png")

        # Load all right facing images into the list
        image = sprite_sheet.get_image(3,106,36,73)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(75,103,41,80)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(143,106,49,75)
        self.walking_frames_r.append(image)

        # Load all left facing images into the other list
        image = sprite_sheet.get_image(0,3,51,74)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(78,0,41,80)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(154,4,36,73)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()

    # Find new position for the Player
    def update(self):
        #Gravity
        self.calc_grav()

        # Move left and right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos//30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos//30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite
                self.rect.left = block.rect.right

        # Move up and down
        self.rect.y += self.change_y

        # Check to see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                # Otherwise if we are moving left, do the opposite
                self.rect.top = block.rect.bottom

    def calc_grav(self):
        # Calculate the effects of Gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # Check if we are on the ground
        if self.rect.y >= Constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = Constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        # Move down a bit and see if there is a platform below us
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # When working with a platform moving down
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is okay to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= Constants.SCREEN_HEIGHT:
            self.change_y = -10

    def move_left(self):
        # Called when the user hits the left arrow
        self.direction = "L"
        self.change_x = -6

    def move_right(self):
        # Called when the user hits the right arrow
        self.direction = "R"
        self.change_x = 6

    def stop(self):
        # Called when the user lets off the keyboard
        self.change_x = 0
        self.change_y = 0

    def get_direction(self):
        return self.direction
