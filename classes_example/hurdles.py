#!/usr/bin/env python3

import random
import time
class Hurdler:

    def __init__(self, name, height, speed=1, jump_accuracy=0.75):
        self.position = 0
        self.failed_hurdle = 0
        self.name = name
        self.height = height
        self.speed = speed
        self.jump_accuracy = jump_accuracy

    def run(self):
        self.position += self.speed
        print(f"{self.name} is at {self.position}")

    def jump(self):
        hurdle = random.random()
        if hurdle <= self.jump_accuracy:
            self.position += self.speed + 1
        else:
            self.position += (self.speed / 2)
            self.failed_hurdle += 1


def hundred_meter(hurdlers):

    furthest_position = 0
    while furthest_position <= 100:
        time.sleep(0.4)
        for hurdler in hurdlers:
            hurdler.run()
            hurdler.jump()
            if hurdler.position > furthest_position:
                furthest_position = hurdler.position
    for hurdler in hurdlers:
        print(f"{hurdler.name} is at {hurdler.position} and has missed {hurdler.failed_hurdle}")

    # while bolt.position < 100 and turbo.position < 100:  <----original info in loop.
    #     bolt.run()
    #     turbo.run()
    #     bolt.jump()
    #     turbo.jump()
    #     time.sleep(0.5)
    # print(f"{bolt.name} is at {bolt.position} and has missed {bolt.failed_hurdle}")
    # print(f"{turbo.name} is at {turbo.position} and has missed {turbo.failed_hurdle}")


bolt = Hurdler("Bolt", "6' 5\"", 2.5, 0.5)
turbo = Hurdler("Turbo", "0' 9\"", 2, 0.7)
steve = Hurdler("Steve", "5' 3\"", 2.25, 0.6)
racers = [bolt, turbo, steve]

hundred_meter(racers)