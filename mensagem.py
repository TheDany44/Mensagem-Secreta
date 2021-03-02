
import pygame, sys
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Test Run")

font = pygame.font.SysFont("Times New Roman, Arial",50)
text = font.render("O David é gay.",True,(255,255,255))
textRect = text.get_rect()
textRect.center = (250,250)

rect = pygame.Rect(0,0,350,90)
rect.center = (250,250)

pygame.draw.rect(screen,(0, 197, 144),rect)
screen.blit(text,textRect)


pygame.display.update()

click = False
while True:

    mx, my = pygame.mouse.get_pos()

    if click:
        if rect.collidepoint(mx,my):
            screen.fill((0,0,0))

    click = False

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
