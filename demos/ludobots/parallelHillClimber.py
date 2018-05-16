from population import POPULATION
#from robot import ROBOT
#from individual import INDIVIDUAL
#import pickle
import copy
#import random
#import matplotlib.pyplot as plt
#import sys
#sys.path.insert(0, '../..')
#import pyrosim
parents = POPULATION(10)
parents.Evaluate(True)
parents.Print()
for g in range(1, 200):
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate(True)
    parents.ReplaceWith(children)
    print(g),
    parents.Print()
parents.Evaluate(False)




#parent = INDIVIDUAL()
#parent.Evaluate(True)
#print(parent.fitness)
#
#for i in range(0,100):
#    child = copy.deepcopy( parent )
#    child.Mutate()
#    child.Evaluate(True)
#    print"[g:",  i, "]", "[pw:", parent.genome, "]", "[p:", parent.fitness , "]", "[c:", child.fitness , "]"
#    if ( child.fitness > parent.fitness ):
#        child.Evaluate(True)
#        parent = child


#        f = open('robot.p','w')
#        pickle.dump(parent , f )
#        f.close()


#sensorData = sim.get_sensor_data( sensor_id = MN2 )
#print(sensorData)
#f = plt.figure()
#panel = f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(-2, +2)
#plt.show()


