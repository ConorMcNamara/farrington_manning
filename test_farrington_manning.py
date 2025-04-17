import pytest

from farrington_manning import farrington_manning
from numpy.testing import assert_allclose


class Test_Farrington:
    @staticmethod
    def test_farrington_p_val() -> None:
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        actual = farrington_manning(x, y, delta=-0.3, alternative="greater")
        expected = 0.0008037
        assert actual["p_value"] == pytest.approx(expected, abs=1e-06)

    @staticmethod
    def test_farrington_ci() -> None:
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        actual = farrington_manning(x, y, delta=-0.3, alternative="greater")
        expected = [-0.1824742, 0.2282376]
        assert_allclose(actual["ci"], expected, atol=5)
