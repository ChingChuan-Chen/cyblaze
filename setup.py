#!/usr/bin/python
import os
import sys

import numpy as np
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


try:
  from Cython.Build import cythonize
  USE_CYTHON = True
except ImportError:
  USE_CYTHON = False


def get_openmp_flag():
  """
  Returns the flags for openmp.
  This function is copied from sklearn.
  """
  if sys.platform == "win32":
    return ["/openmp"]
  elif sys.platform == "darwin" and "openmp" in os.getenv("CPPFLAGS", ""):
    return []
  return ["-fopenmp"]


class BuildExtClass(build_ext):
  def build_extensions(self) -> None:
    DEFINE_MACRO_NUMPY_C_API = (
      'NPY_NO_DEPRECATED_API',
      'NPY_1_7_API_VERSION',
    )
    for ext in self.extensions:
      ext.define_macros.append(DEFINE_MACRO_NUMPY_C_API)

    for e in self.extensions:
      e.include_dirs += [np.get_include()]
      e.extra_compile_args += get_openmp_flag()
      e.extra_link_args += get_openmp_flag()

    build_ext.build_extensions(self)

  def run(self) -> None:
    self.run_command('build_clib')
    build_ext.run(self)


ext = '.pyx' if USE_CYTHON else '.cpp'
cyblaze_ext = [
  Extension(
    'cyblaze.conversions',
    sources=[f'cyblaze/conversions{ext}'],
  )
]

setup_args = dict(
  ext_modules=cythonize(cyblaze_ext) if USE_CYTHON else cyblaze_ext,
  cmdclass={'build_ext': BuildExtClass},
)

setup(**setup_args)
