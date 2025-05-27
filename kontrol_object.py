import turtle

# Setup layar
win = turtle.Screen()
win.title("Gerak Objek dengan Keyboard")
win.bgcolor("lightblue")

# Setup karakter
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Fungsi gerak
def go_up():
    player.setheading(90)
    player.forward(20)

def go_down():
    player.setheading(270)
    player.forward(20)

def go_left():
    player.setheading(180)
    player.forward(20)

def go_right():
    player.setheading(0)
    player.forward(20)

# Binding key
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Menjaga window tetap terbuka
win.mainloop()
