import os, pygame

import Constants

from platforms import Platform
from Spritesheet_Functions import Spritesheet

class create_fire_enemy(pygame.sprite.Sprite):

    # Player movement speed vars
    change_x = 0
    change_y = 0
    counter = 0


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
        sprite_sheet = Spritesheet("FireEnemy.png")

        # Load all right facing images into the list
        image = sprite_sheet.get_image(0,0,68,123)
        self.walking_frames_r.append(image)
        self.walking_frames_l.append(pygame.transform.flip(image, True, False))
        image = sprite_sheet.get_image(157,123,67,120)
        self.walking_frames_r.append(image)
        self.walking_frames_l.append(pygame.transform.flip(image, True, False))
        image = sprite_sheet.get_image(313,244,73,117)
        self.walking_frames_r.append(image)
        self.walking_frames_l.append(pygame.transform.flip(image, True, False))

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()

        self.health = 3

    # Find new position for the Player
    def update(self):
        #Gravity
        self.calc_grav()

        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos//30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos//30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        self.move()

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
            self.change_y = 1
        # Check if we are on the ground
        if self.rect.y >= Constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = Constants.SCREEN_HEIGHT - self.rect.height

    def move(self):
        # Enemy movement
        self.distance = 240
        self.speed = 1
        self.rect.y += self.change_y

        if self.counter >= 0 and self.counter <= self.distance:
            self.direction = "R"
            self.rect.x += self.speed
        elif self.counter >= self.distance and self.counter <= self.distance*2:
            self.direction = "L"
            self.rect.x -= self.speed
        else:
            self.counter = 0

        self.counter += 1

    def get_health(self):
        return self.health

    def take_damage(self,damage):
        self.health -= damage

    def get_direction(self):
        return self.direction

class create_monk_enemy(pygame.sprite.Sprite):

    # Player movement speed vars
    change_x = 0
    change_y = 0
    counter = 0


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
        sprite_sheet = Spritesheet("MonkEnemy.png")

        # Load all right facing images into the list
        image = sprite_sheet.get_image(0,0,90,118)
        self.walking_frames_r.append(image)
        self.walking_frames_l.append(pygame.transform.flip(image, True, False))
        image = sprite_sheet.get_image(731,120,86,115 )
        self.walking_frames_r.append(image)
        self.walking_frames_l.append(pygame.transform.flip(image, True, False))
        image = sprite_sheet.get_image(638,240,82,115)
        self.walking_frames_r.append(image)
        self.walking_frames_l.append(pygame.transform.flip(image, True, False))

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()

        self.health = 3

    # Find new position for the Player
    def update(self):
        #Gravity
        self.calc_grav()

        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos//30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos//30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        self.move()

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
            self.change_y = 1
        # Check if we are on the ground
        if self.rect.y >= Constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = Constants.SCREEN_HEIGHT - self.rect.height

    def move(self):
        # Enemy movement
        self.distance = 240
        self.speed = 1
        self.rect.y += self.change_y

        if self.counter >= 0 and self.counter <= self.distance:
            self.direction = "R"
            self.rect.x += self.speed
        elif self.counter >= self.distance and self.counter <= self.distance*2:
            self.direction = "L"
            self.rect.x -= self.speed
        else:
            self.counter = 0

        self.counter += 1

    def get_health(self):
        return self.health

    def take_damage(self,damage):
        self.health -= damage

    def get_direction(self):
        return self.direction
