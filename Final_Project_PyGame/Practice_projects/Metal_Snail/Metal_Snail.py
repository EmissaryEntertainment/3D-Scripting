import os, pygame, sys

from Player import create_player

import levels

import Constants

import spells

import enemies

import time

def main():
    # Main program
    pygame.init()

    score = 0
    # Set height and width of screen
    size = [Constants.SCREEN_WIDTH,Constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # Set the name of the game window
    pygame.display.set_caption("Metal_Snail")
    directory_name = (sys.path[0] + "\Assets")
    font = pygame.font.Font(os.path.join(directory_name, "Romulus.ttf"),40)

    # Create the player
    player = create_player()

    # Create the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # Set the current level
    current_level_number = 0
    current_level = level_list[current_level_number]

    active_sprite_list = pygame.sprite.Group()
    enemy_sprite_list = pygame.sprite.Group()
    firebolt_list = pygame.sprite.Group()
    enemy_firebolt_list = pygame.sprite.Group()
    player_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 1
    player.rect.y = Constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    player_list.add(player)
    active_sprite_list.add(current_level.get_enemy_list())
    enemy_sprite_list.add(current_level.get_enemy_list())

    clock = pygame.time.Clock()

    done = False
    shift = True

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.move_left()
                elif event.key == pygame.K_d:
                    player.move_right()
                elif event.key == pygame.K_SPACE:
                    player.jump()
                elif event.key == pygame.K_RETURN:
                    # Fire a firebolt if the user clicks the mouse button
                    firebolt = spells.Firebolt()
                    # Set the firebolt so it is where the player is, and so it shoots the same direction as the player
                    if player.get_direction() == "R":
                        firebolt.rect.x = player.rect.x + 25
                        firebolt.rect.y = player.rect.y + 25
                        firebolt.shoot_right()
                    elif player.get_direction() == "L":
                        firebolt.rect.x = player.rect.x - 25
                        firebolt.rect.y = player.rect.y + 25
                        firebolt.shoot_left()
                    # Add the firebolt to the lists
                    active_sprite_list.add(firebolt)
                    firebolt_list.add(firebolt)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player.stop()

        # Update the player
        active_sprite_list.update()
        for enemy in enemy_sprite_list:
            enemy_firebolt = spells.Enemy_Firebolt()
            if enemy.get_direction() == "R":
                enemy_firebolt.rect.x = enemy.rect.x + 25
                enemy_firebolt.rect.y = enemy.rect.y + 25
                enemy_firebolt.shoot_right()
            elif enemy.get_direction() == "L":
                enemy_firebolt.rect.x = enemy.rect.x - 25
                enemy_firebolt.rect.y = enemy.rect.y + 25
                enemy_firebolt.shoot_left()
            active_sprite_list.add(enemy_firebolt)
            enemy_firebolt_list.add(enemy_firebolt)

        # Calculate mechanics for enemy firebolts
        for firebolt in enemy_firebolt_list:
            # See if it hit the player
            block_hit_list = pygame.sprite.spritecollide(firebolt, player_list, False)
            # When a firebolt hits the player deduct the players health based on the firebolts damage
            for block in block_hit_list:
                block.take_damage(firebolt.get_damage())
                enemy_firebolt_list.remove(firebolt)
                active_sprite_list.remove(firebolt)
                if block.get_health() <= 0:
                    enemy_sprite_list.remove(block)
                    active_sprite_list.remove(block)
                    player_list.remove(player_list)

        # Calculate mechanics for player firebolt
        for firebolt in firebolt_list:
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(firebolt, enemy_sprite_list, False)
            # When a firebolt hits an enemy deduct the enemies health based on the firebolts damage
            for block in block_hit_list:
                block.take_damage(firebolt.get_damage())
                firebolt_list.remove(firebolt)
                active_sprite_list.remove(firebolt)
                if block.get_health() <= 0:
                    score += 100
                    enemy_sprite_list.remove(block)
                    active_sprite_list.remove(block)
                    current_level.get_enemy_list().remove(block)

                # Remove the firebolt if it flies up off the screen
            if firebolt.rect.x < -10:
                firebolt_list.remove(firebolt)
                active_sprite_list.remove(firebolt)

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

        if player.rect.x >= 800:
            player.rect.x = 120
            if current_level_number < len(level_list) - 1:
                current_level_number += 1
                current_level = level_list[current_level_number]
                player.level = current_level
                active_sprite_list.add(current_level.get_enemy_list())
                enemy_sprite_list.add(current_level.get_enemy_list())
                shift = True

        # ALL CODE FOR DRAWING THE LEVEL GOES BELOW THIS LINE
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        text_surface = font.render("Health: " + str(player.get_health()), True, Constants.black)
        TextRect = text_surface.get_rect()
        TextRect.center = (90,20)
        screen.blit(text_surface,TextRect)
        text_surface = font.render("Score: " + str(score), True, Constants.black)
        TextRect = text_surface.get_rect()
        TextRect.center = (650,20)
        screen.blit(text_surface,TextRect)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        pygame.display.flip()
        pygame.display.update()

        # Limits the fps of the game
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
