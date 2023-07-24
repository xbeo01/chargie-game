import asyncio
import random
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.font.init()
FPS = 60
CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 704, 704
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("Comic Sans MS", (WIDTH+HEIGHT)//88)

class Chargie():
  size = (WIDTH + HEIGHT) // 11
  x = (WIDTH // 2) - (size // 2)
  y = (HEIGHT // 2) - (size // 2)
  image = pygame.transform.scale(pygame.image.load('./img/cg_south_1.png').convert_alpha(),(size, size))
  speed = size // 16
  angle = 0
  count = 1
  queue = [""]
  heart = pygame.Rect((x + size//4), (y + size//3), size//2, size//2)
  hp = 100
  score = 0
  dash = True
  def show():
    rect = pygame.Rect(0, 0, WIDTH, Chargie.size//2)
    pygame.draw.rect(DISPLAY, "#202020", rect)
    rect = pygame.Rect(WIDTH//2, Chargie.size//8, WIDTH//2, Chargie.size//4)
    pygame.draw.rect(DISPLAY, "#00FF00", rect)
    rect = pygame.Rect(max(WIDTH//2, WIDTH//2+(WIDTH//2*Chargie.hp//100)), Chargie.size//8, WIDTH//2, Chargie.size//4)
    pygame.draw.rect(DISPLAY, "#FF0000", rect)
    rotate = pygame.transform.rotate(Chargie.image, Chargie.angle)
    rect = rotate.get_rect(center=Chargie.image.get_rect(topleft=(Chargie.x, Chargie.y)).center)
    DISPLAY.blit(rotate, rect.topleft)
    Chargie.heart = pygame.Rect((Chargie.x + Chargie.size//4), (Chargie.y + Chargie.size//3), Chargie.size//2, Chargie.size//2)
    text = FONT.render("hold e for debug", False, "#FFFFFF")
    DISPLAY.blit(text, (0,0))
    text = FONT.render("press space to dash, r to restart", False, "#FFFFFF")
    DISPLAY.blit(text, (0,(WIDTH+HEIGHT)//88))
    text = FONT.render("game by xbeo, chargie by neosrc", False, "#FFFFFF")
    DISPLAY.blit(text, (0,(WIDTH+HEIGHT)//44))
    text = FONT.render("score: "+str(int(Chargie.score)), False, "#FFFFFF")
    DISPLAY.blit(text, (0,(WIDTH+HEIGHT)//29))
    if pygame.key.get_pressed()[pygame.K_e]:
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
      if keys_pressed[pygame.K_SPACE] and Chargie.dash:
        Chargie.y -= Chargie.size
        Chargie.dash = False
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_north_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 5/FPS
    elif Chargie.queue[-1] == "a":
      Chargie.x -= Chargie.speed
      if keys_pressed[pygame.K_SPACE] and Chargie.dash:
        Chargie.x -= Chargie.size
        Chargie.dash = False
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_west_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 5/FPS
    elif Chargie.queue[-1] == "s":
      Chargie.y += Chargie.speed
      if keys_pressed[pygame.K_SPACE] and Chargie.dash:
        Chargie.y += Chargie.size
        Chargie.dash = False
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_south_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 5/FPS
    elif Chargie.queue[-1] == "d":
      Chargie.x += Chargie.speed
      if keys_pressed[pygame.K_SPACE] and Chargie.dash:
        Chargie.x += Chargie.size
        Chargie.dash = False
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_east_'+str(int(Chargie.count))+'.png').convert_alpha(),(Chargie.size, Chargie.size))
      Chargie.count += 5/FPS
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

class GameModes():
  rects1 = []
  rects2 = []
  rects3 = []
  rects4 = []
  queue = 0
  def BulletHell():
    global toggle1, toggle2, toggle3, toggle4
    if pygame.key.get_pressed()[pygame.K_r]:
      Chargie.score = 0
      Chargie.hp = 100
      GameModes.rects1 = []
      GameModes.rects2 = []
      GameModes.rects3 = []
      GameModes.rects4 = []
      pygame.mixer.music.stop()
      pygame.mixer.music.play()
      Chargie.dash = True
      Chargie.x = (WIDTH // 2) - (Chargie.size // 2)
      Chargie.y = (HEIGHT // 2) - (Chargie.size // 2)
      Chargie.image = pygame.transform.scale(pygame.image.load('./img/cg_south_1.png').convert_alpha(),(Chargie.size, Chargie.size))
    if Chargie.hp > 0:
      Chargie.score += 5/FPS
    else:
      pygame.mixer.music.stop()
      GameModes.rects1 = []
      GameModes.rects2 = []
      GameModes.rects3 = []
      GameModes.rects4 = []
    if GameModes.queue > 0:
      Chargie.hp -= 1
      GameModes.queue -= 1
    if int(Chargie.score) % 21 == 5 and toggle1:
      toggle1 = False
      Chargie.dash = True
      for i in range(8):
        if random.randint(0,1) == 1:
          rect = pygame.Rect((i*WIDTH//8+Chargie.size//8), 0, Chargie.size//4, Chargie.size//4)
          GameModes.rects1.append(rect)
    elif int(Chargie.score) % 21 != 5:
      toggle1 = True
    if int(Chargie.score) % 21 == 10 and toggle2:
      toggle2 = False
      Chargie.dash = True
      for i in range(8):
        if random.randint(0,1) == 1:
          rect = pygame.Rect(0, (i*HEIGHT//8+Chargie.size//8), Chargie.size//4, Chargie.size//4)
          GameModes.rects2.append(rect)
    elif int(Chargie.score) % 21 != 10:
      toggle2 = True
    if int(Chargie.score) % 21 == 15 and toggle3:
      toggle3 = False
      Chargie.dash = True
      for i in range(8):
        if random.randint(0,1) == 1:
          rect = pygame.Rect((i*WIDTH//8+Chargie.size//8), HEIGHT, Chargie.size//4, Chargie.size//4)
          GameModes.rects3.append(rect)
    elif int(Chargie.score) % 21 != 15:
      toggle3 = True
    if int(Chargie.score) % 21 == 20 and toggle4:
      toggle4 = False
      Chargie.dash = True
      for i in range(8):
        if random.randint(0,1) == 1:
          rect = pygame.Rect(WIDTH, (i*HEIGHT//8+Chargie.size//8), Chargie.size//4, Chargie.size//4)
          GameModes.rects4.append(rect)
    elif int(Chargie.score) % 21 != 20:
      toggle4 = True
    for rect in GameModes.rects1:
      pygame.draw.rect(DISPLAY, "#FFFF00", rect)
      rect.y += Chargie.speed
      if pygame.Rect.colliderect(rect, Chargie.heart):
        GameModes.queue += 10
        GameModes.rects1.remove(rect)
    for rect in GameModes.rects2:
      pygame.draw.rect(DISPLAY, "#FFFF00", rect)
      rect.x += Chargie.speed
      if pygame.Rect.colliderect(rect, Chargie.heart):
        GameModes.queue += 10
        GameModes.rects2.remove(rect)
    for rect in GameModes.rects3:
      pygame.draw.rect(DISPLAY, "#FFFF00", rect)
      rect.y -= Chargie.speed
      if pygame.Rect.colliderect(rect, Chargie.heart):
        GameModes.queue += 10
        GameModes.rects3.remove(rect)
    for rect in GameModes.rects4:
      pygame.draw.rect(DISPLAY, "#FFFF00", rect)
      rect.x -= Chargie.speed
      if pygame.Rect.colliderect(rect, Chargie.heart):
        GameModes.queue += 10
        GameModes.rects4.remove(rect)

async def main():
  pygame.mixer.music.load('./sfx/test.ogg')
  pygame.mixer.music.play()
  while True:
    DISPLAY.fill("#404040")
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
    GameModes.BulletHell()
    Chargie.handle()
    Chargie.show()
    pygame.display.flip()
    CLOCK.tick(FPS)
    await asyncio.sleep(0)
asyncio.run(main())