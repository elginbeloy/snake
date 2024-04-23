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
  screen.fill_background(styles["background_color"])
  title_text = styles["title_font"].render(f'S N A K E', True, styles["tile_color"])
  screen.blit(title_text, (SCREEN_WIDTH - title_text.get_width() - 48, 48))
  subtitle_text = styles["subtitle_font"].render(f"Snakey Snakey Wee Wee", True, styles["subtitle_color"])
  screen.blit(subtitle_text, (SCREEN_WIDTH - subtitle_text.get_width() - 48, 48))


death_menu_styles = {
  "background_color": (255, 25, 55),
  "title_font": pygame.font.Font(pygame.font.get_default_font(), 48),
  "title_color": (55, 255, 55),
  "subtitle_font": pygame.font.Font(pygame.font.get_default_font(), 24),
  "subtitle_color": (225, 225, 225),
}

def show_death_menu(screen):
  styles = main_menu_styles
  screen.fill_background(styles["background_color"])
  title_text = styles["title_font"].render(f'S N A K E', True, styles["tile_color"])
  screen.blit(title_text, (SCREEN_WIDTH - title_text.get_width() - 48, 48))
  subtitle_text = styles["subtitle_font"].render(f"Snakey Snakey Wee Wee", True, styles["subtitle_color"])
  screen.blit(subtitle_text, (SCREEN_WIDTH - subtitle_text.get_width() - 48, 48))

