import pygame

pygame.init()
window_resolution = ( 1080, 1800)

pygame.display.set_caption("pygame test 1.2")
window_surface = pygame.display.set_mode(window_resolution)



launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

window_surface.blit(cat, [10 , 10] )
pygame.display.flip()
