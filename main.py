from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.rect.w = w
        self.rect.h = h
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
window = display.set_mode((700,500))
display.set_caption('saveEcoCity')
clock = time.Clock()
FPS = 60
game = True
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
                
    display.update()
    clock.tick(FPS)