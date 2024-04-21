import pygame

class Computer:
    def __init__(self, fighter1, fighter2, screen):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.screen = screen

    def draw_enemy(self, offsetx, offsety):
        img = self.fighter2.animation[self.fighter2.action].image_list[self.fighter2.frame_index]
        new_image =  pygame.transform.flip(img, self.fighter2.flip, False)
        self.screen.blit(new_image, (self.fighter2.x-offsetx, self.fighter2.y-offsety))

    def update_enemy(self):
        #check what action the player is performing
        if self.fighter2.hp <= 0:
            self.fighter2.hp = 0
            self.fighter2.alive = False
            self.fighter2.action = "Death"
        elif self.fighter2.hit == True:
            self.fighter2.action = "Hit"
        elif self.fighter2.attack_type == "attack1":
            self.fighter2.action = "attack1"
        elif self.fighter2.attack_type == "attack2":
            self.fighter1.action = "attack2"
        elif self.fighter2.jumping:
            self.fighter2.action = "Jump"
        elif self.fighter2.running:
            self.fighter2.action = "Run"
        else:
            self.fighter2.action = "idle"

        animation_cooldown=50

        start_time = self.fighter2.update_time
        time = pygame.time.get_ticks()
        time_past = time-start_time
        if time_past > animation_cooldown:
            self.fighter2.frame_index+=1
            self.fighter2.update_time = pygame.time.get_ticks()
        #check if the animation has finished
        if self.fighter2.frame_index >= len(self.fighter2.animation[self.fighter2.action].image_list):
            #if the player is dead then end the animation
            if self.fighter2.alive == False:
                self.fighter2.frame_index = len(self.fighter2.animation[self.fighter2.action].image_list) - 1
            else:
                self.fighter2.frame_index = 0        #check if an attack was executed
                if self.fighter2.action == "attack1" or self.fighter2.action == "attack2":
                    self.fighter2.attack_type = "none"
                #check if damage was taken
                if self.fighter2.action == "Hit":
                    self.fighter2.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.fighter2.attack_type = "none"

    def attack_figher(self, defender, attacker, attack_frame, type):
        self.fighter2.attack_type = type
        defender.got_hit(attacker, attack_frame)

    def move_enemy(self, speed):
        self.fighter2.running=False
        self.fighter2.attack_type="none"
        gravity =10
        floor_height = 120
        dx=0
        dy=0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx = -speed
            self.fighter2.running = True
        if keys[pygame.K_RIGHT]:
            dx = speed
            self.fighter2.running = True
        
        # Boundary and gravity
        if self.fighter2.y + self.fighter2.height + floor_height <= 720:
            dy+=gravity    
        if self.fighter2.x + dx < 0:
            dx = -self.fighter2.x
        if self.fighter2.x+dx > 1280-self.fighter2.width:
            dx = 1280 - self.fighter2.x-self.fighter2.width
        if self.fighter2.y + dy < 0:
            dy = -self.fighter2.y
        if dy == 0:
            self.fighter2.jumping = False
        if self.fighter2.x<self.fighter1.x:
            self.fighter2.flip = False
        else:
            self.fighter2.flip = True

        self.fighter2.x += dx
        self.fighter2.y += dy