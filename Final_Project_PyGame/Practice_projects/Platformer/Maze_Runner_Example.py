import pygame

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
purple = (255,0,255)

# This class represents the wall at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # constructor
    def __init__(self,x,y,width,height,color):
        # Call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, size of specified params
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

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
    def move(self,walls):

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

class Room():
    # Base class for all rooms

    # Each room has a list of walls, and of enemy sprites
    walls_list = None
    enemy_sprites = None

    # constructor to create our lists
    def __init__(self):
        self.walls_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

class Room1:
    # This will ceat the walls in room 1
    def __init__(self):
        Room.__init__(self)

        # Make a list of walls (x_pos, y_pos, width, height)
        walls = [[0,0,20,250,white],
        [0,350,20,250,white],
        [780,0,20,250,white],
        [780,350,20,250,white],
        [20,0,760,20,white],
        [20,580,760,20,white],
        [390,50,20,500,blue]]

        for item in walls:
            wall = Wall(item[0],item[1],item[2],item[3],item[4])
            self.walls_list.add(wall)

class Room2:
    # This will ceat the walls in room 1
    def __init__(self):
        Room.__init__(self)

        # Make a list of walls (x_pos, y_pos, width, height)
        walls = [[0,0,20,250,red],
        [0,350,20,250,red],
        [780,0,20,250,red],
        [780,350,20,250,red],
        [20,0,760,20,red],
        [20,580,760,20,red],
        [190,50,20,500,green],
        [590,50,20,500,green]]

        for item in walls:
            wall = Wall(item[0],item[1],item[2],item[3],item[4])
            self.walls_list.add(wall)

class Room3:
    # This will ceat the walls in room 1
    def __init__(self):
        Room.__init__(self)

        # Make a list of walls (x_pos, y_pos, width, height)
        walls = [[0,0,20,250,purple],
        [0,350,20,250,purple],
        [780,0,20,250,purple],
        [780,350,20,250,purple],
        [20,0,760,20,purple],
        [20,580,760,20,purple]]

        for item in walls:
            wall = Wall(item[0],item[1],item[2],item[3],item[4])
            self.walls_list.add(wall)

        for x in range(100,800, 100):
            for y in range(50,541, 300):
                wall = Wall(x,y,20,200,red)
                self.walls_list.add(wall)

        for x in range(150,700, 100):
            wall = Wall(x,200,20,200,white)
            self.walls_list.add(wall)

def main():
    # Initialize pygame
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800,600])

    # Set the title of the display window
    pygame.display.set_caption("Test")

    # Create the player sprite
    player = Player(50,50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_number = 0
    current_room = rooms[current_room_number]

    clock = pygame.time.Clock()

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

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


        player.move(current_room.walls_list)

        if player.rect.x < -15:
            if current_room_number == 0:
                current_room_number = 2
                current_room = rooms[current_room_number]
                player.rect.x = 790
            elif current_room_number == 2:
                current_room_number = 1
                current_room = rooms[current_room_number]
                player.rect.x = 790
            else:
                current_room_number = 0
                current_room = rooms[current_room_number]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_number == 0:
                current_room_number = 1
                current_room = rooms[current_room_number]
                player.rect.x = 0
            elif current_room_number == 1:
                current_room_number = 2
                current_room = rooms[current_room_number]
                player.rect.x = 0
            else:
                current_room_number = 0
                current_room = rooms[current_room_number]
                player.rect.x = 0

        screen.fill(black)

        movingsprites.draw(screen)
        current_room.walls_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
