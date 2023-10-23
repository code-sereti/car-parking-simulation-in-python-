import random, math
import numpy as np
import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
import SimPy.Simulation as Sim
class Arrival(Sim.Process):
   """ Source generates cars at random
Arrivals are at a time-dependent rate
"""
   def generate(self):
       i=0
       while (self.sim.now() < G.maxTime):
           tnow = self.sim.now()
           arrivalrate = 100 + 10 * math.sin(math.pi * tnow/12.0)
           t = random.expovariate(arrivalrate)
           yield Sim.hold, self, t
           c = Car(name="Car%02d" % (i), sim=self.sim)
           timeParking = random.expovariate(1.0/G.parkingtime)
           self.sim.activate(c, c.visit(timeParking))
           i += 1

        
           
