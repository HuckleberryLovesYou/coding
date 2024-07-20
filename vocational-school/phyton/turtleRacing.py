import turtle as tur
import random as ran
from time import sleep as sle

WIDTH, HEIGHT = 500, 500 # defines the screen width and height. For example: WIDTH, HEIGHT = 500, 500 creates a grid going from -250 to 250 on x-axis and going from -250 to 250 on y-axis
COLORS = ["red" , "green" , "blue" , "orange" , "yellow" , "black" , "purple" , "pink" , "brown" , "cyan"] #defines all possible colors for the turtles. Increasing the len(COLORS) allows more turtles tp spawn
MIN_DISTANCE, MAX_DISTANCE = 5 , 25 #Values between a random value is chosen to move up the screen
FINISH_LINE = 200 # defines the y-cord of the finish line
SPEED_OF_TURTLE = 2 # 1 is the slowest getting increasingly fast till a max value of 10, 0 is the fastest it can get

def get_amount_of_turtles():
    while True:
        amount_of_turtles = tur.textinput("Turtle Amount" , "Enter the amount of turtles to be racing")
        if amount_of_turtles.isdigit():
            amount_of_turtles = int(amount_of_turtles)
            if 2 <= amount_of_turtles <= 10:
                return amount_of_turtles
            else:
                print("Please enter a value between 2 and 10")
        else:
            print("Please enter a valid number")



def init_turtle():
    scr = tur.Screen()
    scr.setup(WIDTH, HEIGHT)
    scr.title("Turtle Race")
    scr.bgcolor("gray")


def race(colors):
    create_finish_line()
    turtles = create_turtles(colors)
    distance_on_turn = []
    current_pos = []
    winners = []
    while True:
        for racer in turtles:
            x, y = racer.pos()
            #print(f"{x=}, {y=}")
            current_pos.append(y)
        for _ in turtles:
            distance = ran.randrange(MIN_DISTANCE , MAX_DISTANCE)
            #print(f"{distance=}")
            distance_on_turn.append(distance)
        for racer in turtles:
            next_pos = current_pos[turtles.index(racer)] + distance_on_turn[turtles.index(racer)]
            #print(f"{next_pos=}")
            if next_pos >= FINISH_LINE:
                winners.append(colors[turtles.index(racer)])
            racer.forward(distance_on_turn[turtles.index(racer)])
        if len(winners) >= 1:
            return winners
        distance_on_turn = []
        current_pos = []

def create_finish_line():
    tur.shape("blank")
    tur.penup()
    tur.setpos(-WIDTH // 2 + 10, FINISH_LINE + 15)
    tur.pendown()
    tur.write("Finish Line")
    finish_line = tur.Turtle()
    finish_line.color("red")
    finish_line.shape("blank")
    finish_line.speed(0)
    finish_line.pensize(5)
    finish_line.penup()
    finish_line.setpos(-WIDTH // 2 , FINISH_LINE)
    finish_line.pendown()
    finish_line.setpos(WIDTH // 2, FINISH_LINE)



def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        turtle = tur.Turtle()
        turtle.color(color)
        turtle.shape("turtle")
        turtle.speed(SPEED_OF_TURTLE)
        turtle.pencolor("black")
        turtle.left(90)
        turtle.penup()
        turtle.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 20)
        turtle.pendown()
        turtles.append(turtle)
    return turtles

def main():
    turtles = get_amount_of_turtles()
    init_turtle()
    ran.shuffle(COLORS)
    colors = COLORS[:turtles]
    winners = race(colors)
    if len(winners) == 1:
        print(f"The Winner of the race is the turtle with the color {winners[0]}")
    else:
        print("Since multiple turtles finished within the same turn, these are the Winners:")
        for i, winner in enumerate(winners):
            print(f"The {i + 1}. winner is the color {winner}")
    sle(5)

if __name__ == "__main__":
    main()


