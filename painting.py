import pygame

pygame.init()

fps = 240
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_size = 0
active_color = 'white'
painting = []
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint!')


def draw_menu():
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155, 35), 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215, 35), 5)
    brush_list = [s_brush, m_brush, l_brush, xl_brush]
    
    
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 65, 10, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 95, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 125, 10, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 35, 40, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 65, 40, 25, 25])
    white = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 95, 40, 25, 25])
    black = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 125, 40, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),  (255, 255, 255)]
    return brush_list, color_rect, rgb_list
    
def draw_painting(paints):
    for i in range(len(paints)):
          pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])
run = True
while run:
    timer.tick(fps)                                    # fps in game
    screen.fill((255, 255, 255))                       # or screen.fill('white')
    mouse_coordinate = pygame.mouse.get_pos()          # coordinate of mouse position (x, y)
    left_click = pygame.mouse.get_pressed()[0]
    right_click = pygame.mouse.get_pressed()[2]
    
    if mouse_coordinate[1] > 70 and (left_click or right_click): 
        painting.append((active_color, mouse_coordinate, active_size))
    draw_painting(painting)
    
    if mouse_coordinate[1] > 70: 
        pygame.draw.circle(screen, active_color, mouse_coordinate, active_size)
    
    brushes, colors, rgb = draw_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):       # to take size of brush
                    active_size = 5 + (i * 5)
            
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):        # to take the color of brush
                    active_color = rgb[i]
                    
    pygame.display.flip()
pygame.quit()