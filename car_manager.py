from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_COR = 310
POSSIBLE_Y_COR = [-230, -180, -130, -80, -30, 20, 70, 120, 170, 220, 270]


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def random_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=X_COR, y=random.choice(POSSIBLE_Y_COR))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            if car.xcor() >= -320:
                car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
