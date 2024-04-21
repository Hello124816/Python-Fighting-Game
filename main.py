from view import View
import pygame
from fighter import Fighter
from controller import Controller
from animation import Animation
from computer import Computer

pygame.init()

clock = pygame.time.Clock()

#load background image
background1 =  View(1280, 720, 60, "Assets/Images/Background.jpeg")
screen = pygame.display.set_mode((background1.width, background1.height))
pygame.display.set_caption("Brawler")
bg_image = pygame.image.load(background1.bg_image).convert_alpha()

idle1_sheet = pygame.image.load('Assets/Fighter1/Sprites/Idle.png').convert_alpha()
idle1_animation = Animation(idle1_sheet, 8, 200, 4)
attack1_sheet = pygame.image.load('Assets/Fighter1/Sprites/Attack1.png').convert_alpha()
attack1_animation = Animation(attack1_sheet, 6, 200, 4)
attack2_sheet = pygame.image.load('Assets/Fighter1/Sprites/Attack2.png').convert_alpha()
attack2_animation = Animation(attack2_sheet, 6, 200, 4)
Death_sheet = pygame.image.load('Assets/Fighter1/Sprites/Death.png').convert_alpha()
Death_animation = Animation(Death_sheet, 6, 200, 4)
Fall_sheet = pygame.image.load('Assets/Fighter1/Sprites/Fall.png').convert_alpha()
Fall_animation = Animation(Fall_sheet, 2, 200, 4)
Hit_sheet = pygame.image.load('Assets/Fighter1/Sprites/Hit.png').convert_alpha()
Hit_animation = Animation(Hit_sheet, 4, 200, 4)
Jump_sheet = pygame.image.load('Assets/Fighter1/Sprites/Jump.png').convert_alpha()
Jump_animation = Animation(Jump_sheet, 2, 200, 4)
Run_sheet = pygame.image.load('Assets/Fighter1/Sprites/Run.png').convert_alpha()
Run_animation = Animation(Run_sheet, 8, 200, 4)


idle1_sheet2 = pygame.image.load('Assets/Fighter2/Sprites/Idle.png').convert_alpha()
idle1_animation2 = Animation(idle1_sheet2, 4, 200, 3.8)
attack1_sheet2 = pygame.image.load('Assets/Fighter2/Sprites/Attack1.png').convert_alpha()
attack1_animation2 = Animation(attack1_sheet2, 4, 200, 3.8)
attack2_sheet2 = pygame.image.load('Assets/Fighter2/Sprites/Attack2.png').convert_alpha()
attack2_animation2 = Animation(attack2_sheet2, 4, 200, 3.8)
Death_sheet2 = pygame.image.load('Assets/Fighter2/Sprites/Death.png').convert_alpha()
Death_animation2 = Animation(Death_sheet2, 7, 200, 3.8)
Fall_sheet2 = pygame.image.load('Assets/Fighter2/Sprites/Fall.png').convert_alpha()
Fall_animation2 = Animation(Fall_sheet2, 2, 200, 3.8)
Hit_sheet2 = pygame.image.load('Assets/Fighter2/Sprites/Take hit.png').convert_alpha()
Hit_animation2 = Animation(Hit_sheet2, 3, 200, 3.8)
Jump_sheet2 = pygame.image.load('Assets/Fighter2/Sprites/Jump.png').convert_alpha()
Jump_animation2 = Animation(Jump_sheet2, 2, 200, 3.8)
Run_sheet2 = pygame.image.load('Assets/Fighter2/Sprites/Run.png').convert_alpha()
Run_animation2 = Animation(Run_sheet2, 8, 200, 3.8)

fighter1_animations = {
    "idle": idle1_animation,
    "attack1": attack1_animation,
    "attack2": attack2_animation,
    "Death": Death_animation,
    "Fall": Fall_animation,
    "Hit": Hit_animation,
    "Jump": Jump_animation,
    "Run": Run_animation,}
fighter2_animations = {
    "idle": idle1_animation2,
    "attack1": attack1_animation2,
    "attack2": attack2_animation2,
    "Death": Death_animation2,
    "Fall": Fall_animation2,
    "Hit": Hit_animation2,
    "Jump": Jump_animation2,
    "Run": Run_animation2,   
}

# Fighter(self, id, hp, x, y, width, height, damage, hitbox, animation):
fighter1 = Fighter("Player_1", 100, 100, 400, 200, 200, 10, 250, fighter1_animations, False)
fighter2 = Fighter("Player_2", 150, 1000, 420, 100, 180, 5, 25, fighter2_animations, True)
controller1 = Controller(fighter1, fighter2, screen)
computer2 = Computer(fighter1, fighter2, screen)

def draw_bg():
    screen.blit(bg_image, (0, 0))

def draw_hp(health, maxhealth, x, y):
    ratio=health/maxhealth
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 500, 30))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x, y, 500*ratio, 30))


#Gameloop
run = True

while run:
    clock.tick(background1.framerate)

    draw_bg()

    draw_hp(fighter1.hp, 100, 20, 20)
    draw_hp(fighter2.hp, 150, 760, 20)

    controller1.move_fighter(10)
    controller1.update()
    controller1.draw_fighter(fighter1, screen, 300, 200)

    computer2.move_enemy(10)
    computer2.update_enemy()
    computer2.draw_enemy(300, 200)

    #event handlezr
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #update display
    pygame.display.update()
pygame.quit()