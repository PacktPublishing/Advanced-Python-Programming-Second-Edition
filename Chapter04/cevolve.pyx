import numpy as np
cimport cython
from libc.math cimport sqrt

#@cython.boundscheck(False)
#@cython.cdivision(True)
def c_evolve(double[:, :] r_i,double[:] ang_speed_i,
             double timestep,int nsteps):
    cdef int i
    cdef int j
    cdef int nparticles = r_i.shape[0]
    cdef double norm, x, y, vx, vy, dx, dy, ang_speed


    for i in range(nsteps):
        for j in range(nparticles):
            x = r_i[j, 0]
            y = r_i[j, 1]
            ang_speed = ang_speed_i[j]

            norm = sqrt(x ** 2 + y ** 2)

            vx = (-y)/norm
            vy = x/norm

            dx = timestep * ang_speed * vx
            dy = timestep * ang_speed * vy

            r_i[j, 0] += dx
            r_i[j, 1] += dy

# Untyped version
# def c_evolve(r_i, ang_speed_i, timestep, nsteps):
#     v_i = np.empty_like(r_i)

#     for i in range(nsteps):
#         norm_i = np.sqrt((r_i ** 2).sum(axis=1))
#         v_i = r_i[:, [1, 0]]
#         v_i[:, 0] *= -1
#         v_i /= norm_i[:, np.newaxis]

#         d_i = timestep * ang_speed_i[:, np.newaxis] * v_i

#         r_i += d_i
