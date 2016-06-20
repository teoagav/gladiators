import pygame, sys, time, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

screenWidth = 800
screenHeight = 600
windowSurface = pygame.display.set_mode((screenWidth, screenHeight), 0, 0)
pygame.display.set_caption('Gladiators')

background = pygame.image.load('tiledbackground.png')
backgroundRect = background.get_rect()
font = pygame.font.SysFont("TimesNewRoman", 15)

paused = pygame.font.SysFont("Arial", 18)
instructions = pygame.font.SysFont("Arial", 15)

pauseScreen = pygame.Surface((1000,750), pygame.SRCALPHA)   
pauseScreen.fill((0,0,0,120))

def setup():    
    global p1DamageImmune
    global p2DamageImmune
    global p1DamageTime
    global p2DamageTime
    global player1
    global p1Image
    global p1ShieldImage
    global p1SpearImage
    global p1Shield
    global p1Spear
    global p1UseShield
    global p1SpearThrust
    global p1MoveSpeed
    global p1Health
    global p1Alive
    global p1MoveLeft 
    global p1MoveRight 
    global p1MoveUp 
    global p1MoveDown
    global p1FaceDown
    global p1FaceUp
    global p1FaceLeft 
    global p1FaceRight 
    global player2
    global p2Image 
    global p2ShieldImage 
    global p2SpearImage 
    global p2Shield
    global p2Spear 
    global p2UseShield  
    global p2SpearThrust
    global p2MoveSpeed
    global p2Health 
    global p2Alive 
    global p2MoveLeft 
    global p2MoveRight 
    global p2MoveUp 
    global p2MoveDown 
    global p2FaceDown 
    global p2FaceUp 
    global p2FaceLeft 
    global p2FaceRight 
    global isPaused
    global hurtNoise
    global healthLst
    global healthSize
    global newHealth
    global healthCounter
    global healthImage
    global powerUpNoise
    global speedLst
    global speedSize
    global newSpeed
    global speedCounter
    global speedImage
    global p1SpeedTime
    global p2SpeedTime
    global p1SpeedUp
    global p2SpeedUp
    global musicPlaying

    p1DamageImmune = False
    p2DamageImmune = False
    p1DamageTime = 0
    p2DamageTime = 0
    p1SpeedTime = 0
    p2SpeedTime = 0
    p1SpeedUp = False
    p2SpeedUp = False
    isPaused = False

    player1 = pygame.Rect(125, 150, 40, 65)
    p1Image = pygame.image.load('gladiator-right.png')
    p1ShieldImage = pygame.image.load('shield-right.png')
    p1SpearImage = pygame.image.load('spear-right.png')

    p1Shield = pygame.Rect(player1.left + 31, player1.top + 10, 26, 38)
    p1Spear = pygame.Rect(player1.left, player1.top + 33, 60, 15)
    p1UseShield = False
    p1SpearThrust = 0

    p1MoveSpeed = 4
    p1Health = 10
    p1Alive = True

    p1MoveLeft = False
    p1MoveRight = False
    p1MoveUp = False
    p1MoveDown = False

    p1FaceDown = False
    p1FaceUp = False
    p1FaceLeft = False
    p1FaceRight = True

    player2 = pygame.Rect(600, 150, 40, 65)
    p2Image = pygame.image.load('gladiator2-left.png')
    p2ShieldImage = pygame.image.load('shield-left.png')
    p2SpearImage = pygame.image.load('spear-left.png')

    p2Shield = pygame.Rect(player2.left - 20, player2.top + 15, 26, 38)
    p2Spear = pygame.Rect(player2.left - 20, player2.top + 33, 60, 15)
    p2UseShield = False 
    p2SpearThrust = 0

    p2MoveSpeed = 4
    p2Health = 10
    p2Alive = True

    p2MoveLeft = False
    p2MoveRight = False
    p2MoveUp = False
    p2MoveDown = False

    p2FaceDown = False
    p2FaceUp = False
    p2FaceLeft = True
    p2FaceRight = False
    
    musicPlaying = True
    
    healthImage = pygame.image.load('health.png')
    healthCounter = 0
    newHealth = 500
    healthSize = 20
    healthLst = []
    
    speedImage = pygame.image.load('speed.png')
    speedCounter = 0
    newSpeed = 300
    speedSize = 20
    speedLst = []
    
    hurtNoise = pygame.mixer.Sound('hurt.wav')
    powerUpNoise = pygame.mixer.Sound('drink.wav')

def damageFlash(player):   
    if player == player1 and p1Alive == True:
        if p1FaceDown: 
            p1Image = pygame.image.load('gladiatorDamage-down.png')
        if p1FaceUp:
            p1Image = pygame.image.load('gladiatorDamage-up.png')
        if p1FaceLeft:
            p1Image = pygame.image.load('gladiatorDamage-left.png')
        if p1FaceRight:
            p1Image = pygame.image.load('gladiatorDamage-right.png')
        windowSurface.blit(p1Image, player1)
    if player == player2 and p2Alive == True:
        if p2FaceDown: 
            p2Image = pygame.image.load('gladiatorDamage-down.png')
        if p2FaceUp:
            p2Image = pygame.image.load('gladiatorDamage-up.png')
        if p2FaceLeft:
            p2Image = pygame.image.load('gladiatorDamage-left.png')
        if p2FaceRight:
            p2Image = pygame.image.load('gladiatorDamage-right.png')
        windowSurface.blit(p2Image, player2)
    
def updateScore():
    global p1Alive
    global p2Alive
    
    if p1Health > 0:
        p1HealthScreen = font.render("Player 1 Health: "+ str(p1Health), 1, (255,255,0))
        windowSurface.blit(p1HealthScreen, (100, 50))
        
    elif p1Health <= 0:
        p1Alive = False
        p1DeathScreen = font.render("Player 1 has died!", 1, (255,255,0))
        windowSurface.blit(background, backgroundRect)
        windowSurface.blit(p1DeathScreen, (100, 50)) 
        playAgain()
            
    if p2Health > 0:
        if p1Alive == False:
            p2VictoryScreen = font.render("Player 2 is victorious!", 1, (255,0,0))
            windowSurface.blit(p2VictoryScreen, (550, 50))
        else:
            p2HealthScreen = font.render("Player 2 Health: "+ str(p2Health), 1, (255,0,0))
            windowSurface.blit(p2HealthScreen, (550, 50))
            
    elif p2Health <= 0:
        p2Alive = False
        p2DeathScreen = font.render("Player 2 has died!", 1, (255,0,0))
        p1VictoryScreen = font.render("Player 1 is victorious!", 1, (255,255,0))
        windowSurface.blit(background, backgroundRect)
        windowSurface.blit(p2DeathScreen, (550, 50))
        windowSurface.blit(p1VictoryScreen, (100, 50))
        playAgain()
        
    pauseInstruction = font.render("Escape to pause and view controls, m to enable/disable sounds", 1, (255,255,255))
    windowSurface.blit(pauseInstruction, (5,5))
    scoreScreen = font.render(str(p1Score) + " - " + str(p2Score), 1, (255,255,255))
    windowSurface.blit(scoreScreen, (390, 50))
    pygame.display.update()

def playAgain():
    global p1Score
    global p2Score
    displayPlayAgain = paused.render("Do you want to play again. Yes (y) or No (n)", 1 ,(255,255,255))
    windowSurface.blit(displayPlayAgain, (275, 250))
    if event.type == KEYDOWN:
        if event.key == ord('y'):
            if p1Health <= 0:
                p2Score += 1
            if p2Health <= 0:
                p1Score += 1
            setup()
        if event.key == ord('n'):
            pygame.quit()
            sys.exit()
            
def documentation():
    global pauseScreen
    global p1Score
    global p2Score
    windowSurface.blit(pauseScreen, (0,0))
    pauseText = paused.render("Game is paused!", 1, (255,255,255))
    pygame.draw.rect(windowSurface, (0,0,0), [340, 95, 140, 35], 0)
    windowSurface.blit(pauseText, (354, 102))    
    
    line1 = "Player 1's movement is controlled with the WASD keys. To shield, hold down Q, and to stab, press E."
    line2 = "Player 2's movement is controlled with the IJKL keys. To shield, hold down the spacebar, and to stab, press O."
    line3 = "Each gladiator is equipped with a shield and a spear. While active, the shield blocks any incoming spears about to strike it, but" 
    line4 = "lowers the player's movement speed. Spears are normally held in the gladiators' hands, but they can also be extended to improve"
    line5 = "their range. If a spear encounters a gladiator, they lose 1 health point."
    line6 = "Players may also collect powerups that spawn occasionally on the map. Red potions increase a player's health by 1,"
    line7 = "and blue potions increase a player's movement speed for 5 seconds."
    line8 = "The objective of the game is to defeat your opponent by bringing his health to 0."
    
    windowSurface.blit(instructions.render(line1, 1, (255,255,255)), (30, 200))
    windowSurface.blit(instructions.render(line2, 1, (255,255,255)), (30, 225))
    windowSurface.blit(instructions.render(line3, 1, (255,255,255)), (30, 300))
    windowSurface.blit(instructions.render(line4, 1, (255,255,255)), (30, 325))
    windowSurface.blit(instructions.render(line5, 1, (255,255,255)), (30, 350))
    windowSurface.blit(instructions.render(line6, 1, (255,255,255)), (30, 400))
    windowSurface.blit(instructions.render(line7, 1, (255,255,255)), (30, 425))
    windowSurface.blit(instructions.render(line8, 1, (255,255,255)), (30, 500))
    
    pygame.display.flip()
                
setup()
p1Score = 0
p2Score = 0
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1, 0.0)

while True:
    
    if pygame.time.get_ticks() - p1DamageTime > 1000:
        p1DamageImmune = False
        
    if pygame.time.get_ticks() - p2DamageTime > 1000:
        p2DamageImmune = False

    if pygame.time.get_ticks() - p1SpeedTime > 5000:
        p1SpeedUp = False
        
    if pygame.time.get_ticks() - p2SpeedTime > 5000:
        p2SpeedUp = False

    if p1SpeedUp:
        if p1UseShield == True:
            p1MoveSpeed = 0
        else:
            p1MoveSpeed = 6
    else:
        if p1UseShield == True:
            p1MoveSpeed = 0
        else:
            p1MoveSpeed = 4
        
    if p2SpeedUp:
        if p2UseShield == True:
            p2MoveSpeed = 0
        else:
            p2MoveSpeed = 6
    else:
        if p2UseShield == True:
            p2MoveSpeed = 0
        else:
            p2MoveSpeed = 4

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isPaused = not isPaused
                if isPaused:
                    documentation()
          
            if not isPaused:
                if p1Alive:
                    if event.key == ord('a'):
                        p1MoveRight = False
                        p1MoveUp = False
                        p1MoveDown = False
                        p1MoveLeft = True
                        p1Image = pygame.image.load('gladiator-left.png')
                        p1SpearImage = pygame.image.load('spear-left.png')
                    if event.key == ord('d'):
                        p1MoveUp = False
                        p1MoveLeft = False
                        p1MoveDown = False
                        p1MoveRight = True
                        p1Image = pygame.image.load('gladiator-right.png')
                        p1SpearImage = pygame.image.load('spear-right.png')
                    if event.key == ord('w'):
                        p1MoveDown = False
                        p1MoveRight = False
                        p1MoveLeft = False
                        p1MoveUp = True
                        p1Image = pygame.image.load('gladiator-up.png')
                        p1SpearImage = pygame.image.load('spear-up.png')
                    if event.key == ord('s'):
                        p1MoveUp = False
                        p1MoveRight = False
                        p1MoveLeft = False
                        p1MoveDown = True
                        p1Image = pygame.image.load('gladiator-down.png')
                        p1SpearImage = pygame.image.load('spear-down.png')
                    if event.key == K_LSHIFT:
                        p1UseShield = True
                    if event.key == ord('e'):
                        p1SpearThrust += 1
                                    
                if p2Alive:
                    if event.key == ord('j'):
                        p2MoveRight = False
                        p2MoveLeft = True
                        p2MoveUp = False
                        p2MoveDown = False
                        p2SpearImage = pygame.image.load('spear-left.png')
                        p2Image = pygame.image.load('gladiator2-left.png')
                    if event.key == ord('l'):
                        p2MoveUp = False
                        p2MoveLeft = False
                        p2MoveRight = True
                        p2MoveDown = False
                        p2SpearImage = pygame.image.load('spear-right.png')
                        p2Image = pygame.image.load('gladiator2-right.png')
                    if event.key == ord('i'):
                        p2MoveDown = False
                        p2MoveUp = True
                        p2MoveRight = False
                        p2MoveLeft = False
                        p2SpearImage = pygame.image.load('spear-up.png')
                        p2Image = pygame.image.load('gladiator2-up.png')
                    if event.key == ord('k'):
                        p2MoveUp = False
                        p2MoveDown = True
                        p2MoveRight = False
                        p2MoveLeft = False
                        p2SpearImage = pygame.image.load('spear-down.png')
                        p2Image = pygame.image.load('gladiator2-down.png')
                    if event.key == K_SPACE:
                        p2UseShield = True
                    if event.key == ord('o'):
                        p2SpearThrust += 1
              
        if event.type == KEYUP:
            
            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
                
            if not isPaused:
                if p1Alive:
                    if event.key == ord('a'):
                        p1MoveLeft = False
                    if event.key == ord('d'):
                        p1MoveRight = False
                    if event.key == ord('w'):
                        p1MoveUp = False
                    if event.key == ord('s'):
                        p1MoveDown = False
                    if event.key == K_LSHIFT:
                        p1UseShield = False
                    if event.key == ord('e'):
                        p1UseSpear = False
                
                if p2Alive:
                    if event.key == ord('j'):
                        p2MoveLeft = False
                    if event.key == ord('l'):
                        p2MoveRight = False
                    if event.key == ord('i'):
                        p2MoveUp = False
                    if event.key == ord('k'):
                        p2MoveDown = False
                    if event.key == K_SPACE:
                        p2UseShield = False
    
    if not isPaused:
        windowSurface.blit(background, backgroundRect)
   
        if p1Alive:
            windowSurface.blit(p1Image, player1)
            
            if p1SpearThrust % 10 != 0:
                p1SpearThrust += 1
                if p1FaceDown:
                    p1Spear.bottom += 5
                elif p1FaceUp:
                    p1Spear.top -= 5
                elif p1FaceLeft:
                    p1Spear.left -= 5
                elif p1FaceRight:
                    p1Spear.right += 5
                if p1Spear.colliderect(p2Shield) and p2UseShield:
                    p1SpearThrust = 0
                if p1Spear.colliderect(player2) and p2DamageImmune == False:
                    p2Health -= 1
                    if musicPlaying:
                        hurtNoise.play()
                    p2DamageImmune = True
                    damageFlash(player2)
                    if p1FaceDown:
                        player2.top = p1Spear.bottom + 30
                    elif p1FaceUp:
                        player2.bottom = p1Spear.top - 30
                    elif p1FaceLeft:
                        player2.right = p1Spear.left - 30
                    elif p1FaceRight:
                        player2.left = p1Spear.right + 30
                    if p2FaceDown:
                        p2Shield = pygame.Rect(player2.left + 14, player2.top + 33, 26, 38)
                        p2Spear = pygame.Rect(player2.left - 5, player2.top + 25, 15, 60)
                    elif p2FaceUp:
                        p2Shield = pygame.Rect(player2.left + 1, player2.top - 10, 26, 38)
                        p2Spear = pygame.Rect(player2.left + 25, player2.top - 15, 15, 60)
                    elif p2FaceLeft:
                        p2Shield = pygame.Rect(player2.left - 20, player2.top + 15, 26, 38)
                        p2Spear = pygame.Rect(player2.left - 20, player2.top + 33, 60, 15)
                    elif p2FaceRight:
                        p2Shield = pygame.Rect(player2.left + 32, player2.top + 15, 26, 38)
                        p2Spear = pygame.Rect(player2.left, player2.top + 33, 60, 15)
                        
                    p2DamageTime = pygame.time.get_ticks()     
        
            else:
                p1SpearThrust = 0
                if p1FaceDown:
                    p1Spear = pygame.Rect(player1.left - 5, player1.top + 25, 15, 60)
                elif p1FaceUp:
                    p1Spear = pygame.Rect(player1.left + 25, player1.top - 15, 15, 60)
                elif p1FaceLeft:
                    p1Spear = pygame.Rect(player1.left - 20, player1.top + 33, 60, 15)
                elif p1FaceRight:
                    p1Spear = pygame.Rect(player1.left, player1.top + 33, 60, 15)

            if p1MoveDown:
                p1FaceDown = True
                p1FaceUp = False
                p1FaceLeft = False
                p1FaceRight = False
                p1Shield = pygame.Rect(player1.left + 14, player1.top + 38, 26, 38)
                p1Spear = pygame.Rect(player1.left - 5, player1.top + 25, 15, 60)
                if p1Spear.bottom > player2.top and p1Spear.colliderect(player2): 
                    if p2DamageImmune == False:
                        p2Health -= 1
                        if musicPlaying:
                            hurtNoise.play()
                        p2DamageImmune = True
                        p2DamageTime = pygame.time.get_ticks()
    
                        damageFlash(player2)
                        
                        player2.top += 30
                        p2Spear.top += 30
                        p2Shield.top += 30
                        
                    else:
                        pass
                    
                elif p1Spear.colliderect(p2Shield) and p2UseShield == True or player1.bottom > screenHeight:
                    pass
                
                else:
                    player1.bottom += p1MoveSpeed
                    
            if p1MoveUp:
                p1FaceDown = False
                p1FaceUp = True
                p1FaceLeft = False
                p1FaceRight = False
                p1Shield = pygame.Rect(player1.left + 1, player1.top - 10, 26, 38)
                p1Spear = pygame.Rect(player1.left + 25, player1.top - 15, 15, 60)
                if p1Spear.top < player2.bottom and p1Spear.colliderect(player2):
                    if p2DamageImmune == False:
                        p2Health -= 1
                        if musicPlaying:
                            hurtNoise.play()
                        p2DamageImmune = True
                        p2DamageTime = pygame.time.get_ticks()
    
                        damageFlash(player2)
                        
                        player2.bottom -= 30
                        p2Spear.bottom -= 30
                        p2Shield.bottom -= 30
    
                    else:
                        pass
                    
                elif p1Spear.colliderect(p2Shield) and p2UseShield == True or player1.top < 0:
                    pass
                
                else:
                    player1.top -= p1MoveSpeed 
            
            if p1MoveLeft:
                p1FaceDown = False
                p1FaceUp = False
                p1FaceLeft = True
                p1FaceRight = False
                p1Shield = pygame.Rect(player1.left - 20, player1.top + 15, 26, 38)
                p1Spear = pygame.Rect(player1.left - 20, player1.top + 33, 60, 15)
                if p1Spear.left < player2.right and p1Spear.colliderect(player2):
                    if p2DamageImmune == False:
                        p2Health -= 1
                        if musicPlaying:
                            hurtNoise.play()
                        p2DamageImmune = True
                        p2DamageTime = pygame.time.get_ticks()
    
                        damageFlash(player2)
                        
                        player2.right -= 30
                        p2Spear.right -= 30
                        p2Shield.right -= 30
        
                    else:
                        pass
                    
                elif p1Spear.colliderect(p2Shield) and p2UseShield == True or player1.left < 0:
                    pass
                
                else:
                    player1.left -= p1MoveSpeed
                    
            if p1MoveRight:
                p1FaceDown = False
                p1FaceUp = False
                p1FaceLeft = False
                p1FaceRight = True
                p1Shield = pygame.Rect(player1.left + 32, player1.top + 15, 26, 38)
                p1Spear = pygame.Rect(player1.left, player1.top + 33, 60, 15)
                if p1Spear.right > player2.left and p1Spear.colliderect(player2):
                    if p2DamageImmune == False:
                        p2Health -= 1
                        if musicPlaying:
                            hurtNoise.play()
                        p2DamageImmune = True
                        p2DamageTime = pygame.time.get_ticks()
    
                        damageFlash(player2)
                        
                        player2.left += 30
                        p2Spear.left += 30
                        p2Shield.left += 30
                        
                    else:
                        pass
                    
                elif p1Spear.colliderect(p2Shield) and p2UseShield == True or player1.right > screenWidth:
                    pass
                
                else:
                    player1.right += p1MoveSpeed
                            
            if p1UseShield == True:
                if p1FaceDown == True:
                    p1ShieldImage = pygame.image.load('shield-down.png')
                    windowSurface.blit(p1ShieldImage, p1Shield)
                elif p1FaceUp == True:
                    p1ShieldImage = pygame.image.load('shield-up.png')
                    windowSurface.blit(p1ShieldImage, p1Shield)
                    windowSurface.blit(p1Image, player1)
                elif p1FaceLeft == True:
                    p1ShieldImage = pygame.image.load('shield-left.png')
                    windowSurface.blit(p1ShieldImage, p1Shield)
                elif p1FaceRight == True:
                    p1ShieldImage = pygame.image.load('shield-right.png')
                    windowSurface.blit(p1ShieldImage, p1Shield)
                    
        if p2Alive: 
            windowSurface.blit(p2Image, player2)
            
            if p2SpearThrust % 10 != 0:
                p2SpearThrust += 1
                if p2FaceDown:
                    p2Spear.bottom += 5
                elif p2FaceUp:
                    p2Spear.top -= 5
                elif p2FaceLeft:
                    p2Spear.left -= 5
                elif p2FaceRight:
                    p2Spear.right += 5
                if p2Spear.colliderect(p1Shield) and p1UseShield:
                    p2SpearThrust = 0
                if p2Spear.colliderect(player1) and p1DamageImmune == False:
                    p1Health -= 1
                    if musicPlaying:
                        hurtNoise.play()
                    p1DamageImmune = True
                    damageFlash(player1)
                    if p2FaceDown:
                        player1.top = p2Spear.bottom + 30
                    if p2FaceUp:
                        player1.bottom = p2Spear.top - 30
                    if p2FaceLeft:
                        player1.right = p2Spear.left - 30
                    if p2FaceRight:
                        player1.left = p2Spear.right + 30
                    if p1FaceDown:
                        p1Shield = pygame.Rect(player1.left + 14, player1.top + 33, 26, 38)
                        p1Spear = pygame.Rect(player1.left - 5, player1.top + 25, 15, 60)
                    elif p1FaceUp:
                        p1Shield = pygame.Rect(player1.left + 1, player1.top - 10, 26, 38)
                        p1Spear = pygame.Rect(player1.left + 25, player1.top - 15, 15, 60)
                    elif p1FaceLeft:
                        p1Shield = pygame.Rect(player1.left - 20, player1.top + 15, 26, 38)
                        p1Spear = pygame.Rect(player1.left - 20, player1.top + 33, 60, 15)
                    elif p1FaceRight:
                        p1Shield = pygame.Rect(player1.left + 32, player1.top + 15, 26, 38)
                        p1Spear = pygame.Rect(player1.left, player1.top + 33, 60, 15)
                    p1DamageTime = pygame.time.get_ticks()     
                    
            else:
                p2SpearThrust = 0
                if p2FaceDown:
                    p2Spear = pygame.Rect(player2.left - 5, player2.top + 25, 15, 60)
                elif p2FaceUp:
                    p2Spear = pygame.Rect(player2.left + 25, player2.top - 15, 15, 60)
                elif p2FaceLeft:
                    p2Spear = pygame.Rect(player2.left - 20, player2.top + 33, 60, 15)
                elif p2FaceRight:
                    p2Spear = pygame.Rect(player2.left, player2.top + 33, 60, 15)
                                    
            if p2MoveDown:
                p2FaceDown = True
                p2FaceUp = False
                p2FaceLeft = False
                p2FaceRight = False
                p2Shield = pygame.Rect(player2.left + 14, player2.top + 38, 26, 38)
                p2Spear = pygame.Rect(player2.left - 5, player2.top + 25, 15, 60)
                if p2Spear.bottom > player1.top and p2Spear.colliderect(player1):
                    if p1DamageImmune == False:
                        p1Health -= 1
                        if musicPlaying:
                            hurtNoise.play()
                        p1DamageImmune = True
                        p1DamageTime = pygame.time.get_ticks()
    
                        damageFlash(player1)
                        
                        player1.top += 30
                        p1Spear.top += 30
                        p1Shield.top += 30
                        
                    else:
                        pass
                        
                elif p2Spear.colliderect(p1Shield) and p1UseShield == True or player2.bottom > screenHeight:
                    pass
    
                else:
                    player2.bottom += p2MoveSpeed
                    
            if p2MoveUp:
                p2FaceDown = False
                p2FaceUp = True
                p2FaceLeft = False
                p2FaceRight = False
                p2Shield = pygame.Rect(player2.left + 1, player2.top - 10, 26, 38)
                p2Spear = pygame.Rect(player2.left + 25, player2.top - 15, 15, 60)
                if p2Spear.top < player1.bottom and p2Spear.colliderect(player1):
                    if p1DamageImmune == False:
                        p1Health -= 1
                        if musicPlaying:
                            hurtNoise.play()
                        p1DamageImmune = True
                        p1DamageTime = pygame.time.get_ticks()

                        damageFlash(player1)
                        
                        player1.bottom -= 30
                        p1Spear.bottom -= 30
                        p1Shield.bottom -= 30
    
                    else:
                        pass
    
                elif p2Spear.colliderect(p1Shield) and p1UseShield == True or player2.top < 0:
                    pass
                
                else:
                    player2.top -= p2MoveSpeed
                    
            if p2MoveLeft:
                p2FaceDown = False
                p2FaceUp = False
                p2FaceLeft = True
                p2FaceRight = False
                p2Shield = pygame.Rect(player2.left - 20, player2.top + 15, 26, 38)
                p2Spear = pygame.Rect(player2.left - 20, player2.top + 33, 60, 15)
                if p2Spear.left < player1.right and p2Spear.colliderect(player1):
                    if p1DamageImmune == False:
                        p1Health -= 1
                        if musicPlaying:
                            hurtNoise.play()
                        p1DamageImmune = True
                        p1DamageTime = pygame.time.get_ticks()
    
                        damageFlash(player1)
                        
                        player1.right -= 30
                        p1Spear.right -= 30
                        p1Shield.right -= 30
                        
                    else:
                        pass
                    
                elif p2Spear.colliderect(p1Shield) and p1UseShield == True or player2.left < 0:
                    pass
                
                else:
                    player2.left -= p2MoveSpeed
                    
            if p2MoveRight:
                p2FaceDown = False
                p2FaceUp = False
                p2FaceLeft = False
                p2FaceRight = True
                p2Shield = pygame.Rect(player2.left + 32, player2.top + 15, 26, 38)
                p2Spear = pygame.Rect(player2.left, player2.top + 33, 60, 15)
                if p2Spear.right > player1.left and p2Spear.colliderect(player1):
                    if p1DamageImmune == False:
                        p1Health -= 1
                        if musicPlaying:
                            hurtNoise.play()
                        p1DamageImmune = True
                        p1DamageTime = pygame.time.get_ticks()
    
                        damageFlash(player1)
                        
                        player1.left += 30
                        p1Spear.left += 30
                        p1Shield.left += 30
                        
                    else:
                        pass
                    
                elif p2Spear.colliderect(p1Shield) and p1UseShield == True or player2.right > screenWidth:
                    pass
                
                else:
                    player2.right += p2MoveSpeed
         
            if p2UseShield == True:
                if p2FaceDown == True:
                    p2ShieldImage = pygame.image.load('shield-down.png')
                    windowSurface.blit(p2ShieldImage, p2Shield)
                elif p2FaceUp == True:
                    p2ShieldImage = pygame.image.load('shield-up.png')
                    windowSurface.blit(p2ShieldImage, p2Shield)
                    windowSurface.blit(p2Image, player2)
                elif p2FaceLeft == True:
                    p2ShieldImage = pygame.image.load('shield-left.png')
                    windowSurface.blit(p2ShieldImage, p2Shield)
                elif p2FaceRight == True:
                    p2ShieldImage = pygame.image.load('shield-right.png')
                    windowSurface.blit(p2ShieldImage, p2Shield)
                
        healthCounter += 1
        if healthCounter >= newHealth:
            healthCounter = 0
            healthLst.append(pygame.Rect(random.randint(0, screenWidth - healthSize), random.randint(0, screenHeight - healthSize), healthSize, healthSize))
        
        speedCounter += 1
        if speedCounter >= newSpeed:
            speedCounter = 0
            speedLst.append(pygame.Rect(random.randint(0, screenWidth - speedSize), random.randint(0, screenHeight - speedSize), speedSize, speedSize))
        
        for speed in speedLst[:]:
            if player1.colliderect(speed):
                p1SpeedUp = True
                p1SpeedTime = pygame.time.get_ticks()
                damageFlash(player1)
                if musicPlaying:
                    powerUpNoise.play()
                speedLst.remove(speed)
                
        for speed in speedLst[:]:   
            if player2.colliderect(speed):
                p2SpeedUp = True
                p2SpeedTime = pygame.time.get_ticks()
                damageFlash(player2)
                if musicPlaying:
                    powerUpNoise.play()
                speedLst.remove(speed)
    
        for speed in speedLst:
            windowSurface.blit(speedImage, speed)
        
        for health in healthLst[:]:
            if player1.colliderect(health):
                if p1Health < 10:
                    p1Health += 1
                    damageFlash(player1)
                    if musicPlaying:
                        powerUpNoise.play()
                healthLst.remove(health)
                
        for health in healthLst[:]:   
            if player2.colliderect(health):
                if p2Health < 10:
                    p2Health += 1
                    damageFlash(player2)
                    if musicPlaying:
                        powerUpNoise.play()
                healthLst.remove(health)
    
        for health in healthLst:
            windowSurface.blit(healthImage, health)
        
        windowSurface.blit(p1SpearImage,p1Spear)
        windowSurface.blit(p2SpearImage,p2Spear)
        
        updateScore()
        
        pygame.display.update()
        mainClock.tick(60)
