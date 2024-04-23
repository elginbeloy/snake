import pygame
pygame.init()
pygame.font.init()

import random
from menus import show_main_menu, show_death_menu

# Game constants
TILE_SIZE = 20
ROWS = 40
COLUMNS = 60
SCREEN_WIDTH = TILE_SIZE * COLUMNS
SCREEN_HEIGHT = TILE_SIZE * ROWS
FPS = 60
APPLE_AMOUNT = 20

SNAKE_HEAD_COLOR = (115, 15, 255)
SNAKE_COLOR = (155, 35, 245)
SNAKE_GLOW_COLOR = (155, 35, 245, 75)
APPLE_COLOR = (255, 35, 0)
APPLE_GLOW_COLOR = (255, 35, 0, 55)
BACKGROUND_COLOR = (15, 15, 35)
GRID_COLOR = (25, 25, 55)
SCORE_COLOR = (255, 255, 255)

# Setup game window and clock
font = pygame.font.Font(pygame.font.get_default_font(), 40)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Create all the tiles for the grid, snake, and apple
tiles = []
for row_index in range(ROWS):
  tile_row = []
  for column_index in range(COLUMNS):
    rect_args = [column_index, row_index, 1, 1]
    tile_row.append(pygame.Rect(*[arg*TILE_SIZE for arg in rect_args]))
  tiles.append(tile_row)

snake_tiles = [(len(tiles)//2, len(tiles[0])//2)]
apple_tiles = [
  (random.randint(0, ROWS-1),
  random.randint(0, COLUMNS-1)) for _ in range(APPLE_AMOUNT)]

# Initial snake speed and direction
snake_direction = 'right'
snake_movements_per_second = 10
score = 0

# Main game loop
running = True
frame = 0
while running:
  clock.tick(FPS)
  frame += 1
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT and snake_direction != "right":
        snake_direction = "left"
      if event.key == pygame.K_RIGHT and snake_direction != "left":
        snake_direction = "right"
      if event.key == pygame.K_UP and snake_direction != "down":
        snake_direction = "up"
      if event.key == pygame.K_DOWN and snake_direction != "up":
        snake_direction = "down"

  screen.fill(BACKGROUND_COLOR)
  for row_index, row in enumerate(tiles):
    for column_index, tile in enumerate(row):
      tile_cords = (row_index, column_index)
      if tile_cords not in snake_tiles and tile_cords not in apple_tiles:
        pygame.draw.rect(screen, GRID_COLOR, tile, 1)

  score_text = font.render(f'Score: {score}', True, SCORE_COLOR)
  screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 20, 20))

  for cords_index, cords in enumerate(snake_tiles):
    snake_glow_surface = pygame.Surface((TILE_SIZE + 10, TILE_SIZE + 10), pygame.SRCALPHA)
    snake_glow_surface.fill(SNAKE_GLOW_COLOR)
    screen.blit(snake_glow_surface, (tiles[cords[0]][cords[1]].x - 5, tiles[cords[0]][cords[1]].y - 5))
    if cords_index == len(snake_tiles) - 1:
      pygame.draw.rect(screen, SNAKE_HEAD_COLOR, tiles[cords[0]][cords[1]])
    else:
      pygame.draw.rect(screen, SNAKE_COLOR, tiles[cords[0]][cords[1]])

  for cords in apple_tiles:
    apple_glow_surface = pygame.Surface((TILE_SIZE + 10, TILE_SIZE + 10), pygame.SRCALPHA)
    apple_glow_surface.fill(APPLE_GLOW_COLOR)
    screen.blit(apple_glow_surface, (tiles[cords[0]][cords[1]].x - 5, tiles[cords[0]][cords[1]].y - 5))
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
        score += 1
        if len(snake_tiles) % 10 == 0:
          snake_movements_per_second += 1
        apple_tiles.remove(new_head)
        apple_tiles.append((random.randint(0, ROWS-1), random.randint(0, COLUMNS-1)))
      else:
        snake_tiles.pop(0)

  pygame.display.flip()

pygame.quit()
print("You died! Score: " + str(score))
