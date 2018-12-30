#!/usr/bin/env python
import time
import os
class counter(object):
    def __init__(self, max):
        self.max = int(max)
        self.time = 0
        self.countArray = []
    def count(self):
        if (self.max > 1000000):
            print(self.max)
            print("The counter can only count to 1 million!")
            exit(1)
        else:
            try:
                for number in range(1, (self.max+1)):
                    self.countArray.append(number)
                    os.system("say " + str(number) + " sheep")
                    print(str(number) + " sheep")
                    if (number <= 10):
                        self.time = self.time + 0.10
                        time.sleep(self.time)
                    elif (number <= 100):
                        self.time = self.time + 0.010
                        time.sleep(self.time)
                    elif (number <= 1000):
                        self.time = self.time + 0.0010
                        time.sleep(self.time)
            except (KeyboardInterrupt):
                print("Counter Stopped at: " + str(self.countArray[-1]))
                exit(1)

newCounter = counter("10000")
newCounter.count()
