import pygame

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

# This class represents the wall at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # constructor
    def __init__(self,x,y,width,height):
        # Call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, size of specified params
        self.image = pygame.Surface([width,height])
        self.image.fill(blue)

        # Make the top left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    # constructor
    def __init__(self,x,y):
        #call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height and width
        self.image = pygame.Surface([15,15])
        self.image.fill(white)

        # Make the top left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    # Change the speed of the character
    def changespeed(self,x,y):
        self.change_x += x
        self.change_y += y

    # Find new position for the Player
    def update(self,walls):

        # Move left and right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
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
        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                # Otherwise if we are moving left, do the opposite
                self.rect.top = block.rect.bottom

# Initialize pygame
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800,600])

# Set the title of the display window
pygame.display.set_caption("Test")

# Create a surface we can draw on
background = pygame.Surface(screen.get_size())

# Used for converting color maps
background = background.convert()

# Fill the background with a color
background.fill(black)

# Create the player sprite
player = Player(50,50)
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)

# Make the walls (x_pos, y_pos, height, width)
walls_list = pygame.sprite.Group()

wall = Wall(0,0,10,600)
walls_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10,0,790,10)
walls_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10,200,100,10)
walls_list.add(wall)
all_sprite_list.add(wall)

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = true
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3,0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3,0)
            elif event.key == pygame.K_UP:
                player.changespeed(0,-3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3,0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3,0)
            elif event.key == pygame.K_UP:
                player.changespeed(0,3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,-3)

    player.update(walls_list)

    screen.fill(black)

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(40)

pygame.quit()
