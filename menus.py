import pygame

main_menu_styles = {
  "background_color": (255, 25, 55),
  "title_font": pygame.font.Font(pygame.font.get_default_font(), 48),
  "title_color": (55, 255, 55),
  "subtitle_font": pygame.font.Font(pygame.font.get_default_font(), 24),
  "subtitle_color": (225, 225, 225),
}

def show_main_menu(screen):
  styles = main_menu_styles
  screen.fill(styles["background_color"])
  title_text = styles["title_font"].render('S N A K E', True, styles["title_color"])
  screen.blit(title_text, (screen.get_width() / 2 - title_text.get_width() / 2, 100))
  subtitle_text = styles["subtitle_font"].render("Press any key to start", True, styles["subtitle_color"])
  screen.blit(subtitle_text, (screen.get_width() / 2 - subtitle_text.get_width() / 2, 200))
  pygame.display.flip()
  waiting = True
  while waiting:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      if event.type == pygame.KEYDOWN:
        waiting = False

death_menu_styles = {
  "background_color": (25, 25, 55),
  "title_font": pygame.font.Font(pygame.font.get_default_font(), 48),
  "title_color": (255, 55, 55),
  "subtitle_font": pygame.font.Font(pygame.font.get_default_font(), 24),
  "subtitle_color": (225, 225, 225),
}

def show_death_menu(screen, score):
  styles = death_menu_styles
  screen.fill(styles["background_color"])
  title_text = styles["title_font"].render('Game Over', True, styles["title_color"])
  screen.blit(title_text, (screen.get_width() / 2 - title_text.get_width() / 2, 100))
  score_text = styles["subtitle_font"].render(f'Score: {score}', True, styles["subtitle_color"])
  screen.blit(score_text, (screen.get_width() / 2 - score_text.get_width() / 2, 200))
  pygame.display.flip()
  pygame.time.wait(2000)
