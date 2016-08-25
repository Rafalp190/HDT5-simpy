#Ejemplo DCPlayer
import random
import simpy

class ProcesosDeComputadora:

    def _init_(self, env, num):
        self.memoria = simpy.Container(env, init = 100, capacity = 100)
        self.cpu     = simpy.Resource(env, capacity = 1)
        self.IO      = simpy.Resource(env, capacity = 1)

    def MemoryRAM(env):
        # New: otorgarle memoria de 1-10 al proceso
        mem = random.randint(1,10)

        with ProcesosDeComputadora.memoria.get(mem) as req:
            yield req


        # Ready: instrucciones es random de 1-10
        instrucciones = random.randint(1,10)
        return instrucciones

    def CentralProcess(instrucciones):
        with ProcesosDeComputadora.cpu.request() as req:
            yield req

            instrucciones = instrucciones - 3
            env.timeout(1)
            if instrucciones <=0:
                print 'Proceso %d terminado' %num
                ProcesosDeComputadora.memoria.put(mem)
            else:
                resultado = random.randint(1,2)
                if resultado == 1:
                    CentralProcess(instrucciones)
                else:
                    Waiting()

    def Waiting(instrucciones):
        with ProcesosDeComputadora.IO.request() as req:
            yield req
        
