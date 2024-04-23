import pygame

default_styles = {
  "line_color": (200, 200, 200),
  "circle_color": (225, 55, 225),
}


class Slider:
  def __init__(self, x, y, width, height, value, min_value=0, max_value=100, styles=default_styles):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.min_value = min_value
    self.max_value = max_value
    self.value = min(max_value, max(min_value, value))
    self.styles = styles

  def update(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    circle_x = self.x + (self.value - self.min_value) / (self.max_value - self.min_value) * self.width
    circle_diameter = self.height
    circle_y = self.y + circle_diameter

    if (abs(mouse_x - circle_x) < circle_diameter and \
      abs(mouse_y - circle_y) < circle_diameter):
      if mouse_pressed[0]:
        self.is_holding = True

    if not mouse_pressed[0]:
      self.is_holding = False

    if self.is_holding:
      relative_x = mouse_x - self.x
      relative_x = max(0, min(self.width, relative_x))
      self.value = round((relative_x / self.width) * (self.max_value - self.min_value) + self.min_value)

  def display(self, screen):
    pygame.draw.rect(screen, self.styles["line_color"], (self.x, self.y, self.width, self.height), 2, 8)
    circle_x = self.x + (self.value - self.min_value) / (self.max_value - self.min_value) * self.width
    pygame.draw.circle(screen, self.styles["circle_color"], (int(circle_x), self.y + (self.height / 2)), self.height/2)
