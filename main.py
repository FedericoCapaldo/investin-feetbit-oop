# FeetBit program
import time
from datetime import datetime
import random

class Utilities:
    def sleep_now(self):
        time.sleep(0)

# 1. create class Watch
class Watch:
    def __init__(self):
        self.watch = datetime

    def get_current_time(self):
        return self.watch.now().time()

    def get_current_day(self):
        days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        return "Today is " + days_of_the_week[self.watch.today().weekday()]


# 2. create class Step Counter
class StepCounter():
    def __init__(self):
        self.steps = 0

    def get_steps(self):
        return self.steps

    def record_new_steps(self, new_steps):
        self.steps = self.steps + new_steps

# 3. create class Weather

class FeetBit:
    # what happens at 'object initialize'
    def __init__(self, watch, my_step_counter):
        self.step_counter = my_step_counter
        self.watch = watch
        self.weather = self.update_weather()

    def get_current_time(self):
        return self.watch.get_current_time()

    def get_current_day(self):
        return self.watch.get_current_day()

    def get_steps(self):
        return self.step_counter.get_steps()

    def record_new_steps(self, new_steps):
        self.step_counter.record_new_steps(new_steps)

    def update_weather(self):
        # simulating weather forecast
        possible_weather_conditions = ["Sunny", "Cloudy", "Windy", "Rainy", "Snowy"]
        return possible_weather_conditions[random.randint(0, 4)]

    def get_weather(self):
        return self.weather


# ENTRY POINT OF OUR PROGRAM
if __name__ == "__main__":
    utils = Utilities()
    print("we are runnning the main program")

    # 4. when creating the feetbit object, also pass these new objects to it
    watch_object = Watch()
    step_counter_objet = StepCounter()

    feet_bit_object = FeetBit(watch_object, step_counter_objet) # this is 'object initialize'

    utils.sleep_now()
    print("printing time from feetbit:")
    utils.sleep_now()
    print(feet_bit_object.get_current_time())

    utils.sleep_now()
    print("printing day of the week:")
    utils.sleep_now()
    print(feet_bit_object.get_current_day())


    utils.sleep_now()
    print("current steps ->", feet_bit_object.get_steps())

    utils.sleep_now()
    print("adding more steps to fitbit")
    feet_bit_object.record_new_steps(5)
    feet_bit_object.record_new_steps(5)

    utils.sleep_now()
    print("current steps ->", feet_bit_object.get_steps())


    utils.sleep_now()
    print("printing time from feetbit")
    utils.sleep_now()
    print(feet_bit_object.get_current_time())

    utils.sleep_now()
    print("what's the weather like?")
    utils.sleep_now()
    print(feet_bit_object.get_weather())
