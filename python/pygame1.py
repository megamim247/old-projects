import pygame
import time
import math

GUY=pygame.image.load("amogus.png")
BG=pygame.image.load("susland.png")
WIDTH,HEIGHT=200,200
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("platformer")
FPS=60

run=True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
    WIN.blit(BG)
    WIN.blit(GUY)