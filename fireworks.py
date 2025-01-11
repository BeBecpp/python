import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy New Year")
screen.setup(width=800, height=600)

# Create a turtle object for the text
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("gold")

# Function to display the message
def display_message():
    t.goto(0, 100)
    t.write("HAPPY NEW YEAR!", align="center", font=("Arial", 36, "bold"))

# Create fireworks effect
def fireworks(x, y):
    firework = turtle.Turtle()
    firework.hideturtle()
    firework.speed(0)
    firework.penup()
    firework.goto(x, y)
    firework.color("red")
    firework.pendown()

    for _ in range(36):
        firework.forward(100)
        firework.backward(100)
        firework.right(10)

# Display fireworks animation
for i in range(5):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    fireworks(x, y)

# Display the message
display_message()

# Keep the window open
time.sleep(5)
turtle.done()
