import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done  = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.    :
            done = True
    pygame.display.flip()