import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Leveling & Upgrade")
clock = pygame.time.Clock()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Font
font = pygame.font.SysFont("Arial", 24)

# Paddle
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 30, 120, 15)
paddle_speed = 8

# Bola utama
balls = [
    {
        "rect": pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20),
        "speed": [4, -4]
    }
]

# Suara
bounce_sound = pygame.mixer.Sound("eat.mp3")

# Level
level = 1
score = 0

# Brick types
BRICK_TYPES = {
    "normal": ORANGE,
    "healing": GREEN,
    "bonus": YELLOW
}

def generate_bricks(level):
    bricks = []
    brick_rows = 3 + level  # makin tinggi level, makin banyak baris
    brick_cols = 8
    brick_width = 80
    brick_height = 30
    brick_margin = 10
    offset_y = 60

    for row in range(brick_rows):
        for col in range(brick_cols):
            x = col * (brick_width + brick_margin) + 60
            y = row * (brick_height + brick_margin) + offset_y
            rect = pygame.Rect(x, y, brick_width, brick_height)
            brick_type = random.choices(["normal", "healing", "bonus"], [0.7, 0.2, 0.1])[0]
            bricks.append({"rect": rect, "type": brick_type})
    return bricks

bricks = generate_bricks(level)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Update and draw each ball
    for ball in balls:
        ball["rect"].x += ball["speed"][0]
        ball["rect"].y += ball["speed"][1]

        # Wall collisions
        if ball["rect"].left <= 0 or ball["rect"].right >= WIDTH:
            ball["speed"][0] *= -1
            bounce_sound.play()
        if ball["rect"].top <= 0:
            ball["speed"][1] *= -1
            bounce_sound.play()
        if ball["rect"].bottom >= HEIGHT:
            balls.remove(ball)
            continue

        # Paddle collision
        if ball["rect"].colliderect(paddle):
            ball["speed"][1] *= -1
            bounce_sound.play()

        # Brick collision
        for brick in bricks[:]:
            if ball["rect"].colliderect(brick["rect"]):
                ball["speed"][1] *= -1
                bounce_sound.play()
                if brick["type"] == "normal":
                    score += 10
                elif brick["type"] == "healing":
                    score += 25  # Bisa diganti sistem nyawa
                elif brick["type"] == "bonus":
                    score += 15
                    # Tambah bola baru
                    new_ball = {
                        "rect": pygame.Rect(ball["rect"].x, ball["rect"].y, 20, 20),
                        "speed": [random.choice([-4, 4]), -4]
                    }
                    balls.append(new_ball)
                bricks.remove(brick)
                break

        # Gambar bola
        pygame.draw.ellipse(screen, WHITE, ball["rect"])

    # Gambar paddle
    pygame.draw.rect(screen, BLUE, paddle)

    # Gambar bricks
    for brick in bricks:
        color = BRICK_TYPES[brick["type"]]
        pygame.draw.rect(screen, color, brick["rect"])

    # Teks skor dan level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Cek level selesai
    if not bricks:
        level += 1
        bricks = generate_bricks(level)
        # Reset bola
        balls = [{
            "rect": pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20),
            "speed": [4, -4]
        }]

    # Cek game over
    if len(balls) == 0:
        game_over = font.render("Game Over!", True, RED)
        screen.blit(game_over, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
