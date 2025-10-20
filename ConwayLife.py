import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
GREEN = (67, 82, 61)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)

COLOR1 = CYAN
COLOR2 = BLACK
COLOR3 = BLACK

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()



def gen(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for i in range(num)])

def draw_grid(positions):
    screen.fill(COLOR3)
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, COLOR1, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, COLOR2, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, COLOR2, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2, 3]:
            new_positions.add(position)

    for position in all_neighbors:
        neighbors = get_neighbors(position)
        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions

def get_neighbors(pos):
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.append((x + dx, y + dy))

    return neighbors
def main():
    running = True
    playing = False
    count = 0
    update_frequency = 20

    positions = set()
    while running:
        clock.tick(FPS)

        if playing:
            count += 1

        if count >= update_frequency:
            count = 0
            positions = adjust_grid(positions)

        pygame.display.set_caption("Playing" if playing else "Stopped")

        for event in pygame.event.get():

            mousePressed = pygame.mouse.get_pressed()

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if mousePressed[0] == True:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions:
                    continue
                else:
                    positions.add(pos)

            if mousePressed[2] == True:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    continue

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False

                if event.key == pygame.K_2:
                    global COLOR1
                    global COLOR2
                    global COLOR3
                    COLOR1 = BLACK
                    COLOR2 = BLACK
                    COLOR3 = GREEN

                if event.key == pygame.K_3:
                    COLOR1 = BLACK
                    COLOR2 = GREEN
                    COLOR3 = GREEN

                if event.key == pygame.K_4:
                    COLOR1 = YELLOW
                    COLOR2 = BLACK
                    COLOR3 = GREY

                if event.key == pygame.K_1:
                    COLOR1 = CYAN
                    COLOR2 = BLACK
                    COLOR3 = BLACK

                if event.key == pygame.K_5:
                    COLOR1 = BLACK
                    COLOR2 = BLACK
                    COLOR3 = WHITE

                if event.key == pygame.K_r:
                    positions = gen(random.randrange(7, 9) * GRID_WIDTH,)

        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()