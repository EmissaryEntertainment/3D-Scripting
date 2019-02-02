import pygame

# list of colors for sprites
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
purple = (255,0,255)

# screen dimensions
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    level = None

    # constructor
    def __init__(self):
        #call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height and width
        self.image = pygame.Surface([15,15])
        self.image.fill(white)

        self.rect = self.image.get_rect()

    # Find new position for the Player
    def update(self):
        #Gravity
        self.calc_grav()

        # Move left and right
        self.rect.x += self.change_x
        pos = self.rect.x

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
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        # Move down a bit and see if there is a platform below us
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # When working with a platform moving down
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is okay to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    def move_left(self):
        # Called when the user hits the left arrow
        self.change_x = -6

    def move_right(self):
        # Called when the user hits the right arrow
        self.change_x = 6

    def stop(self):
        # Called when the user lets off the keyboard
        self.change_x = 0
        self.change_y = 0

class Platform(pygame.sprite.Sprite):
    # constructor
    def __init__(self,width,height):
        # Call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, size of specified params
        self.image = pygame.Surface([width,height])
        self.image.fill(green)

        # Make the top left corner the passed-in location
        self.rect = self.image.get_rect()

class Level():
    # Base class for all rooms

    # Each room has a list of walls, and of enemy sprites
    platform_list = None
    enemy_list = None

    # Background image
    background = None

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
        screen.fill(blue)

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

class Level_01(Level):
    # Definition for level 1
    def __init__(self,player):
        # Create level 1

        # Call parent constructor
        Level.__init__(self,player)

        # Create array with platform information
        level = [[210,70,500,500],[210,70,200,400],[210,70,600,300]]

        for platform in level:
            block = Platform(platform[0],platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

def main():
    # Main program
    pygame.init()

    # Set height and width of screen
    size = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # Set the name of the game window
    pygame.display.set_caption("Test")

    # Create the player
    player = Player()

    # Create the levels
    level_list = []
    level_list.append(Level_01(player))

    # Set the current level
    current_level_number = 0
    current_level = level_list[current_level_number]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 34
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    clock = pygame.time.Clock()

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_UP:
                    player.jump()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop()
                elif event.key == pygame.K_UP:
                    player.stop()

        # Update the player
        active_sprite_list.update()

        # Update the level
        current_level.update()

        # if the player gets near the right side, shift the world left (-x)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        # If the player gets near the left side, shift the world left (x)
        if player.rect.left < 0:
            player.rect.left = 0

        # ALL CODE FOR DRAWING THE LEVEL GOES BELOW THIS LINE
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        pygame.display.flip()

        # Limits the fps of the game
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
