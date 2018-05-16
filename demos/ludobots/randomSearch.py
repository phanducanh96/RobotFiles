from robot import ROBOT
from individual import INDIVIDUAL
import random
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../..')
import pyrosim

for i in range(0,10):
    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)

#sensorData = sim.get_sensor_data( sensor_id = MN2 )
#print(sensorData)
#f = plt.figure()
#panel = f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(-2, +2)
#plt.show()


