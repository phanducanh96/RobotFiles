from robot import ROBOT
import random
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../..')
import pyrosim

for i in range(0,10):
    sim = pyrosim.Simulator( play_paused=True , eval_time=1000 )
    #sim.send_cylinder( x=0 , y=0 , z=0.6 , length=1.0 , radius=0.1 )
    robot = ROBOT( sim, random.random()*2 - 1 )

    sim.start()
    sim.wait_to_finish()
#sensorData = sim.get_sensor_data( sensor_id = MN2 )
#print(sensorData)
#f = plt.figure()
#panel = f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(-2, +2)
#plt.show()


