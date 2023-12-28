import threading
import time
import random


class TrafficLight:
    def __init__(self):
        self.straight_semaphore = threading.Semaphore(1)
        self.turn_semaphore = threading.Semaphore(1)
        self.intersection_semaphore = threading.Semaphore(1)
        self.stop_flag = threading.Event()

    def set_green_light(self, direction):
        if direction == 'straight':
            self.straight_semaphore.release()
            self.turn_semaphore.acquire()
            print(f'Traffic light set to green for {direction} traffic.')
        elif direction == 'turn':
            self.turn_semaphore.release()
            self.straight_semaphore.acquire()
            print(f'Traffic light set to green for {direction} traffic.')

    def stop_traffic(self):
        self.stop_flag.set()

    def should_stop_traffic(self):
        return self.stop_flag.is_set()


class Road:
    def __init__(self, name, traffic_light):
        self.cars_on_cross = 0
        self.name = name
        self.traffic_light = traffic_light

    def enter_road(self, car, direction):
        print(f'{car.name} is approaching the road from direction {direction}.')

        if direction == 'straight':
            self.traffic_light.straight_semaphore.acquire()
        elif direction == 'turn':
            self.traffic_light.turn_semaphore.acquire()

        with self.traffic_light.intersection_semaphore:
            self.cars_on_cross += 1
            print(f'{car.name} enters the cross from direction {direction}. Traffic light is green. Cars on the road: {self.cars_on_cross}')

    def exit_road(self, car):
        time_spent_on_cross = random.uniform(1, 4)

        with self.traffic_light.intersection_semaphore:
            print(f'{car.name} is exiting the cross and will spend {time_spent_on_cross:.2f} seconds on the road.')

        time.sleep(time_spent_on_cross)

        with self.traffic_light.intersection_semaphore:
            self.cars_on_cross -= 1
            print(f'{car.name} has completely exited the road.')

            if self.cars_on_cross == 0:
                self.traffic_light.straight_semaphore.release()
                self.traffic_light.turn_semaphore.release()


class Car(threading.Thread):
    DIRECTIONS = ['straight', 'turn']

    def __init__(self, name, road):
        super().__init__()
        self.name = name
        self.road = road
        self.direction = random.choice(self.DIRECTIONS)

    def run(self):
        time.sleep(random.uniform(0, 1))

        if self.direction == 'straight':
            self.road.enter_road(self, 'straight')
            self.road.exit_road(self)
        elif self.direction == 'turn':
            self.road.enter_road(self, 'turn')
            self.road.exit_road(self)


def traffic_light_controller(traffic_light, straight_duration, turn_duration):
    while not traffic_light.should_stop_traffic():
        traffic_light.set_green_light('straight')
        print(f'Straight traffic green for {straight_duration} seconds.')
        time.sleep(straight_duration)

        if not traffic_light.should_stop_traffic():
            traffic_light.set_green_light('turn')
            print(f'Turn traffic green for {turn_duration} seconds.')
            time.sleep(turn_duration)


def user_interface():
    straight_duration = float(input("Enter the duration for straight traffic (seconds), or press Enter to randomize: ").strip() or random.uniform(5, 15))
    turn_duration = float(input("Enter the duration for turning traffic (seconds), or press Enter to randomize: ").strip() or random.uniform(5, 15))
    num_cars = int(input("Enter the number of cars, or press Enter to randomize: ").strip() or random.randint(5, 15))

    traffic_light = TrafficLight()
    road_straight = Road(name='Main Road', traffic_light=traffic_light)
    road_turn = Road(name='Side Road', traffic_light=traffic_light)

    traffic_light_controller_thread = threading.Thread(
        target=traffic_light_controller, args=(traffic_light, straight_duration, turn_duration)
    )
    traffic_light_controller_thread.start()

    cars = [Car(name=f'Car-{i}', road=random.choice([road_straight, road_turn])) for i in range(1, num_cars + 1)]

    for car in cars:
        car.start()

    for car in cars:
        car.join()

    traffic_light.stop_traffic()
    traffic_light_controller_thread.join()


if __name__ == "__main__":
    user_interface()
