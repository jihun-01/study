def create_car(model, year):
    return {
        'model' : model,
        'year' : year
    }

def accel(car, speed):
    car['speed'] = speed
    print(f"{speed}만큼 전진")

my_car = create_car('sonata', 2010)
accel(my_car, 30)
