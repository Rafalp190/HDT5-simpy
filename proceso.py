# -*- coding: cp1252 -*-
#Simulacion de un proceso en un procesador
#@authors: Rafael Leon 13361, Pablo Lopez 14509
#@version: 0.1
#@date: 24/8/2016
import simpy as sp
import random as rnd
RANDOM_SEED = 32

class proceso(object):
	def __init__(self,env,id)
		self.cpu= sp.Resource(env, capacity=1)
		self.ram= sp.Container(env, init= 100, capacity=100)
		self.io = sp.Resource(env, capacity=1)
