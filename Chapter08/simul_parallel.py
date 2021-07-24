from IPython.parallel import Client
from random import uniform
from simul import Particle


def scatter_gather(nparticles):
    particles = [Particle(uniform(-1.0, 1.0), 
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0)) for i in range(nparticles)]
    
    rc = Client()
    dview = rc[:]
    
    dview.scatter('particle_chunk', particles).get()

    dview.execute('from simul import ParticleSimulator')
    dview.execute('simulator = ParticleSimulator(particle_chunk)')
    dview.execute('simulator.evolve_cython(0.1)')
    
    particles = dview.gather('particle_chunk', block=True)

