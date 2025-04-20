import pygame
import time
import random

snake_velocity = 30

windwidth = 800
windheight = 600

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((windwidth, windheight))

fps = pygame.time.Clock()

snake_pos = [100.0, 100.0] 

snake_body = [[100, 100], [90, 100], [80, 100]]

fruit_pos = [random.randrange(1, (windwidth//10)) * 10, random.randrange(1, (windheight//10)) * 10]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0
growth_counter = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Score : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    
    
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_spawn = False
        growth_counter += 5  

    
    if growth_counter > 0:
        growth_counter -= 1
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (windwidth//10)) * 10, random.randrange(1,(windheight//10)) * 10]

    fruit_spawn = True
    game_window.fill(blue)

    for pos in snake_body:
        pygame.draw.circle(game_window, green, (round(pos[0]), round(pos[1])), 10)
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > windwidth - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > windheight - 10:
        game_over()
    
    for block in snake_body [1 : ] :
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    
    show_score (1, white, 'times new roman', 20)

    pygame.display.update()

    snake_velocity = 10 + (score // 10)  
    fps.tick(snake_velocity)