import pygame
from pygame.locals import *

pygame.init()

FPS = 60
CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 704, 704
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

class Chargie():
  size = (WIDTH + HEIGHT) // 11
  x = (WIDTH // 2) - (size // 2)
  y = (HEIGHT // 2) - (size // 2)
  image = pygame.transform.scale(pygame.image.load('./resources/images/cg_south_1.png').convert_alpha(),(size, size))
  speed = size // 32
  angle = 0
  count = 1
  def show():
    rotate = pygame.transform.rotate(Chargie.image, Chargie.angle)
    rect = rotate.get_rect(center=Chargie.image.get_rect(topleft=(Chargie.x, Chargie.y)).center)
    DISPLAY.blit(rotate, rect.topleft)
  def handle():
    def check():
      if Chargie.count >= 5:
        Chargie.count = 1
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
      Chargie.y -= Chargie.speed
      Chargie.image = pygame.transform.scale(pygame.image.load('./resources/images/cg_north_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 0.1
      check()
    if keys_pressed[pygame.K_a]:
      Chargie.x -= Chargie.speed
      Chargie.image = pygame.transform.scale(pygame.image.load('./resources/images/cg_west_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 0.1
      check()
    if keys_pressed[pygame.K_s]:
      Chargie.y += Chargie.speed
      Chargie.image = pygame.transform.scale(pygame.image.load('./resources/images/cg_south_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 0.1
      check()
    if keys_pressed[pygame.K_d]:
      Chargie.x += Chargie.speed
      Chargie.image = pygame.transform.scale(pygame.image.load('./resources/images/cg_east_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 0.1
      check()

while True:
  DISPLAY.fill("#404040")
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
  Chargie.handle()
  Chargie.show()
  pygame.display.flip()
  CLOCK.tick(FPS)