from distutils.core import setup
from Cython.Build import cythonize
setup(
    name='getlicense',
    ext_modules=cythonize('license-decoding.py')
)