import turtle
import colorsys

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)

# Setup warna HSL ke RGB
hue = 0
n = 100  # jumlah spiral

for i in range(360):
    # Atur warna
    color = colorsys.hsv_to_rgb(hue, 1, 1)  # HSL → RGB
    spiral.color(color)
    spiral.forward(i * 2)
    spiral.left(59)
    hue += 1/n  # agar berputar warnanya

# Selesai
turtle.done()
