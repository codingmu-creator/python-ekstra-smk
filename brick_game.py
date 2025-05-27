import pygame
import sys

# Inisialisasi pygame
pygame.init()
pygame.mixer.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Font untuk skor
font = pygame.font.SysFont("Arial", 24)

# Paddle
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 30, 120, 15)
paddle_speed = 8

# Bola
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_speed = [4, -4]

# Balok
bricks = []
brick_rows = 5
brick_cols = 8
brick_width = 80
brick_height = 30
brick_margin = 10
offset_y = 60

for row in range(brick_rows):
    for col in range(brick_cols):
        x = col * (brick_width + brick_margin) + 60
        y = row * (brick_height + brick_margin) + offset_y
        bricks.append(pygame.Rect(x, y, brick_width, brick_height))

# Skor
score = 0

# Suara
bounce_sound = pygame.mixer.Sound("eat.mp3")

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kontrol paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Gerakan bola
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Tabrakan dinding
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1
        bounce_sound.play()
    if ball.top <= 0:
        ball_speed[1] *= -1
        bounce_sound.play()
    if ball.bottom >= HEIGHT:
        print("Game Over")
        running = False

    # Tabrakan paddle
    if ball.colliderect(paddle):
        ball_speed[1] *= -1
        bounce_sound.play()

    # Tabrakan bricks
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_speed[1] *= -1
        score += 10
        bounce_sound.play()

    # Gambar paddle dan bola
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Gambar bricks
    for brick in bricks:
        pygame.draw.rect(screen, ORANGE, brick)

    # Gambar skor
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Cek kemenangan
    if not bricks:
        win_text = font.render("You Win!", True, RED)
        screen.blit(win_text, (WIDTH // 2 - 50, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
