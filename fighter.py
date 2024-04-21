import pygame

class Fighter:
    def __init__(self, id, hp, x, y, width, height, damage, hitbox, animation, flip):
        self.id = id
        self.hp = hp
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.damage = damage
        self.hitbox = hitbox
        self.animation = animation
        self.flip = flip
        self.attack_type = "none"
        self.frame_index = 0
        self.action = "idle"
        self.update_time = pygame.time.get_ticks()
        self.alive = True
        self.jumping = False
        self.hit = False
        self.running = False

    def got_hit(self, enemy, attack_frame):
        if self.id == "Player_2":
            if not self.hit and enemy.frame_index == attack_frame and self.x - enemy.x -enemy.width <= enemy.hitbox and abs(enemy.y-self.y) <= 150:
                self.hp -= enemy.damage
                self.hit = True

    def move(self, movex, movey):
        self.x += movex
        self.y += movey
