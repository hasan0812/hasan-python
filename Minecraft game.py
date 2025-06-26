# import turtle
# import random

# # Setup screen
# screen = turtle.Screen()
# screen.title("Python Minecraft-like")
# screen.setup(600, 600)

# # Player (a turtle)
# player = turtle.Turtle()
# player.shape("square")
# player.color("blue")
# player.penup()
# player.speed(0)  # Fastest animation

# # Blocks (dirt)
# blocks = []
# for _ in range(20):
#     block = turtle.Turtle()
#     block.shape("square")
#     block.color("brown")
#     block.penup()
#     block.speed(0)
#     block.goto(random.randint(-250, 250), random.randint(-250, 250))  # Corrected line
#     blocks.append(block)

# # Movement functions
# def move_up():
#     player.sety(player.ycor() + 20)

# def move_down():
#     player.sety(player.ycor() - 20)

# def move_left():
#     player.setx(player.xcor() - 20)

# def move_right():
#     player.setx(player.xcor() + 20)

# # Keyboard controls
# screen.listen()
# screen.onkey(move_up, "w")
# screen.onkey(move_down, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")

# # Block-breaking function (optional)
# def break_block(x, y):
#     for block in blocks[:]:  # Iterate over a copy of the list
#         if block.distance(x, y) < 20:
#             block.hideturtle()
#             blocks.remove(block)

# screen.onclick(break_block)  # Click to break blocks

# turtle.done()

import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.title("Python Minecraft-like Overworld")
screen.setup(800, 600)
screen.bgcolor("skyblue")

# Constants
BLOCK_SIZE = 20
GRAVITY = 0.5
JUMP_STRENGTH = 10
WORLD_WIDTH = 40  # In blocks
WORLD_HEIGHT = 20  # In blocks

# Player setup
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.speed(0)
player.dy = 0  # Vertical velocity
player.flying = False  # Debug mode

# Block types
GRASS = "green"
DIRT = "brown"
STONE = "gray"
WOOD = "tan"
LEAVES = "dark green"
WATER = "blue"

# World generation
world = {}
surface_levels = {}

# Generate terrain heights
for x in range(-WORLD_WIDTH//2, WORLD_WIDTH//2):
    # Base terrain with some noise
    height = 5 + int(10 * math.sin(x/5)) + random.randint(-1, 1)
    surface_levels[x] = height
    
    # Generate layers
    for y in range(-WORLD_HEIGHT//2, WORLD_HEIGHT//2):
        if y == height:
            world[(x, y)] = GRASS
        elif y < height and y > height - 4:
            world[(x, y)] = DIRT
        elif y <= height - 4:
            world[(x, y)] = STONE
        elif random.random() < 0.02 and y > height:  # Trees
            if y == height + 1:
                world[(x, y)] = WOOD
            elif height + 2 <= y <= height + 4 and abs(x) % 3 == 0:
                world[(x, y)] = LEAVES

# Add some water
for x in range(-5, 6):
    for y in range(-2, 1):
        if (x, y) not in world:
            world[(x, y)] = WATER

# Draw the world
block_turtles = {}
for (x, y), color in world.items():
    block = turtle.Turtle()
    block.shape("square")
    block.color(color)
    block.penup()
    block.speed(0)
    block.goto(x * BLOCK_SIZE, y * BLOCK_SIZE)
    block_turtles[(x, y)] = block

# Movement functions
def move_up():
    if player.flying:
        player.sety(player.ycor() + BLOCK_SIZE)
    else:
        # Check if standing on a block
        player_x = round(player.xcor() / BLOCK_SIZE)
        player_y = round(player.ycor() / BLOCK_SIZE)
        if (player_x, player_y - 1) in world:
            player.dy = JUMP_STRENGTH

def move_down():
    if player.flying:
        player.sety(player.ycor() - BLOCK_SIZE)

def move_left():
    player.setx(player.xcor() - BLOCK_SIZE)

def move_right():
    player.setx(player.xcor() + BLOCK_SIZE)

def toggle_fly():
    player.flying = not player.flying
    if player.flying:
        player.color("red")
    else:
        player.color("blue")

# Keyboard controls
screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(move_down, "s") if player.flying else None
screen.onkey(toggle_fly, "f")

# Physics update
def update():
    if not player.flying:
        # Apply gravity
        player.dy -= GRAVITY
        player.sety(player.ycor() + player.dy)
        
        # Check for collisions
        player_x = round(player.xcor() / BLOCK_SIZE)
        player_y = round(player.ycor() / BLOCK_SIZE)
        
        # Ground collision
        if (player_x, player_y - 1) in world:
            player.sety((player_y) * BLOCK_SIZE)
            player.dy = 0
    
    screen.ontimer(update, 30)

# Block breaking/placing
def break_block(x, y):
    block_x = round(x / BLOCK_SIZE)
    block_y = round(y / BLOCK_SIZE)
    if (block_x, block_y) in world:
        block_turtles[(block_x, block_y)].hideturtle()
        del world[(block_x, block_y)]
        del block_turtles[(block_x, block_y)]

def place_block(x, y):
    block_x = round(x / BLOCK_SIZE)
    block_y = round(y / BLOCK_SIZE)
    if (block_x, block_y) not in world:
        new_block = turtle.Turtle()
        new_block.shape("square")
        new_block.color(DIRT)
        new_block.penup()
        new_block.speed(0)
        new_block.goto(block_x * BLOCK_SIZE, block_y * BLOCK_SIZE)
        world[(block_x, block_y)] = DIRT
        block_turtles[(block_x, block_y)] = new_block

screen.onclick(break_block, 1)  # Left click to break
screen.onclick(place_block, 3)  # Right click to place

# Start game loop
update()
turtle.done()

# Controls:

# WASD to move (W to jump when on ground)

# F to toggle flying mode

# Left-click to break blocks

# Right-click to place dirt blocks