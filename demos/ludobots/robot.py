import constants as c
import random
class ROBOT:
    def __init__(self,sim,wts):
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)

    def send_objects(self, sim):
#        self.whiteObject = sim.send_cylinder( x=0 ,y=0 , z=0.6 , length=1.0 , radius=0.1)
#        self.redObject = sim.send_cylinder( x=0 , y=0.5 , z=1.1, r=1, g=0, b=0, r1=0, r2=1, r3=0 )
        self.O0 = sim.send_box(x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2 * c.R, r=0.5, g=0.5, b=0.5)
        self.O1 = sim.send_cylinder(x=0, y=c.L, z=c.L + c.R, length=c.L, radius =c.R, r=1, g=0, b=0, r1=0, r2=1, r3=0)
        self.O2 = sim.send_cylinder(x=c.L, y=0, z=c.L + c.R, length=c.L, radius=c.R, r=0, g=1, b=0, r1=1, r2=0, r3=0)
        self.O3 = sim.send_cylinder(x=0, y= -c.L, z=c.L + c.R, length=c.L,radius=c.R, r=0, g=0, b=1, r1=0, r2=1, r3=0)
        self.O4 = sim.send_cylinder(x=-c.L, y=0, z=c.L + c.R, length=c.L, radius=c.R, r=1, g=0, b=1, r1=1, r2=0, r3=0)
        self.O5 = sim.send_cylinder(x=0, y=1.5*c.L, z=c.L - 1.5*c.R, length=c.L, radius=c.R, r=1, g=0, b=0)
        self.O6 = sim.send_cylinder(x=1.5*c.L, y=0, z=c.L - 1.5*c.R, length=c.L, radius=c.R, r=0, g=1, b=0)
        self.O7 = sim.send_cylinder(x=0, y=-1.5*c.L, z=c.L - 1.5*c.R, length=c.L, radius=c.R, r=0, g=0, b=1)
        self.O8 = sim.send_cylinder(x=-1.5*c.L, y=0, z=c.L - 1.5*c.R, length=c.L, radius=c.R, r=1, g=0, b=1)

        self.O = {}
        self.O[0] = self.O0
        self.O[1] = self.O1
        self.O[2] = self.O2
        self.O[3] = self.O3
        self.O[4] = self.O4
        self.O[5] = self.O5
        self.O[6] = self.O6
        self.O[7] = self.O7
        self.O[8] = self.O8
    def send_joints(self, sim):
        self.J0 = sim.send_hinge_joint( first_body_id = self.O0 , second_body_id = self.O1, x=0, y=c.L/2, z=c.L + c.R, n1=-1, n2=0, n3=0, lo=-3.14159/2 , hi=3.14159/2)
        self.J1 = sim.send_hinge_joint( first_body_id = self.O1, second_body_id = self.O5, x=0, y=1.5*c.L, z=c.L + c.R, n1=-1, n2=0, n3=0, lo=-3.14159/2 , hi=3.14159/2)
        self.J2 = sim.send_hinge_joint( first_body_id = self.O0, second_body_id = self.O2, x=c.L/2, y=0, z=c.L + c.R, n1=0, n2=1, n3=0, lo=-3.14159/2 , hi=3.14159/2)
        self.J3 = sim.send_hinge_joint( first_body_id = self.O2, second_body_id = self.O6, x=1.5*c.L, y=0, z=c.L + c.R, n1=0, n2=1, n3=0, lo=-3.14159/2 , hi=3.14159/2)
        self.J4 = sim.send_hinge_joint( first_body_id = self.O0, second_body_id = self.O3, x=0, y=-c.L/2, z=c.L + c.R, n1=1, n2=0, n3=0, lo=-3.14159/2 , hi=3.14159/2)
        self.J5 = sim.send_hinge_joint( first_body_id = self.O3, second_body_id = self.O7, x=0, y=-1.5*c.L, z=c.L + c.R, n1=1, n2=0, n3=0, lo=-3.14159/2 , hi=3.14159/2)
        self.J6 = sim.send_hinge_joint( first_body_id = self.O0, second_body_id = self.O4, x=-c.L/2, y=0, z=c.L + c.R, n1=0, n2=-1, n3=0, lo=-3.14159/2 , hi=3.14159/2)
        self.J7 = sim.send_hinge_joint( first_body_id = self.O4, second_body_id = self.O8, x=-1.5*c.L, y=0, z=c.L + c.R, n1=0, n2=-1, n3=0, lo=-3.14159/2 , hi=3.14159/2)

        self.J = {}
        self.J[0] = self.J0
        self.J[1] = self.J1
        self.J[2] = self.J2
        self.J[3] = self.J3
        self.J[4] = self.J4
        self.J[5] = self.J5
        self.J[6] = self.J6
        self.J[7] = self.J7

    def send_sensors(self, sim):
        self.T0 = sim.send_touch_sensor( body_id = self.O5 )
        self.T1 = sim.send_touch_sensor( body_id = self.O6 )
        self.T2 = sim.send_touch_sensor( body_id = self.O7 )
        self.T3 = sim.send_touch_sensor( body_id = self.O8 )
        self.L4 = sim.send_light_sensor( body_id = self.O0 )

        self.S = {}
        self.S[0] = self.T0
        self.S[1] = self.T1
        self.S[2] = self.T2
        self.S[3] = self.T3
        self.S[4] = self.L4
#        self.P2 = sim.send_proprioceptive_sensor( joint_id = self.joint )
#        self.R3 = sim.send_ray_sensor( body_id = self.redObject , x = 0 , y = 1.1 , z = 1.1 , r1 = 0 , r2 = 1, r3 = 0)
        #R3 = sim.send_ray_sensor( body_id = redObject , x = 0 , y = 0.5 , z = 1.0 , r1 = 0, r2 = 0, r3 = -1)
    def send_neurons(self, sim):
        self.SN = {}
        self.MN = {}
        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])

        for j in self.J:
            self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j], tau = 0.3)
        
#        self.SN0 = sim.send_sensor_neuron( sensor_id = self.T0 )
#        self.SN1 = sim.send_sensor_neuron( sensor_id = self.T1 )
#        self.SN2 = sim.send_sensor_neuron( sensor_id = self.P2 )
#        self.SN3 = sim.send_sensor_neuron( sensor_id = self.R3 )
#
#        self.sensorNeurons = {}
#        self.sensorNeurons[0] = self.SN0
#        self.sensorNeurons[1] = self.SN1
#        self.sensorNeurons[2] = self.SN2
#        self.sensorNeurons[3] = self.SN3
#
#        self.MN2 = sim.send_motor_neuron( joint_id = self.joint )
#        self.motorNeurons = {}
#        self.motorNeurons[0] = self.MN2
    def send_synapses(self, sim, wts):

#        for sn in self.SN:
#            firstMN = min(self.MN, key=self.MN.get)
#            sim.send_synapse(source_neuron_id = self.SN[sn] , target_neuron_id = self.MN[firstMN] , weight = random.random()*2 - 1 )
#        for s in self.sensorNeurons:
#            for m in self.motorNeurons:
#                sim.send_synapse( source_neuron_id = self.sensorNeurons[s] , target_neuron_id = self.motorNeurons[m] , weight = wts[s] )
        for j in self.SN:
            for i in self.MN:
                sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id = self.MN[i], weight = wts[j,i])

#sim.send_synapse( source_neuron_id = SN0 , target_neuron_id = MN2 , weight = -1.0 )



