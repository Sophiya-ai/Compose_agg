class Engine():
    def start(self):
        print("egine start")
    def stop(self):
        print("engine stopped")
class Car():
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()
my_Car = Car()
my_Car.start()
my_Car.stop()