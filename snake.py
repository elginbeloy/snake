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
snake_movements_per_second = 4
apple_tiles = [(random.randint(0, ROWS-1), random.randint(0, COLUMNS-1)) for _ in range(APPLE_AMOUNT)]

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

  screen.fill((0,0,0))
  for row in tiles:
    for tile in row:
      pygame.draw.rect(screen, (55, 55, 55), tile, 1)

  for cords in snake_tiles:
    pygame.draw.rect(screen, (255, 0, 0), tiles[cords[0]][cords[1]])

  for cords in apple_tiles:
    pygame.draw.rect(screen, (0, 255, 0), tiles[cords[0]][cords[1]])

  if frame % (FPS // snake_movements_per_second) == 0:
    head = snake_tiles[-1]
    if snake_direction == 'left':
      snake_tiles.append((head[0], head[1]-1))
    if snake_direction == 'right':
      snake_tiles.append((head[0], head[1]+1))
    if snake_direction == 'up':
      snake_tiles.append((head[0]-1, head[1]))
    if snake_direction == 'down':
      snake_tiles.append((head[0]+1, head[1]))
    if head in apple_tiles:
      apple_tiles.remove(head)
      apple_tiles.append((random.randint(0, ROWS-1), random.randint(0, COLUMNS-1)))
      snake_movements_per_second += 1
    else:
      snake_tiles.pop(0)

  pygame.display.flip()

pygame.quit()
