from simul import Particle, ParticleSimulator
from random import uniform


def close(particles, eps=1e-5):
    p0, p1 = particles

    x_dist = abs(p0.x - p1.x)
    y_dist = abs(p0.y - p1.y)

    return x_dist < eps and y_dist < eps


def benchmark():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for i in range(2)
    ]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

    print(close(particles))
