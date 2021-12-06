from gameoflife import *
from gameoflife.gameview import GameView


'''
TODO: 
graphical output
realtime interactions with simulation

*maybe port to java or c# for better performance
'''

simulation = Simulation()
#simulation.add_pattern(patterns.glider, Point(0, 5))
#simulation.add_pattern(patterns.block, Point(5, -5))
#simulation.add_pattern(patterns.blinker, Point(5, 0))

simulation.add_pattern(patterns.acorn)

view = GameView(simulation)
view.start(10)
#view.start_step_by_step()