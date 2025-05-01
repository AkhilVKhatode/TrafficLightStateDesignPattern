from abc import ABC, abstractmethod

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def next(self, context):
        pass

    @abstractmethod
    def get_color(self):
        pass


# Concrete State: Red
class RedState(TrafficLightState):
    def next(self, context):
        print("Switching from RED to GREEN after some timer. Cars go!")
        context.set_state(GreenState())

    def get_color(self):
        return "RED"


# Concrete State: Green
class GreenState(TrafficLightState):
    def next(self, context):
        print("Switching from GREEN to YELLOW after some timer. Slow down!")
        context.set_state(YellowState())

    def get_color(self):
        return "GREEN"


# Concrete State: Yellow
class YellowState(TrafficLightState):
    def next(self, context):
        print("Switching from YELLOW to RED after some timer. Stop!")
        context.set_state(RedState())

    def get_color(self):
        return "YELLOW"


# Concrete State: Blinking
class BlinkingState(TrafficLightState):
    def next(self, context):
        print("Switching from BLINKING to MAINTENANCE mode...")
        context.set_state(MaintenanceState())

    def get_color(self):
        return "BLINKING"


# Concrete State: Maintenance
class MaintenanceState(TrafficLightState):
    def next(self, context):
        print("Maintenance done, back to RED!")
        context.set_state(RedState())

    def get_color(self):
        return "MAINTENANCE"


# Context Class
class TrafficLightContext:
    def __init__(self):
        self.current_state = RedState()  # Start with RED

    def set_state(self, state):
        self.current_state = state

    def next(self):
        self.current_state.next(self)

    def get_color(self):
        return self.current_state.get_color()


# Driver Class
if __name__ == "__main__":
    traffic_light = TrafficLightContext()
    print(traffic_light.get_color())  # RED
    traffic_light.next()  # RED -> GREEN
    print(traffic_light.get_color())  # GREEN
    traffic_light.next()  # GREEN -> YELLOW
    print(traffic_light.get_color())  # YELLOW
    traffic_light.next()  # YELLOW -> RED
    print(traffic_light.get_color())  # RED
    traffic_light.next()  # RED -> GREEN
    print(traffic_light.get_color())  # GREEN
    # Adding new states like BLINKING or MAINTENANCE is easy now
