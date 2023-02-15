import pygame

pygame.init()

fps = 120
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint!')


def draw_menu():
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    
run = True
while run:
    timer.tick(fps)                         # fps in game
    screen.fill((255, 255, 255))            # or screen.fill('white')
    draw_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.flip()
pygame.quit()