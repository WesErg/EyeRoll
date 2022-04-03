import unittest
from eyeroll.math import transform as tx
import numpy as np


class TestMathTransform(unittest.TestCase):

    def test_r_matrix(self):
        """
        Simple test to just verify shape.
        """
        Rs = tx.rotation_matrix(eulers=np.array([[0, 0, 0], [45, 0, 45]]))
        self.assertEqual((2, 3, 3), Rs.shape)

    def test_html(self):
        Rs = tx.rotation_matrix(eulers=np.array([[0, 0, 0], [45, 0, 45]]))
        dv = np.array(2 * [[[0], [0], [1]]])
        print(Rs.shape, dv.shape)
        Ts = tx.htm(Rs, dv)
        self.assertEqual((2, 4, 4), Ts.shape)
