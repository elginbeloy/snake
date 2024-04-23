import pygame
from widgets import Slider

styles = {
  "background_color": (25, 25, 55),
  "title_font": pygame.font.Font(pygame.font.get_default_font(), 48),
  "title_color": (255, 55, 55),
  "subtitle_font": pygame.font.Font(pygame.font.get_default_font(), 28),
  "subtitle_color": (225, 225, 225),
}

def wait_for_keypress(update_func, FPS=10):
  clock = pygame.time.Clock()
  waiting = True
  while waiting:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      if event.type == pygame.KEYDOWN:
        waiting = False

      update_func()

def show_main_menu(screen):
  slider = Slider((screen.get_width() / 2) - 100, 300, 200, 30, 10, max_value=100)
  title_text = styles["title_font"].render('S  N  A  K  E', True, styles["title_color"])
  subtitle_text = styles["subtitle_font"].render("Press any key to start", True, styles["subtitle_color"])

  def update_func():
    screen.fill(styles["background_color"])
    screen.blit(title_text, (screen.get_width() / 2 - title_text.get_width() / 2, 100))
    screen.blit(subtitle_text, (screen.get_width() / 2 - subtitle_text.get_width() / 2, 200))

    apples = slider.value
    apples_text = styles["subtitle_font"].render(f"Apple Amount: {apples}", True, styles["subtitle_color"])
    screen.blit(apples_text, (screen.get_width() / 2 - apples_text.get_width() / 2, 250))
    slider.display(screen)
    slider.update()
    pygame.display.flip()

  wait_for_keypress(update_func, FPS=60)
  return slider.value

def show_death_menu(screen, score):
  slider = Slider((screen.get_width() / 2) - 100, 320, 200, 30, 10, max_value=100)
  title_text = styles["title_font"].render('Game Over', True, styles["title_color"])
  score_text = styles["subtitle_font"].render(f'Score: {score}', True, styles["subtitle_color"])
  subtitle_text = styles["subtitle_font"].render(f'Press any key to restart', True, styles["subtitle_color"])

  screen.fill(styles["background_color"])
  screen.blit(title_text, (screen.get_width() / 2 - title_text.get_width() / 2, 100))
  screen.blit(score_text, (screen.get_width() / 2 - score_text.get_width() / 2, 180))
  pygame.display.flip()
  pygame.time.wait(1000)

  def update_func():
    screen.fill(styles["background_color"])
    screen.blit(title_text, (screen.get_width() / 2 - title_text.get_width() / 2, 100))
    screen.blit(score_text, (screen.get_width() / 2 - score_text.get_width() / 2, 180))
    screen.blit(subtitle_text, (screen.get_width() / 2 - subtitle_text.get_width() / 2, 240))

    apples = slider.value
    apples_text = styles["subtitle_font"].render(f"Apple Amount: {apples}", True, styles["subtitle_color"])
    screen.blit(apples_text, (screen.get_width() / 2 - apples_text.get_width() / 2, 280))
    slider.display(screen)
    slider.update()
    pygame.display.flip()

  update_func()
  wait_for_keypress(update_func, FPS=60)
  return slider.value
