__version__ = '0.0.1'

# Import numpy and scipy to ensure BLAS libs are loaded before creating the ThreadpoolController.
# This is basic setup copied from sklearn.
import numpy  # noqa
import scipy.linalg  # noqa
from threadpoolctl import ThreadpoolController

_threadpool_controller = ThreadpoolController()
