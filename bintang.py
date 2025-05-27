import turtle

# Setup jendela
window = turtle.Screen()
window.bgcolor("black")
window.title("Gambar Bintang dengan Loop")

# Buat objek turtle
bintang = turtle.Turtle()
bintang.color("yellow")
bintang.pensize(2)
bintang.speed(3)

# Gambar bintang dengan loop
for i in range(5):  # Bintang 5 sisi
    bintang.forward(150)
    bintang.right(144)  # Sudut untuk bintang: 180 - (360 / 5)

# Selesai
turtle.done()
