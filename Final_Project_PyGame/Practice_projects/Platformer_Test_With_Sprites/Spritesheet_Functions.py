# Used to pull sprites out of spritesheets

import os, pygame

import Constants

class Spritesheet(object):
    # Class used to grab each sprite form the spritesheets
    sprite_sheet = None

    def __init__(self,filename):
        # Pass in the file name of the spritesheet

        # Load sheet
        self.sprite_sheet = pygame.image.load(os.path.join("C:/School/11th Quarter/3D Scripting/3D-Scripting/Final_Project_PyGame/Practice_projects/Platformer_Test_With_Sprites", filename)).convert_alpha()

    def get_image(self,x,y,width,height):
        # Grab single image from the sheet
        # Pass in x and y position of the sprite, and its width and height

        # Create blank image
        image = pygame.Surface([width,height]).convert()

        # Copy the sprite from the larger sheet onto the smaller image
        image.blit(self.sprite_sheet,(0,0),(x,y,width,height))

        # Assuming black works as the transparent color
        image.set_colorkey(Constants.black)

        # Return the image
        return image