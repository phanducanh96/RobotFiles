import numpy
import math
import random
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../..')
import pyrosim
from robot import ROBOT

class INDIVIDUAL:
    def __init__(self, i):
        self.genome = numpy.random.random_sample((4, 8)) * 2 - 1
        self.fitness = 0
        self.ID = i
    def Evaluate(self, pb):
        sim = pyrosim.Simulator( play_paused=False , eval_time=1000, play_blind = pb )
        robot = ROBOT( sim , self.genome )
        sim.start()
#        sim.wait_to_finish()
#        sensorData = sim.get_sensor_data( sensor_id = robot.P4, svi = 1 )
#        self.fitness = sensorData[-1]
    def Mutate(self):
        geneToMutate = random.randint(0,3)
        geneToMutate2 = random.randint(0,7)
        
        temp = random.gauss( self.genome[geneToMutate][geneToMutate2], math.fabs(self.genome[geneToMutate][geneToMutate2]))
        if temp > 1:
            temp = 1
        if temp < -1:
            temp = -1
        self.genome[geneToMutate][geneToMutate2] = temp

    def Print(self):
        print('['),
        print(self.ID),
        print(self.fitness),
        print('] '),
    def Start_Evaluation(self, pb):
        self.sim = pyrosim.Simulator( play_paused=False , eval_time=1000, play_blind = pb)
        self.robot = ROBOT( self.sim , self.genome )
        self.sim.start()
    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        sensorData = self.sim.get_sensor_data( sensor_id = self.robot.P4, svi = 1 )
        self.fitness = sensorData[-1]
        del self.sim


