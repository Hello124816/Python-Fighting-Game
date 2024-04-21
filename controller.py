import pygame

class Controller:
    def __init__(self, fighter1, fighter2, screen):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.screen = screen


    def move_fighter(self, move_speed):
        self.fighter1.running=False
        self.fighter1.attack_type="none"
        gravity =10
        floor_height = 120
        dx=0
        dy=0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            dx = -move_speed
            self.fighter1.running = True
        if keys[pygame.K_d]:
            dx = move_speed
            self.fighter1.running = True
        if keys[pygame.K_w]:
            if self.fighter1.action == "jump":
                if self.fighter1.frame_index == 1:
                    dy = -move_speed-15
                    self.fighter1.jumping=True
            else: 
                dy = -move_speed-15
                self.fighter1.jumping=True
        if keys[pygame.K_k] and self.fighter1.attack_type == "none":
            self.attack_figher(self.fighter2, self.fighter1, 5, "attack1")
        if keys[pygame.K_v] and self.fighter1.attack_type == "none":
            self.attack_figher(self.fighter2, self.fighter1, 5, "attack2")

            

        # Boundary and gravity
        if self.fighter1.y + self.fighter1.height + floor_height <= 720:
            dy+=gravity    
        if self.fighter1.x + dx < 0:
            dx = -self.fighter1.x
        if self.fighter1.x+dx > 1280-self.fighter1.width:
            dx = 1280 - self.fighter1.x-self.fighter1.width
        if self.fighter1.y + dy < 0:
            dy = -self.fighter1.y
        if dy == 0:
            self.fighter1.jumping = False
        if self.fighter1.x>self.fighter2.x:
            self.fighter1.flip = True
        else:
            self.fighter1.flip = False

        self.fighter1.x += dx
        self.fighter1.y += dy

    def attack_figher(self, defender, attacker, attack_frame, type):
        self.fighter1.attack_type = type
        defender.got_hit(attacker, attack_frame)

    def update(self):
        #check what action the player is performing
        if self.fighter1.hp <= 0:
            self.fighter1.hp = 0
            self.fighter1.alive = False
            self.fighter1.action = "Death"
        elif self.fighter1.hit == True:
            self.fighter1.action = "Hit"
        elif self.fighter1.attack_type == "attack1":
            self.fighter1.action = "attack1"
        elif self.fighter1.attack_type == "attack2":
            self.fighter1.action = "attack2"
        elif self.fighter1.jumping:
            self.fighter1.action = "Jump"
        elif self.fighter1.running:
            self.fighter1.action = "Run"
        else:
            self.fighter1.action = "idle"

        animation_cooldown=50

        start_time = self.fighter1.update_time
        time = pygame.time.get_ticks()
        time_past = time-start_time
        if time_past > animation_cooldown:
            self.fighter1.frame_index+=1
            self.fighter1.update_time = pygame.time.get_ticks()
        #check if the animation has finished
        if self.fighter1.frame_index >= len(self.fighter1.animation[self.fighter1.action].image_list):
            #if the player is dead then end the animation
            if self.fighter1.alive == False:
                self.fighter1.frame_index = len(self.fighter1.animation[self.fighter1.action].image_list) - 1
            else:
                self.fighter1.frame_index = 0        #check if an attack was executed
                if self.fighter1.action == "attack1" or self.fighter1.action == "attack2":
                    self.fighter1.attack_type = "none"
                #check if damage was taken
                if self.fighter1.action == "hit":
                    self.fighter1.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.fighter1.attack_type = "none"
            
    def draw_fighter(self, fighter, screen, offsetx, offsety):
        img = fighter.animation[fighter.action].image_list[fighter.frame_index]
        new_image =  pygame.transform.flip(img, fighter.flip, False)
        screen.blit(new_image, (fighter.x-offsetx, fighter.y-offsety))