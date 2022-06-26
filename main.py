from tkinter import *
import random
from game_settings import *


class Snake:
    
    def __init__(self):
        
        # Snake body
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Append snake body into coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Draw snake and append
        for x, y in self.coordinates:
            snake_shape = canvas.create_rectangle(x , y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(snake_shape)
        
class Food:
    
    def __init__(self):
        
        # Generate random coordinates of Food
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x , y]

        # Food
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x , y))

    snake_shape = canvas.create_rectangle(x , y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOR)

    snake.squares.insert(0, snake_shape)

    # Check if snake and food are overlapping
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        # Increment score and change label
        score += 1
        label.config(text ="Score: {}".format(score))
        canvas.delete("food")

        # Put new food
        food = Food()

    else:
        # Delete last body part of snake after moving

        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    # Change directions of Snake
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collision(snake):
    x , y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

def game_over():
    canvas.delete(ALL)

    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,  font=('Arial', 20), text="GAME OVER, YOU LOSE!!", fill="red")



window = Tk()
window.title("Kelechi's Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

# Game top Label
label = Label(window, text="Score: {}".format(score), font=('Arial', 40))
label.pack()

# Game Canvas Body
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Snake and Food
snake = Snake()
food = Food()

next_turn(snake, food)


window.mainloop()