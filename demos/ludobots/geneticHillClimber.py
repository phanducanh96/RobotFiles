from population import POPULATION
import copy
import constants as c
from environments import ENVIRONMENTS

envs = ENVIRONMENTS()

parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, False, True, c.evalTime)
parents.Print()
for g in range(1, c.numGens):
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, False, True, c.evalTime)
#    children.Print()
#    children = copy.deepcopy(parents)
#    children.Mutate()
#    children.Evaluate(True)
    parents.ReplaceWith(children)
    print(g),
    children.Print()
#for e in range(0, c.numEnvs):

#parents.p[0].Start_Evaluation(envs.envs[3], True, False, c.evalTime)
#parents.p[0].Start_Evaluation(envs.envs[2], True, False, c.evalTime)
#parents.p[0].Start_Evaluation(envs.envs[1], True, False, c.evalTime)
parents.p[0].Start_Evaluation(envs.envs[0], True, False, c.evalTime)





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


