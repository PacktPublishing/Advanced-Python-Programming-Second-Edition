from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

hello_parallel = Extension('hello_parallel',
                           ['hello_parallel.pyx'],
                           extra_compile_args=['-fopenmp'],
                           extra_link_args=['-fopenmp'])
cevolve = Extension('cevolve',
                    ['cevolve.pyx'],
                    extra_compile_args=['-fopenmp'],
                    extra_link_args=['-fopenmp'])
setup(
   name='Hello',
   ext_modules = cythonize([cevolve, hello_parallel]),
)
