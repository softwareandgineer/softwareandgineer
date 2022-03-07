import pygame
import math

pygame.init()

surface_size = 1024
main_surface= pygame.display.set_mode((surface_size, surface_size))
my_clock = pygame.time.Clock()
color1 = (255,0,0)
color2 = (0,0,255)


def draw_tree(main_surface, order, theta, size, position, heading, color=(0, 0, 0), depth=0):
    global color1
    global color2

    trunk_ratio = 0.29
    trunk = size * trunk_ratio
    delta_x = trunk * math.cos(heading)
    delta_y = trunk * math.sin(heading)
    (u, v) = position

    newposition = (u + delta_x, v + delta_y)

    pygame.draw.line(main_surface, color, position, newposition)
    if order > 0:
        color1 = ((color[0] + depth * 10)%255, (color[1] + depth * 10)%255, (color[2] + depth * 10)%255)
        color2 = ((color[0] + depth * 30) % 255, (color[1] + depth * 30) % 255, (color[2] + depth * 30) % 255)


        newsize = size * (1 - trunk_ratio)
        draw_tree(main_surface, order - 1, theta, newsize, newposition, heading - theta, color1, depth + 1)
        draw_tree(main_surface, order - 1, theta, newsize, newposition, heading + theta, color2, depth + 1)


def gameloop():
    theta = 0
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        theta += 0.01

        main_surface.fill((255,255,0))
        draw_tree(main_surface, 15, theta, surface_size * 0.9, (surface_size // 2, surface_size - 50), -math.pi / 2, (200, 20, 20))
        pygame.display.flip()
        my_clock.tick(60)


gameloop()
