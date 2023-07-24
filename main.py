import asyncio
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.font.init()
FPS = 60
CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 704, 704
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("Comic Sans MS", (WIDTH+HEIGHT)//64)

class Chargie():
  size = (WIDTH + HEIGHT) // 11
  x = (WIDTH // 2) - (size // 2)
  y = (HEIGHT // 2) - (size // 2)
  image = pygame.transform.scale(pygame.image.load('./img/cg_south_1.png').convert_alpha(),(size, size))
  speed = size // 32
  angle = 0
  count = 1
  queue = [""]
  heart = pygame.Rect((x + size//4), (y + size//3), size//2, size//2)
  def show():
    rect = pygame.Rect(0, 0, WIDTH, Chargie.size//2)
    pygame.draw.rect(DISPLAY, "#202020", rect)
    rotate = pygame.transform.rotate(Chargie.image, Chargie.angle)
    rect = rotate.get_rect(center=Chargie.image.get_rect(topleft=(Chargie.x, Chargie.y)).center)
    DISPLAY.blit(rotate, rect.topleft)
    Chargie.heart = pygame.Rect((Chargie.x + Chargie.size//4), (Chargie.y + Chargie.size//3), Chargie.size//2, Chargie.size//2)
    text = FONT.render("hold space for debug", False, "#FFFFFF")
    DISPLAY.blit(text, (0,0))
    text = FONT.render("game by xbeo", False, "#FFFFFF")
    DISPLAY.blit(text, (0,(WIDTH+HEIGHT)//64))
    text = FONT.render("chargie by neosrc", False, "#FFFFFF")
    DISPLAY.blit(text, (0,(WIDTH+HEIGHT)//32))
    if pygame.key.get_pressed()[pygame.K_SPACE]:
      pygame.draw.rect(DISPLAY, "#0000FF", rect, Chargie.size//64)
      pygame.draw.rect(DISPLAY, "#FF0000", Chargie.heart, Chargie.size//64)
  def handle():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] and "w" not in Chargie.queue:
      Chargie.queue.append("w")
    elif not keys_pressed[pygame.K_w] and "w" in Chargie.queue:
      Chargie.queue.remove("w")
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_north_1.png').convert_alpha(),(Chargie.size, Chargie.size))
    if keys_pressed[pygame.K_a] and "a" not in Chargie.queue:
      Chargie.queue.append("a")
    elif not keys_pressed[pygame.K_a] and "a" in Chargie.queue:
      Chargie.queue.remove("a")
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_west_1.png').convert_alpha(),(Chargie.size, Chargie.size))
    if keys_pressed[pygame.K_s] and "s" not in Chargie.queue:
      Chargie.queue.append("s")
    elif not keys_pressed[pygame.K_s] and "s" in Chargie.queue:
      Chargie.queue.remove("s")
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_south_1.png').convert_alpha(),(Chargie.size, Chargie.size))
    if keys_pressed[pygame.K_d] and "d" not in Chargie.queue:
      Chargie.queue.append("d")
    elif not keys_pressed[pygame.K_d] and "d" in Chargie.queue:
      Chargie.queue.remove("d")
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_east_1.png').convert_alpha(),(Chargie.size, Chargie.size))
    if Chargie.queue[-1] == "w":
      Chargie.y -= Chargie.speed
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_north_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 0.1
    elif Chargie.queue[-1] == "a":
      Chargie.x -= Chargie.speed
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_west_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 0.1
    elif Chargie.queue[-1] == "s":
      Chargie.y += Chargie.speed
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_south_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 0.1
    elif Chargie.queue[-1] == "d":
      Chargie.x += Chargie.speed
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_east_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 0.1
    if Chargie.count >= 5:
      Chargie.count = 1
    if Chargie.y <= 0:
      Chargie.y = 0
    if Chargie.x <= 0:
      Chargie.x = 0
    if Chargie.y >= HEIGHT - Chargie.size:
      Chargie.y = HEIGHT - Chargie.size
    if Chargie.x >= WIDTH - Chargie.size:
      Chargie.x = WIDTH - Chargie.size

async def main():
  pygame.mixer.music.load('./sfx/test.ogg')
  pygame.mixer.music.play()
  while True:
    DISPLAY.fill("#404040")
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
    Chargie.handle()
    Chargie.show()
    pygame.display.flip()
    CLOCK.tick(FPS)
    await asyncio.sleep(0)
asyncio.run(main())