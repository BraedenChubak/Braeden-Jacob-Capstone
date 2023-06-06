import pygame
import random
import time

global powerup
global firerate_shotgun
global firerate_basic
global firerate_pierce
pygame.init()

white = (255, 255, 255)
gray = (50, 50, 75)
redgray = (75, 50, 50)
yellow = (255, 255, 100)
orange = (255, 100, 50)
black = (0, 0, 0)
red = (255, 20, 50)
lightred = (255, 80, 100)
darkred = (150, 10, 30)
green = (50, 200, 25)
lightgreen = (100, 255, 100)
aqua = (50, 255, 200)
blue = (50, 50, 255)
lightblue = (100, 120, 255)

dis_width = 800
dis_height = 500

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Shift")
clock = pygame.time.Clock()
game_tick = 60
font_style = pygame.font.SysFont("sans-serif", 36)


def your_score(score):
  val = font_style.render("Score: " + str(int(round(score, 0 * 10))), True,
                          white)
  dis.blit(val, [0, 0])


def player(playerx, playery):
  pygame.draw.rect(dis, playercolor, pygame.Rect(playerx, playery, 20, 20))


def basic_projectile(projectilex, projectiley, projectilexv, projectileyv):
  pygame.draw.rect(dis, white, pygame.Rect(projectilex, projectiley, 10, 10))


def projectile_spawn(playerx, playery, projectilexv, projectileyv):
  proj_new_List = []
  spawnx = playerx + 5
  spawny = playery + 5
  proj_new_List.append(spawnx)
  proj_new_List.append(spawny)
  proj_new_List.append(projectilexv)
  proj_new_List.append(projectileyv)
  projectile_List.append(proj_new_List)
  pass


def enemy(enemyx, enemyy):
  pygame.draw.rect(dis, enemycolor, pygame.Rect(enemyx, enemyy, 20, 20))


def enemyhunt(enemyx, enemyy, playerx, playery, enemyspeed):
  global enemyvx
  global enemyvy
  if abs(enemyx - playerx) > 2:
    if enemyx > playerx:
      enemyvx = -1 * enemyspeed
    else:
      enemyvx = 1 * enemyspeed
  else:
    enemyvx = 0
  if abs(enemyy - playery) > 2:
    if enemyy > playery:
      enemyvy = -1 * enemyspeed
    else:
      enemyvy = 1 * enemyspeed
  else:
    enemyvy = 0
  enemyx += enemyvx
  enemyy += enemyvy
  enemy(enemyx, enemyy)
  pass


def enemyspawn():
  enemyspawnrate = (round(time_survived, 0) // 20)
  if enemyspawnrate >= 100:
    enemyspawnrate = 100
  spawnrate = random.randrange(1, 126 - int(enemyspawnrate))
  if spawnrate == 1:
    NewEnemy_List = []
    axisspawn = random.randrange(1, 3)
    if axisspawn == 1:
      xrand = random.randrange(1, 3)
      if xrand == 1:
        spawnx = -20
      elif xrand == 2:
        spawnx = dis_width
      enemyspeedmod = (round(time_survived, 0) // 50)
      if enemyspeedmod >= 50:
        enemyspeedmod = 50
      spawny = int(random.randrange(0, dis_height - 20))
      spawnspeed = random.randrange(70 + enemyspeedmod,
                                    125 + enemyspeedmod) / 100
      NewEnemy_List.append(spawnx)
      NewEnemy_List.append(spawny)
      NewEnemy_List.append(spawnspeed)
      enemy_List.append(NewEnemy_List)
    if axisspawn == 2:
      yrand = random.randrange(1, 3)
      if yrand == 1:
        spawny = -20
      elif yrand == 2:
        spawny = dis_height
      enemyspeedmod = (round(time_survived, 0) // 50)
      if enemyspeedmod >= 50:
        enemyspeedmod = 50
      spawnx = int(random.randrange(0, dis_width - 20))
      spawnspeed = random.randrange(50 + enemyspeedmod,
                                    125 + enemyspeedmod) / 100
      NewEnemy_List.append(spawnx)
      NewEnemy_List.append(spawny)
      NewEnemy_List.append(spawnspeed)
      enemy_List.append(NewEnemy_List)


def message(msg, color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [150, dis_height / 2 - 30])


highestscore = 0

def highscore(
    currentscore,
    color):  #highest score, would like to make a list but python fiesty today
  global highestscore
  if currentscore >= highestscore:
    highestscore = currentscore
  msg = font_style.render("Your high score is: " + str(round(highestscore)),
                          True, color)
  dis.blit(msg, [275, dis_height / 2])


def gameLoop():
  global playerx
  global playery
  playerx = int(dis_width / 2)  # center of screen
  playery = int(dis_height / 2)  # center of screen
  xvelocity = 0
  yvelocity = 0
  game_over = False
  game_close = False
  global time_survived
  time_survived = 0
  playerspeed = 3
  global enemy_List
  enemy_List = [[-20, 200, 1]]
  global projectile_List
  projectile_List = []
  player_invulnerable = False
  global projectilexv
  global projectileyv
  shottime = 0
  global weaponchoice
  weaponchoice = 1
  global firerate_shotgun
  global firerate_basic
  firerate_shotgun = 3000
  firerate_basic = 500
  powertimer = 0
  powercooldown = -30000
  onpower = 0
  global enemycolor
  enemycolor = red
  global playercolor
  playercolor = lightblue
  global backgroundcolor
  backgroundcolor = gray
  gun_switch = pygame.time.get_ticks()

  while not game_over:
    while game_close and not player_invulnerable:  # game over screen
      dis.fill(lightred)
      message("Game Over! Press C to play again or Q to quit", black)
      highscore(time_survived, black)  #attempting a highscore function
      your_score(time_survived)
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:  # quit key
            game_over = True
            game_close = False
          if event.key == pygame.K_c:  # play again key
            gameLoop()
    for event in pygame.event.get():  # keypresses
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:  # move up
          yvelocity += -1 * playerspeed
        elif event.key == pygame.K_s:  # move down
          yvelocity += 1 * playerspeed
        elif event.key == pygame.K_d:  # move right
          xvelocity += 1 * playerspeed
        elif event.key == pygame.K_a:  # move left
          xvelocity += -1 * playerspeed

        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
          if pygame.time.get_ticks() - powercooldown >= 30000:
            powertimer = pygame.time.get_ticks()
            firerate_shotgun = firerate_shotgun / 5
            firerate_basic = firerate_basic / 5
            player_invulnerable = True
            playercolor = yellow
            onpower = 1
            powercooldown = pygame.time.get_ticks()
        if event.key == pygame.K_UP:
          if weaponchoice == 1:
            if pygame.time.get_ticks() - shottime >= firerate_basic:
              projectilexv = 0
              projectileyv = -6
              projectile_spawn(playerx, playery, projectilexv, projectileyv)
              shottime = pygame.time.get_ticks()
          if weaponchoice == 2:
            if pygame.time.get_ticks() - shottime >= firerate_shotgun:
              for num in range(1, random.randrange(6, 9)):
                projectilexv = random.randrange(-15, 15) / 10
                projectileyv = random.randrange(30, 60) / -10
                projectile_spawn(playerx, playery, projectilexv, projectileyv)
              shottime = pygame.time.get_ticks()
              shottime = pygame.time.get_ticks()
        if event.key == pygame.K_RIGHT:
          if weaponchoice == 1:
            if pygame.time.get_ticks() - shottime >= firerate_basic:
              projectilexv = 6
              projectileyv = 0
              projectile_spawn(playerx, playery, projectilexv, projectileyv)
              shottime = pygame.time.get_ticks()
          if weaponchoice == 2:
            if pygame.time.get_ticks() - shottime >= firerate_shotgun:
              for num in range(1, random.randrange(6, 9)):
                projectileyv = random.randrange(-15, 15) / 10
                projectilexv = random.randrange(30, 60) / 10
                projectile_spawn(playerx, playery, projectilexv, projectileyv)
              shottime = pygame.time.get_ticks()
        if event.key == pygame.K_DOWN:
          if weaponchoice == 1:
            if pygame.time.get_ticks() - shottime >= firerate_basic:
              projectilexv = 0
              projectileyv = 6
              projectile_spawn(playerx, playery, projectilexv, projectileyv)
              shottime = pygame.time.get_ticks()
          if weaponchoice == 2:
            if pygame.time.get_ticks() - shottime >= firerate_shotgun:
              for num in range(1, random.randrange(6, 9)):
                projectilexv = random.randrange(-15, 15) / 10
                projectileyv = random.randrange(30, 60) / 10
                projectile_spawn(playerx, playery, projectilexv, projectileyv)
              shottime = pygame.time.get_ticks()
        if event.key == pygame.K_LEFT:
          if weaponchoice == 1:
            if pygame.time.get_ticks() - shottime >= firerate_basic:
              projectilexv = -6
              projectileyv = 0
              projectile_spawn(playerx, playery, projectilexv, projectileyv)
              shottime = pygame.time.get_ticks()
          if weaponchoice == 2:
            if pygame.time.get_ticks() - shottime >= firerate_shotgun:
              projectileyv = -1
              for num in range(1, random.randrange(6, 9)):
                projectileyv = random.randrange(-15, 15) / 10
                projectilexv = random.randrange(30, 60) / -10
                projectile_spawn(playerx, playery, projectilexv, projectileyv)
              shottime = pygame.time.get_ticks()
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_w and yvelocity <= 0:  # move up
          yvelocity -= -1 * playerspeed
        elif event.key == pygame.K_s and yvelocity >= 0:  # move down
          yvelocity -= 1 * playerspeed
        elif event.key == pygame.K_d and xvelocity >= 0:  # move right
          xvelocity -= 1 * playerspeed
        elif event.key == pygame.K_a and xvelocity <= 0:  # move left
          xvelocity -= -1 * playerspeed

    playerx += xvelocity
    playery += yvelocity
    if playerx <= 0:
      playerx = 0
    elif playerx >= dis_width - 20:  # 20 is player width
      playerx = dis_width - 20
    if playery <= 0:
      playery = 0
    elif playery >= dis_height - 20:  # 20 is player height
      playery = playery = dis_height - 20
    dis.fill(backgroundcolor)
    player(playerx, playery)
    if onpower == 1:
      if pygame.time.get_ticks() - powertimer >= 3000:
        firerate_shotgun = firerate_shotgun * 5
        firerate_basic = firerate_basic * 5
        player_invulnerable = False
        if weaponchoice == 1:
          playercolor = lightblue
        else:
          playercolor = lightgreen
        powercooldown = pygame.time.get_ticks()
        onpower = 0
    enemyspawn()
    time_survived += 0.1
    your_score(time_survived)
    if pygame.time.get_ticks() - gun_switch >= 10000:
      if weaponchoice == 1:
        weaponchoice = 2
        enemycolor = orange
        if onpower == 1:
          playercolor = yellow
        else:
          playercolor = lightgreen
        backgroundcolor = redgray
      elif weaponchoice == 2:
        weaponchoice = 1
        enemycolor = red
        if onpower == 1:
          playercolor = yellow
        else:
          playercolor = lightblue
        backgroundcolor = gray
      gun_switch = pygame.time.get_ticks()
      shottime = 0
    if player_invulnerable == True:
      game_close = False
    for y in projectile_List:
      basic_projectile(y[0], y[1], y[2], y[3])
      y[0] += y[2]
      y[1] += y[3]
      if y[0] <= -15 or y[0] >= dis_width:
        projectile_List.remove(y)
        break
      if y[1] <= -15 or y[1] >= dis_height:
        projectile_List.remove(y)
        break
      for z in enemy_List:
        if abs(y[0] - z[0]) <= 15 and abs(y[1] - z[1]) <= 15:
          projectile_List.remove(y)
          enemy_List.remove(z)
          time_survived += 5
          break
    for x in enemy_List:
      enemyhunt(x[0], x[1], playerx, playery, x[2])
      x[0] += enemyvx
      x[1] += enemyvy
      if abs(x[0] - playerx) <= 20 and abs(x[1] - playery) <= 20:
        game_close = True
    pygame.display.update()
    clock.tick(game_tick)
  pygame.quit()
  quit()


gameLoop()
