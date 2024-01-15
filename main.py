import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
cars = []
lane_number = 0


# Create line of cars
def create_line_of_cars(lane):
    for y in range(230, -250, -20):
        lane += 1
        if lane % 6 == 0:
            y_cor = random.randint(-230, 230)
            car = CarManager((310, y_cor))
            cars.append(car)
    return lane_number


# move the turtle up

screen.onkey(player.move_up, "Up")
n = 0
game_is_on = True
while game_is_on:
    time.sleep(0.5)
    if n % 3 == 0:
        lane_number = create_line_of_cars(lane_number)
    for i in range(1,6):
        for game_car in cars:
            game_car.move_forward()
            game_car.move_forward()
            if player.distance(game_car) < 15:
                game_is_on = False
            if player.ycor() == 280:
                player.goto(0, -280)

    screen.update()
    n += 17


screen.exitonclick()