from distutils.core import setup
from Cython.Build import cythonize
import numpy

sourcefiles = ['Fifteen.pyx', 'BFS.pyx', 'DFS.pyx', 'Search_Algorithm.pyx', 'State.pyx']
include_dirs = [numpy.get_include()]
setup(ext_modules=cythonize(sourcefiles), include_dirs=include_dirs, requires=['Cython', 'numpy'], language_level=3)
