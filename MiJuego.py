import pygame 
import sys
import random
from pygame.math import Vector2

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def check_collision(player_rect, mini_cube_rect):
    return player_rect.colliderect(mini_cube_rect)

pygame.init()

window_screen = (642, 361)
screen = pygame.display.set_mode(window_screen)
clock = pygame.time.Clock()

background = pygame.image.load("Fondo_2.jpg").convert()

player = pygame.image.load("Personaje.png").convert()
player.set_colorkey([255, 255, 255])
player_position = Vector2(100, 100)
player_speed = 10

mini_cube_size = 5
mini_cube_color = (255, 0, 0)
mini_cubes = [pygame.Rect(random.randint(0, window_screen[0] - mini_cube_size), random.randint(0, window_screen[1] - mini_cube_size),mini_cube_size, mini_cube_size) for _ in range(50)]

font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    player_position.x = clamp(player_position.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed, 0, window_screen[0] - player.get_width())
    player_position.y = clamp(player_position.y + (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed, 0, window_screen[1] - player.get_height())

    player_rect = pygame.Rect(player_position.x, player_position.y, player.get_width(), player.get_height())

    screen.blit(background, [0, 0])
    screen.blit(player, player_position)

    for mini_cube in mini_cubes:
        pygame.draw.rect(screen, mini_cube_color, mini_cube)

    for mini_cube in mini_cubes[:]:
        if check_collision(player_rect, mini_cube):
            mini_cubes.remove(mini_cube)
            print("Capturaste un mini cuadrito!")

    if not mini_cubes:
        text = font.render("¡Ganaste!", True, (0, 0, 0))
        screen.blit(text, (window_screen[0] // 2 - text.get_width() // 2, window_screen[1] // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)