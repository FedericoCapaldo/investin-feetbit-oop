# FeetBit program
import time
from datetime import datetime

class Utilities:
    def sleep_now(self):
        time.sleep(12)

class FeetBit:
    # what happens at 'object initialize'
    def __init__(self):
        self.steps = 0

    def get_current_time(self):
        return datetime.now().time()

    def get_current_day(self):
        days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        return "Today is " + days_of_the_week[datetime.today().weekday()]

    def get_steps(self):
        return self.steps

    def record_new_steps(self, new_steps):
        self.steps = self.steps + new_steps



# ENTRY POINT OF OUR PROGRAM
if __name__ == "__main__":
    utils = Utilities()
    print("we are runnning the main program")

    feet_bit_object = FeetBit() # this is 'object initialize'

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
