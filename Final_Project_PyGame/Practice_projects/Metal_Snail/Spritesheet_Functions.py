# Used to pull sprites out of spritesheets

import os, pygame, sys

import Constants

class Spritesheet(object):
    # Class used to grab each sprite form the spritesheets
    sprite_sheet = None

    def __init__(self,filename):
        # Pass in the file name of the spritesheet

        # Load sheet
        directory_name = (sys.path[0] + "\Assets")
        self.sprite_sheet = pygame.image.load(os.path.join(directory_name, filename)).convert_alpha()

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
