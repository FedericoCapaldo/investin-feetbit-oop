# FeetBit program

# steps
# time
#

import datetime
import time

class StepCounter:

    def __init__(self):
        self._steps = 0

    def get_steps(self):
        return self._steps

    def record_steps(self, number_of_steps):
        print(f'recording some steps... ({number_of_steps})')
        self._steps += number_of_steps



class Watch:
    import datetime
    # what happens when we create an object of this blueprint
    def __init__(self):
        self.watch = datetime.datetime

    def gimme_time(self):
        return self.watch.now().time()


class FeetBit:

    def gimme_time(self):
        return datetime.datetime.now().time()


def sleep_now():
    time.sleep(5)


if __name__ == "__main__":
    print("we are runnning the main program")

    feet_bit_object = FeetBit()
    print("printing time from feetbit")
    sleep_now()
    print(feet_bit_object.gimme_time())


    spo = StepCounter()
    sleep_now()
    print("this is the step count ->", spo.get_steps())
    new_steps_to_record = 5
    spo.record_steps(new_steps_to_record)
    spo.record_steps(new_steps_to_record)
    sleep_now()
    print("this is the step count ->", spo.get_steps())

    watch_object = Watch()
    sleep_now()
    print(watch_object.gimme_time())
