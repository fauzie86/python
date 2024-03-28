import pygame
import sys


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Painting App")


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brush_color = red  


brush_size = 10
brush_pos = [width // 2, height // 2]

def draw_brush(pos):
    pygame.draw.circle(screen, brush_color, pos, brush_size)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]: 
                brush_pos = pygame.mouse.get_pos()
                draw_brush(brush_pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  
                screen.fill(white)
            elif event.key == pygame.K_s:  
                brush_size = 5
            elif event.key == pygame.K_m:  
                brush_size = 10
            elif event.key == pygame.K_l:  
                brush_size = 20
            elif event.key == pygame.K_r:  
                brush_color = red
            elif event.key == pygame.K_g:  
                brush_color = green
            elif event.key == pygame.K_b:  
                brush_color = blue

    
    pygame.display.flip()
    draw_brush(brush_pos)


