import time
import os
import math

from .simulation import Simulation
from .pattern import Cell

class GameView:
    def __init__(self, simulation: Simulation, width: int = 50, height: int = 25):
        if width < 4 or height < 4:
            raise ValueError('too smal view')

        self.simulation = simulation
        self.width = width
        self.height = height
        self.xOffset = math.floor(self.width / 2)
        self.yOffset = math.floor(self.height / 2)

        self.generation_number = 1

    def _draw(self):
        os.system('cls')
        for i in range(self.height):
            # print field
            for j in range(self.width):
                if Cell(j - self.xOffset, self.yOffset - i) in self.simulation.pattern.cells:
                    print('#', end='')
                else:
                    print('.', end='')
            # print status
            if i == 3:
                print(f'\t\t Alive cells = {len(self.simulation.pattern.cells)} Generation number = {self.generation_number}', end='')
            print()

    def start(self, gens_per_second:int = 10):
        timer_last = time.perf_counter() # init timer
        while True:
            # calculate elapsed time
            if time.perf_counter() - timer_last < (1./gens_per_second):
                continue
            timer_last = time.perf_counter()

            self._draw()

            self.simulation.make_step()
            self.generation_number += 1

    def start_step_by_step(self):
        while True:
            self._draw()
            self.simulation.make_step()
            self.generation_number += 1
            input('press enter')
