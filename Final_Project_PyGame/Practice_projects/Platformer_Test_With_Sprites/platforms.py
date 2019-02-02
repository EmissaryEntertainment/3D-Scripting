import pygame

from Spritesheet_Functions import Spritesheet

# These constants define our platforms
# Name of the file
# X and Y location of the sprite
# Width and Height of the sprite

purple_diamond = (0,0,252,66)
grey_crack = (258,2,252,66)
green_crack = (518,2,252,66)
blue_diamonds = (785,2,252,66)
concrete = (2,81,250,61)
purple_fancy_01 = (3,158,379,47)
purple_fancy_02 = (3,222,379,47)
blue_fancy_01 = (5,288,379,57)
blue_fancy_02 = (3,350,379,57)
blue_crack = (651,81,250,63)
cracked_wall = (650,159,250,63)
big_blue_square = (519,81,99,99)
small_blue_square = (938,81,54,54)
big_purple_square = (396,81,99,99)
small_purple_square = (938,152,54,54)

class Platform(pygame.sprite.Sprite):
    # constructor
    def __init__(self,sprite_sheet_data):
        # Call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = Spritesheet("Platforms.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        # Make the top left corner the passed-in location
        self.rect = self.image.get_rect()
