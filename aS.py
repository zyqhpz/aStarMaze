# import class from pymaze.py
from pymaze import *

m = maze(5, 5)
m.CreateMaze(loadMaze='astarDemo.csv')

m.run()