import pygame
import time
import random

windwidth = 800
windheight = 600
grid_size = 10  

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
snake_prev_head = None

snake_body = [[100, 100], [90, 100], [80, 100]]

fruit_pos = [random.randrange(1, (windwidth // grid_size)) * grid_size, random.randrange(1, (windheight // grid_size)) * grid_size]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0
growth_counter = 0

snake_velocity = 10 

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (windwidth // 2, 10)
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Score : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.center = (windwidth // 2, windheight // 2)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def reset_game():
    global snake_pos, snake_body, fruit_pos, fruit_spawn, direction, change_to, score, growth_counter, snake_velocity, snake_prev_head
    snake_pos = [100.0, 100.0]
    snake_prev_head = None
    snake_body = [[100, 100], [90, 100], [80, 100]]
    fruit_pos = [random.randrange(1, (windwidth // grid_size)) * grid_size, random.randrange(1, (windheight // grid_size)) * grid_size]
    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    growth_counter = 0
    snake_velocity = 10 

def check_collision(snake_head, fruit_pos):

   
    if abs(snake_head[0] - fruit_pos[0]) < grid_size and abs(snake_head[1] - fruit_pos[1]) < grid_size:
        return True
    return False

fruit_texture = pygame.image.load('Graphics/apple.png')

head_textures = {
    'UP': pygame.image.load('Graphics/head_up.png'),
    'DOWN': pygame.image.load('Graphics/head_down.png'),
    'LEFT': pygame.image.load('Graphics/head_left.png'),
    'RIGHT': pygame.image.load('Graphics/head_right.png')
}

tail_textures = {
    'UP': pygame.image.load('Graphics/tail_up.png'),
    'DOWN': pygame.image.load('Graphics/tail_down.png'),
    'LEFT': pygame.image.load('Graphics/tail_left.png'),
    'RIGHT': pygame.image.load('Graphics/tail_right.png')
}

body_textures = {
    'HORIZONTAL': pygame.image.load('Graphics/body_horizontal.png'),
    'VERTICAL': pygame.image.load('Graphics/body_vertical.png'),
    'TOPLEFT': pygame.image.load('Graphics/body_topleft.png'),
    'TOPRIGHT': pygame.image.load('Graphics/body_topright.png'),
    'BOTTOMLEFT': pygame.image.load('Graphics/body_bottomleft.png'),
    'BOTTOMRIGHT': pygame.image.load('Graphics/body_bottomright.png')
}

running = True
paused = False
speed_increment = 0.5  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
            if not paused:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

    if paused:
        pause_font = pygame.font.SysFont('times new roman', 50)
        pause_surface = pause_font.render('Game Paused', True, white)
        pause_rect = pause_surface.get_rect()
        pause_rect.center = (windwidth // 2, windheight // 2 - 50)
        game_window.blit(pause_surface, pause_rect)

        reset_font = pygame.font.SysFont('times new roman', 30)
        reset_surface = reset_font.render('Reset Game', True, white)
        reset_rect = reset_surface.get_rect()
        reset_rect.center = (windwidth // 2, windheight // 2 + 50)
        pygame.draw.rect(game_window, (50, 50, 50), reset_rect.inflate(20, 10))
        game_window.blit(reset_surface, reset_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if reset_rect.collidepoint(mouse_pos):
                    reset_game()
                    paused = False

        continue

    if not paused:
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        snake_prev_head = list(snake_pos)


        if direction == 'UP':
            snake_pos[1] -= snake_velocity
        if direction == 'DOWN':
            snake_pos[1] += snake_velocity
        if direction == 'LEFT':
            snake_pos[0] -= snake_velocity
        if direction == 'RIGHT':
            snake_pos[0] += snake_velocity

        #initiate wrapping when the snake touches the the border instead of losing

        if snake_pos[0] < 0:
            snake_pos[0] = windwidth - grid_size
        elif snake_pos[0] >= windwidth:
            snake_pos[0] = 0
        elif snake_pos[1] < 0:
            snake_pos[1] = windheight - grid_size
        elif snake_pos[1] >= windheight:
            snake_pos[1] = 0

        snake_body.insert(0, list(snake_pos))

        #updated the check collision so that it ranged based rather than exact perfect collision

        if check_collision(snake_pos, fruit_pos):
            score += 10
            fruit_spawn = False
            growth_counter += 5
            snake_velocity += speed_increment 

        if growth_counter > 0:
            growth_counter -= 1
        else:
            snake_body.pop()

        if not fruit_spawn:
           
            fruit_pos = [random.randrange(0, (windwidth // grid_size)) * grid_size,
                         random.randrange(0, (windheight // grid_size)) * grid_size]
            fruit_spawn = True
        else:
        
            pass

        game_window.fill(black)

        #added the snake textures based on the position of the snake and length

        for index, pos in enumerate(snake_body):
            if index == 0:
                game_window.blit(head_textures[direction], (pos[0], pos[1]))
            elif index == len(snake_body) - 1:
                tail_direction = 'UP'
                if snake_body[-2][0] < pos[0]:
                    tail_direction = 'RIGHT'
                elif snake_body[-2][0] > pos[0]:
                    tail_direction = 'LEFT'
                elif snake_body[-2][1] < pos[1]:
                    tail_direction = 'DOWN'
                elif snake_body[-2][1] > pos[1]:
                    tail_direction = 'UP'
                game_window.blit(tail_textures[tail_direction], (pos[0], pos[1]))
            else:
                prev_segment = snake_body[index - 1]
                next_segment = snake_body[index + 1]

                if prev_segment[0] == next_segment[0]:
                    game_window.blit(body_textures['VERTICAL'], (pos[0], pos[1]))
                elif prev_segment[1] == next_segment[1]:
                    game_window.blit(body_textures['HORIZONTAL'], (pos[0], pos[1]))
                elif (prev_segment[0] < pos[0] and next_segment[1] < pos[1]) or \
                     (prev_segment[1] < pos[1] and next_segment[0] < pos[0]):
                    game_window.blit(body_textures['TOPLEFT'], (pos[0], pos[1]))
                elif (prev_segment[0] > pos[0] and next_segment[1] < pos[1]) or \
                     (prev_segment[1] < pos[1] and next_segment[0] > pos[0]):
                    game_window.blit(body_textures['TOPRIGHT'], (pos[0], pos[1]))
                elif (prev_segment[0] < pos[0] and next_segment[1] > pos[1]) or \
                     (prev_segment[1] > pos[1] and next_segment[0] < pos[0]):
                    game_window.blit(body_textures['BOTTOMLEFT'], (pos[0], pos[1]))
                elif (prev_segment[0] > pos[0] and next_segment[1] > pos[1]) or \
                     (prev_segment[1] > pos[1] and next_segment[0] > pos[0]):
                    game_window.blit(body_textures['BOTTOMRIGHT'], (pos[0], pos[1]))

        game_window.blit(fruit_texture, (fruit_pos[0], fruit_pos[1]))

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        show_score(1, white, 'times new roman', 20)

        pygame.display.update()
        fps.tick(30)

pygame.quit()
quit()