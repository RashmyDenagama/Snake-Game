import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Modern Snake Game by CareYou Team')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (50, 153, 213)
green = (0, 255, 0)
red = (213, 50, 80)

# Snake settings
snake_block = 20

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)
clock = pygame.time.Clock()

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block], border_radius=5)

def show_score(score, player_name):
    value = score_font.render(f"{player_name} Score: {score}", True, white)
    dis.blit(value, [10, 10])

def show_message(msg, color, y_offset=0):
    mesg = font_style.render(msg, True, color)
    rect = mesg.get_rect(center=(width / 2, height / 2 + y_offset))
    dis.blit(mesg, rect)

def login_screen():
    input_box = pygame.Rect(width // 2 - 100, height // 2 - 20, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 36)

    while True:
        dis.fill(black)
        show_message("Enter your name and press ENTER", white, y_offset=-50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text.strip() or "Player"
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = font.render(text, True, color)
        input_box.w = max(200, txt_surface.get_width() + 10)
        dis.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(dis, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)

def level_selection_screen():
    font = pygame.font.SysFont("bahnschrift", 35)
    easy_btn = pygame.Rect(width // 2 - 100, height // 2 - 60, 200, 50)
    medium_btn = pygame.Rect(width // 2 - 100, height // 2, 200, 50)
    hard_btn = pygame.Rect(width // 2 - 100, height // 2 + 60, 200, 50)

    while True:
        dis.fill(black)
        show_message("Choose Difficulty Level", white, y_offset=-120)

        pygame.draw.rect(dis, green, easy_btn)
        pygame.draw.rect(dis, (255, 165, 0), medium_btn)
        pygame.draw.rect(dis, red, hard_btn)

        dis.blit(font.render("Easy", True, black), easy_btn.move(60, 10))
        dis.blit(font.render("Medium", True, black), medium_btn.move(40, 10))
        dis.blit(font.render("Hard", True, black), hard_btn.move(60, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_btn.collidepoint(event.pos):
                    return 10  # Easy speed
                elif medium_btn.collidepoint(event.pos):
                    return 15  # Medium speed
                elif hard_btn.collidepoint(event.pos):
                    return 25  # Hard speed

def game_loop(player_name, snake_speed):
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            dis.fill(black)
            show_message(f"Game Over, {player_name}!", red, -50)
            show_message("Press Q to Quit or C to Play Again", white, 10)
            show_message(f"Final Score: {length_of_snake - 1}", white, 60)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop(player_name, snake_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Boundary check
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block], border_radius=5)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check self-collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        show_score(length_of_snake - 1, player_name)
        pygame.display.update()

        # Check food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Main Execution
player = login_screen()
speed = level_selection_screen()
game_loop(player, speed)
