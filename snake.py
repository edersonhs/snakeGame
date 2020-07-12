import pygame
from pygame.locals import *
from random import randint


def on_grid_random():   # Definindo uma posição para a apple
    x = randint(0, 590)
    y = randint(0, 590)
    # Retornando o resultado da divisão inteira de x/y multiplicado por 10
    return x // 10 * 10, y // 10 * 10


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


# Declaração das direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Sempre que utilizar pygame deve-se utilizar o init
pygame.init()

# Janela 600 x 600
screen = pygame.display.set_mode((600, 600))

# Titulo da janela
pygame.display.set_caption('Snake')

# Declarando a cobra
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))  # Definindo cor da cobra / White

# Declarando a maçã
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))  # Definindo a cor da maçã / Red
apple_pos = on_grid_random()

# Indica a direção atual / Começa indo pra esquerda
my_direction = LEFT

# Objeto para limitar o FPS
clock = pygame.time.Clock()

# Inicio do game
while True:
    clock.tick(13)  # Definind limite de FPS

    # Verificando os eventos (teclas pressionadas)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        # Verificando eventos de teclado
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                my_direction = UP
            if event.key == K_DOWN or event.key == K_s:
                my_direction = DOWN
            if event.key == K_LEFT or event.key == K_a:
                my_direction = LEFT
            if event.key == K_RIGHT or event.key == K_d:
                my_direction = RIGHT

    # verificando se a cabeça da cobra esta na mesma posição que a maçã, ocasionando em uma colisão
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()    # Definindo uma nova posição para apple
        snake.append((0, 0))    # Aumentando o tamanho da snake

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # Definindo movimentação da cobra
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # Limpando a tela
    screen.fill((0, 0, 0))

    # Inserindo maçã na tela
    screen.blit(apple, apple_pos)

    # Colocando a cobra na tela
    for pos in snake:
        screen.blit(snake_skin, pos)

    # Atualiza a tela toda vez que o laço for executado
    pygame.display.update()
