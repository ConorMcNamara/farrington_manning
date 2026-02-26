import pytest
from numpy.testing import assert_allclose

from farrington_manning import farrington_manning


class TestFarrington:
    def test_farrington_p_val(self) -> None:
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        actual = farrington_manning(x, y, delta=-0.3, alternative="greater")
        expected = 0.0008037
        assert actual["p_value"] == pytest.approx(expected, abs=1e-06)

    def test_farrington_ci(self) -> None:
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        actual = farrington_manning(x, y, delta=-0.3, alternative="greater")
        expected = [-0.1824742, 0.2282376]
        assert_allclose(actual["ci"], expected, atol=5)

    def test_farrington_two_sided(self) -> None:
        """Test two-sided alternative"""
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        result = farrington_manning(x, y, delta=0.0, alternative="two-sided")
        assert "p_value" in result
        assert "ci" in result
        assert "z_statistic" in result
        assert "rate_difference" in result

    def test_farrington_less(self) -> None:
        """Test less alternative"""
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        result = farrington_manning(x, y, delta=0.0, alternative="less")
        assert "p_value" in result
        assert 0 <= result["p_value"] <= 1

    def test_invalid_alternative(self) -> None:
        """Test that invalid alternative raises ValueError"""
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        with pytest.raises(ValueError, match="alternative must be one of"):
            farrington_manning(x, y, alternative="invalid")
