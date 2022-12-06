"""
This test suite (a module) runs tests for auto_diff_math of the
autodiff package.
"""

import pytest
import math
import numpy as np

# import names to test
from autodiff.utils.auto_diff_math import *


class TestAutoDiffMath:
    """Test class for dual number types"""

    def test_sin(self):
        z1 = DualNumber(np.pi / 4)
        z2 = np.pi / 4

        assert sin(z1).real == math.sin(np.pi / 4)
        assert sin(z1).dual == math.cos(np.pi / 4)

        assert sin(z2).real == math.sin(np.pi / 4)
        assert sin(z2).dual == 0

        with pytest.raises(TypeError):
            sin("string")

    def test_cos(self):
        z1 = DualNumber(np.pi)
        z2 = np.pi

        assert cos(z1).real == math.cos(np.pi)
        assert cos(z1).dual == -math.sin(np.pi)

        assert cos(z2).real == math.cos(np.pi)
        assert cos(z2).dual == 0

        with pytest.raises(TypeError):
            cos("string")

    def test_tan(self):
        z1 = DualNumber(np.pi)
        z2 = np.pi

        assert tan(z1).real == math.tan(np.pi)
        assert tan(z1).dual == 1 / math.cos(np.pi)**2

        assert tan(z2).real == math.tan(np.pi)
        assert tan(z2).dual == 0

        with pytest.raises(TypeError):
            tan("string")

    def test_exp(self):
        z1 = DualNumber(1)
        z2 = 1

        assert exp(z1).real == np.e
        assert exp(z1).dual == np.e

        assert exp(z2).real == np.e
        assert exp(z2).dual == 0

        with pytest.raises(TypeError):
            exp("string")

    def test_log(self):
        z1 = DualNumber(5)
        z2 = 5

        assert log(z1).real == np.log(5)
        assert log(z1).dual == 1 / 5

        assert log(z2).real == np.log(5)
        assert log(z2).dual == 0

        with pytest.raises(TypeError):
            log("string")

    def test_sinh(self):
        z1 = DualNumber(5)
        z2 = 5

        assert sinh(z1).real == pytest.approx(np.sinh(5))
        assert sinh(z1).dual == pytest.approx(np.cosh(5))

        assert sinh(z2).real == pytest.approx(np.sinh(5))
        assert sinh(z2).dual == 0

        with pytest.raises(TypeError):
            sinh("string")

    def test_cosh(self):
        z1 = DualNumber(5)
        z2 = 5

        assert cosh(z1).real == pytest.approx(np.cosh(5))
        assert cosh(z1).dual == pytest.approx(np.sinh(5))

        assert cosh(z2).real == pytest.approx(np.cosh(5))
        assert cosh(z2).dual == 0

        with pytest.raises(TypeError):
            cosh("string")

    def test_tanh(self):
        z1 = DualNumber(0)
        z2 = 0

        assert tanh(z1).real == np.tanh(0)
        assert tanh(z1).dual == 1 - np.tanh(0)**2

        assert tanh(z2).real == np.tanh(0)
        assert tanh(z2).dual == 0

        with pytest.raises(TypeError):
            tanh("string")

    def test_asin(self):
        z1 = DualNumber(0.5)
        z2 = 0.5

        assert asin(z1).real == math.asin(0.5)
        assert asin(z1).dual == 1 / np.sqrt(1 - 0.5**2)

        assert asin(z2).real == math.asin(0.5)
        assert asin(z2).dual == 0

        with pytest.raises(TypeError):
            asin("string")

    def test_acos(self):
        z1 = DualNumber(0.5)
        z2 = 0.5

        assert acos(z1).real == math.acos(0.5)
        assert acos(z1).dual == -1 / np.sqrt(1 - 0.5**2)

        assert acos(z2).real == math.acos(0.5)
        assert acos(z2).dual == 0

        with pytest.raises(TypeError):
            acos("string")

    def test_atan(self):
        z1 = DualNumber(0.5)
        z2 = 0.5

        assert atan(z1).real == math.atan(0.5)
        assert atan(z1).dual == 1 / (1 + 0.5**2)

        assert atan(z2).real == math.atan(0.5)
        assert atan(z2).dual == 0

        with pytest.raises(TypeError):
            atan("string")

    def test_log_b():
        z1 = DualNumber(4)
        z2 = 4

        assert log_b(z1, 2).real == 2
        assert log_b(z1, 2).dual == 1 / (4 * np.log(2))

        assert log_b(z2, 2).real == 2
        assert log_b(z2, 2).dual == 0

        with pytest.raises(TypeError):
            log_b("string", 2)

    def test_exp_b():
        z1 = DualNumber(2)
        z2 = 2

        assert exp_b(z1, 2).real == 4
        assert exp_b(z1, 2).dual == 4 * np.log(2)

        assert exp_b(z2, 2).real == 4
        assert exp_b(z2, 2).dual == 0

        with pytest.raises(TypeError):
            exp_b("string", 2)

    def test_sqrt():
        z1 = DualNumber(4)
        z2 = 4

        assert sqrt(z1).real == 2
        assert sqrt(z1).dual == 1 / (2 * np.sqrt(4))

        assert sqrt(z2).real == 2
        assert sqrt(z2).dual == 0

        with pytest.raises(TypeError):
            sqrt("string")

    def test_logistic():
        z1 = DualNumber(0)
        z2 = 0

        assert logistic(z1).real == 0.5
        assert logistic(z1).dual == 0.25

        assert logistic(z2).real == 0.5
        assert logistic(z2).dual == 0

        with pytest.raises(TypeError):
            logistic("string")
