from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["Cython1.py",
                            "Cython2.py",
                            "Cython3.py",
                            "Cython4.py",
                                ])
)
