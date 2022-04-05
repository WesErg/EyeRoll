import scipy as sp
import numpy as np
np.set_printoptions(precision=1, suppress=True)
from scipy.spatial.transform import Rotation


def htm(rm, dv):
    """
    Function to turn rotation matrix and displacement vector
    into a homogenous transformation matrix.  Handles a list
    or a list of rotation and displacement vectors.

    To move a point p_new = T x homogenous coordinate (4).
       Given this order of multimplication:
       1. Rotation ... then
       2. displacement

    """
    assert len(rm.shape) == len(dv.shape), f"Dimensions must match d(rm)={len(rm.shape)} but d(dv)={len(dv.shape)}"
    wrm, wdv = rm, dv
    if len(rm.shape) == 2:
        wrm, wdv = np.array([rm]), np.array([dv])
    M34 = np.concatenate([wrm, wdv], axis=2)
    M44 = np.concatenate([M34, np.array(rm.shape[0] * [[[0, 0, 0, 1]]])], axis=1)
    if len(rm.shape) == 2:
        M44 = M44[0]
    return M44


def rotation_matrix(eulers):
    """
    Returns a rotation matrix (or matrices) from Euler angles
    (or a list/array of Euler angles).
    """
    R01 = Rotation.from_euler('xyz', eulers, degrees=True)
    T01 = R01.as_matrix()
    return T01
