import pygame
import random

# Game constants
TILE_SIZE = 20
ROWS = 40
COLUMNS = 60
SCREEN_WIDTH = TILE_SIZE * COLUMNS
SCREEN_HEIGHT = TILE_SIZE * ROWS
FPS = 60
APPLE_AMOUNT = 5

# Initialize game window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

tiles = []
for row_index in range(ROWS):
  tile_row = []
  for column_index in range(COLUMNS):
    rect_args = [column_index, row_index, 1, 1]
    tile_row.append(pygame.Rect(*[arg*TILE_SIZE for arg in rect_args]))
  tiles.append(tile_row)

snake_tiles = [(len(tiles)//2, len(tiles[0])//2)]
snake_direction = 'left'
snake_movements_per_second = 10
apple_tiles = [(random.randint(0, ROWS-1), random.randint(0, COLUMNS-1)) for _ in range(APPLE_AMOUNT)]

# Colors
SNAKE_COLOR = (0, 255, 255)
APPLE_COLOR = (255, 165, 0)
BACKGROUND_COLOR = (25, 25, 25)
GRID_COLOR = (50, 50, 50)

# Main game loop
running = True
frame = 0
while running:
  dt = clock.tick(FPS)
  frame += 1
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        snake_direction = "left"
      if event.key == pygame.K_RIGHT:
        snake_direction = "right"
      if event.key == pygame.K_UP:
        snake_direction = "up"
      if event.key == pygame.K_DOWN:
        snake_direction = "down"

  screen.fill(BACKGROUND_COLOR)
  for row in tiles:
    for tile in row:
      pygame.draw.rect(screen, GRID_COLOR, tile, 1)

  for cords in snake_tiles:
    pygame.draw.rect(screen, SNAKE_COLOR, tiles[cords[0]][cords[1]])

  for cords in apple_tiles:
    pygame.draw.rect(screen, APPLE_COLOR, tiles[cords[0]][cords[1]])

  if frame % (FPS // snake_movements_per_second) == 0:
    head = snake_tiles[-1]
    if snake_direction == 'left':
      new_head = (head[0], head[1]-1)
    if snake_direction == 'right':
      new_head = (head[0], head[1]+1)
    if snake_direction == 'up':
      new_head = (head[0]-1, head[1])
    if snake_direction == 'down':
      new_head = (head[0]+1, head[1])
    if new_head in snake_tiles or new_head[0] < 0 or new_head[0] >= ROWS or new_head[1] < 0 or new_head[1] >= COLUMNS:
      running = False
    else:
      snake_tiles.append(new_head)
      if new_head in apple_tiles:
        if len(snake_tiles) % 10 == 0:
          snake_movements_per_second += 1
        apple_tiles.remove(new_head)
        apple_tiles.append((random.randint(0, ROWS-1), random.randint(0, COLUMNS-1)))
      else:
        snake_tiles.pop(0)

  pygame.display.flip()

pygame.quit()
