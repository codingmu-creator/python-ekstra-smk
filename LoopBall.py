import pygame
import sys

# Inisialisasi pygame
pygame.init()
pygame.mixer.init()

# Ukuran layar
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dua Bola Mantul")
clock = pygame.time.Clock()

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Bola 1
ball1 = pygame.Rect(100, 100, 20, 20)
speed1 = [4, 3]

# Bola 2
ball2 = pygame.Rect(400, 300, 30, 30)
speed2 = [-3, 5]

# Suara pantulan
bounce_sound = pygame.mixer.Sound("eat.mp3")  # Pastikan file ini ada di folder yang sama

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Gambar kedua bola
    pygame.draw.ellipse(screen, RED, ball1)
    pygame.draw.ellipse(screen, BLUE, ball2)

    # Gerakkan bola 1
    ball1.x += speed1[0]
    ball1.y += speed1[1]
    if ball1.left <= 0 or ball1.right >= WIDTH:
        speed1[0] *= -1
        bounce_sound.play()
    if ball1.top <= 0 or ball1.bottom >= HEIGHT:
        speed1[1] *= -1
        bounce_sound.play()

    # Gerakkan bola 2
    ball2.x += speed2[0]
    ball2.y += speed2[1]
    if ball2.left <= 0 or ball2.right >= WIDTH:
        speed2[0] *= -1
        bounce_sound.play()
    if ball2.top <= 0 or ball2.bottom >= HEIGHT:
        speed2[1] *= -1
        bounce_sound.play()

    # Event keluar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
