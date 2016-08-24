#Simulacion de un proceso en un procesador
#@authors: Rafael Leon 13361, Pablo Lopez 14509
#@version: 0.1
#@date: 24/8/2016
#Test
import simpy as sp
import random as rnd

class proceso(object):
	def __init__(self,env)
		cpu= sp.Resource(env, capacity=1)
		ram= sp.Container(env, capacity=100)
