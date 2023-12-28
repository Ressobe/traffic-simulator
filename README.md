The program simulates traffic at an intersection. Here is a general overview of its functionality:

1. **Initialization:**
   - The user provides (or random values are generated for) parameters such as the duration of green lights for straight and turning traffic and the number of cars.
   - Objects for traffic lights (`TrafficLight`), roads (`Road`), and car threads (`Car`) are created.

2. **Vehicle Traffic Simulation:**
   - A thread is created for each car, simulating the time it takes to reach the intersection and deciding whether the car moves straight or turns.
   - Cars enter roads, acquire traffic-related semaphores, increase car counters on roads, and leave the intersection after a certain time.

3. **Traffic Light Controller:**
   - In a separate thread, the traffic light controller operates in an infinite loop, changing lights for straight and turning traffic.
   - The controller releases and acquires the relevant semaphores, thereby controlling which direction has the current green light.

4. **Simulation Termination:**
   - Cars finish their threads.
   - An event is set to inform the traffic light controller that traffic should be stopped.
   - We wait for the controller to finish its work.

The program focuses on thread synchronization and simulating changing traffic conditions at an intersection. The use of semaphores and events allows control over access to shared resources, ensuring safe conditions for parallel thread execution. It stops traffic and waits for the traffic light controller thread to finish.

### Class `TrafficLight`:
- **Method `__init__(self)`**: Initializes the traffic light object, creating semaphores (`straight_semaphore` and `turn_semaphore`) and an event (`stop_flag`) for thread synchronization.
- **Method `set_green_light(self, direction)`**: Sets the green light for a specific traffic direction, releasing the appropriate semaphore to indicate which direction currently has the green light.
- **Method `stop_traffic(self)`**: Sets the `stop_flag` event, signaling that traffic should be stopped.
- **Method `should_stop_traffic(self)`**: Checks if the `stop_flag` event is set, indicating that traffic should be stopped.

### Class `Road`:
- **Method `__init__(self, name, traffic_light)`**: Initializes the road object, taking the road's name and the associated traffic light object.
- **Method `enter_road(self, car, direction)`**: Handles a car entering the road. Acquiring the semaphore related to the traffic direction indicates that the car can enter the road. The car counter on the road is increased, and information is printed to the console.
- **Method `exit_road(self, car)`**: Handles a car leaving the road. The car spends some time on the road (simulating traffic) before exiting. The car counter on the road is updated, and information is printed to the console.

### Class `Car`:
- **Attribute `DIRECTIONS`**: A list containing available traffic directions.
- **Method `__init__(self, name, road)`**: Initializes the car object, taking the car's name and the road object it travels on.
- **Method `run(self)`**: Thread method simulating car behavior. The car waits for some time (simulating travel time), then enters and exits the road.

### Function `traffic_light_controller`:
- **Arguments: `traffic_light`, `straight_duration`, `turn_duration`**: Traffic light controller function. In an infinite loop, it changes lights on the traffic signal, simulating traffic.

### Function `user_interface`:
- Takes user input or generates random values for traffic light durations and the number of cars.
- Creates a traffic light object and two roads (for straight and turning traffic).
- Creates a thread for the traffic light controller.
- Creates and starts threads for a specified number of cars.
- Waits for car threads to finish.
