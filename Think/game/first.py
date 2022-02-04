import pygame
import time

colors = [(0, 0, 0), (250, 250, 250)]

class QueenSprite:
    def __init__(self, img, position):
        self.img = img
        self.position = position

    def draw(self, target_surface):
        target_surface.blit(self.img, self.position)


def draw_chessboard(surface, n, square_size):
    for row in range(n):  # for n amount of rows
        for col in range(n):  # for n amount of columns
            color_index = (row + col) % 2  # remainder when % 2 is odd, it is one color, even it is the other
            the_square = (col * square_size, row * square_size, square_size,
                          square_size)  # first is the columns horizontally placed, second is row, 3rd and 4th are
            # position
            surface.fill(colors[color_index], the_square)  # color it in


def main():
    all_sprites = []

    pygame.init()  # initialize library
    surface_size = 480  # window size
    main_surface = pygame.display.set_mode((surface_size, surface_size))  # create window

    grid_size = surface_size / 8  # size of chessboard

    queen = pygame.image.load("queen.png")  # loads in image
    queen = pygame.transform.scale(queen, (grid_size, grid_size))

    queen1 = QueenSprite(queen, (3 * grid_size, 5 * grid_size))
    queen2 = QueenSprite(queen, (5 * grid_size, 3 * grid_size))

    all_sprites.append(queen1)
    all_sprites.append(queen2)
    # brackets are the size, transforms image into the size of grid

    my_font = pygame.font.SysFont("Times New Roman", 16)  # set font

    frame_count = 0
    frame_rate = 0
    t0 = time.perf_counter()  # records the time from time app opened to current
    while True:
        event = pygame.event.poll()  # poll gets the events of the user e.g arrow key presses, mouse movement,etc.
        if event.type == pygame.QUIT:  # special event for when game is terminated e.g window closed
            break

        if event.type != pygame.NOEVENT:
            print(event)

        if event.type == pygame.KEYDOWN:
            key = event.dict["key"]

            if key == 27:
                break

            if key == ord("r"):
                colors[0] = (255, 0, 0)
            elif key == ord("g"):
                colors[0] = (0, 255, 0)
            elif key == ord("b"):
                colors[0] = (0, 0, 255)
            elif key == ord("p"):
                colors[0] = (0, 0, 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = event.dict["pos"]
            all_sprites[0].position = (pos_mouse[0] - grid_size // 2, pos_mouse[1] - grid_size / 2)

        frame_count += 1  # every frame add one
        if frame_count % 500 == 0:  # every 500 frames update frame rate
            t1 = time.perf_counter()  # t1 calculates the time for 500 frames
            frame_rate = 500 / (t1 - t0)  # calculates rate by using t1 and t0
            t0 = t1  # sets t0 up for next calculations by settings t0 up

        main_surface.fill((50, 50, 100))  # makes a color for background

        draw_chessboard(main_surface, 8, grid_size)  # calling of the chessboardF

        #main_surface.blit(queen, (3 * grid_size, 3 * grid_size))  # prints out the queen, inside () is the position

        the_text = my_font.render("Frame = {0}, rate = {1:.2f} fps".format(frame_count, frame_rate), True, (0, 250, 0))
        main_surface.blit(the_text, (10, 10))

        for sprite in all_sprites:
            sprite.draw(main_surface)

        pygame.display.flip()

        pygame.display.flip()  # show everything

    pygame.quit()


main()
