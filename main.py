import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Spawning Cars
    car_manager.random_car()
    car_manager.move()

    # Detect Collision with Car and Player
    for car in car_manager.cars:
        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.game_over()

    # Level Up after Reaching the Finish  Line
    if player.at_finish_line():
        player.reset_position()
        car_manager.speed_up()
        scoreboard.update_level()


screen.exitonclick()
