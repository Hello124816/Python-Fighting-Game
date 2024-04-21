import pygame

class Animation:
    def __init__(self, sprite_sheet, steps, size, scale):
        self.sprite_sheet = sprite_sheet
        self.steps = steps
        self.size = size
        self.scale = scale
        self.image_list = self.load_images(sprite_sheet, steps, size)


    def load_images(self, sprite_sheet, steps, size):
        image_list = []
        for i in range(0, steps):
            frame = sprite_sheet.subsurface(i*size, 0, size, size)
            image_list.append(pygame.transform.scale(frame, (self.size * self.scale, self.size * self.scale)))
        return image_list