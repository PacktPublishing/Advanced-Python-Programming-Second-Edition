import numpy as np
from cevolve import c_evolve, c_evolve_openmp

class Particle:

    __slots__ = ('x', 'y', 'ang_speed')
    
    def __init__(self, x, y, ang_speed):
        self.x = x
        self.y = y
        self.ang_speed = ang_speed

class ParticleSimulator:

    def __init__(self, particles):
        self.particles = particles

    def evolve_cython(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        
        r_i = np.array([[p.x, p.y] for p in self.particles])        
        ang_speed_i = np.array([p.ang_speed for p in self.particles])

        c_evolve(r_i, ang_speed_i, timestep, nsteps)
        
        for i, p in enumerate(self.particles):
            p.x, p.y = r_i[i]

    def evolve_openmp(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        
        r_i = np.array([[p.x, p.y] for p in self.particles])        
        ang_speed_i = np.array([p.ang_speed for p in self.particles])

        c_evolve_openmp(r_i, ang_speed_i, timestep, nsteps)
        
        for i, p in enumerate(self.particles):
            p.x, p.y = r_i[i]
        
    def evolve_numpy(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        
        r_i = np.array([[p.x, p.y] for p in self.particles])        
        ang_speed_i = np.array([p.ang_speed for p in self.particles])
        
        v_i = np.empty_like(r_i)
        
        for i in range(nsteps):
            norm_i = np.sqrt((r_i ** 2).sum(axis=1))

            v_i = r_i[:, [1, 0]]
            v_i[:, 0] *= -1
            v_i /= norm_i[:, np.newaxis]                

            d_i = timestep * ang_speed_i[:, np.newaxis] * v_i

            r_i += d_i
        
        for i, p in enumerate(self.particles):
            p.x, p.y = r_i[i]

    def evolve_python(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        # First, change the loop order
        for p in self.particles:
            t_x_ang = timestep * p.ang_speed
            for i in range(nsteps):
                norm = (p.x**2 + p.y**2)**0.5
                p.x, p.y = p.x - t_x_ang*p.y/norm, p.y + t_x_ang * p.x/norm

from random import uniform

def benchmark(npart=100, method='python'):
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0)) 
                  for i in range(npart)]
    
    simulator = ParticleSimulator(particles)
    if method=='python':
        simulator.evolve_python(1.0)
        
    if method == 'cython':
        simulator.evolve_cython(10.0)

    if method == 'openmp':
        simulator.evolve_openmp(10.0)
        
    elif method == 'numpy':
        simulator.evolve_numpy(1.0)
