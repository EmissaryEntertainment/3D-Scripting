import os, pygame

from Player import create_player

import levels

import Constants

def main():
    # Main program
    pygame.init()

    # Set height and width of screen
    size = [Constants.SCREEN_WIDTH,Constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # Set the name of the game window
    pygame.display.set_caption("Test")

    # Create the player
    player = create_player()

    # Create the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_01(player))

    # Set the current level
    current_level_number = 0
    current_level = level_list[current_level_number]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 1
    player.rect.y = Constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    clock = pygame.time.Clock()

    done = False
    shift = True

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

        # Update the player
        active_sprite_list.update()

        # Update the level
        current_level.update()

        # if the player gets near the right side, shift the world left (-x)
        current_position = player.rect.x + current_level.world_shift
        if player.rect.x >= 500 and shift == True:
            diff = player.rect.x - 500
            if current_position < current_level.level_limit:
                diff = 0
                shift = False
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world left (x)
        if player.rect.x <= 1:
            player.rect.x = 0

        print(player.rect.x)
        if player.rect.x >= 800:
            player.rect.x = 120
            if current_level_number < len(level_list) - 1:
                current_level_number += 1
                current_level = level_list[current_level_number]
                player.level = current_level
                shift = True

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
