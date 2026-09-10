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

    def test_farrington_ci_r_reference(self) -> None:
        """Validate CI against R kkmann/farringtonManning package (alpha=0.025 default)."""
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        actual = farrington_manning(x, y, delta=-0.3, alternative="greater", alpha=0.025)
        expected = [-0.1824742, 0.2282376]
        assert_allclose(actual["ci"], expected, atol=1e-04)

    def test_farrington_ci_default_alpha(self) -> None:
        """Validate CI with default alpha=0.05."""
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        actual = farrington_manning(x, y, delta=-0.3, alternative="greater")
        expected = [-0.1497990, 0.1972266]
        assert_allclose(actual["ci"], expected, atol=1e-04)

    def test_farrington_two_sided(self) -> None:
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        result = farrington_manning(x, y, delta=0.0, alternative="two-sided")
        assert result["rate_difference"] == pytest.approx(0.025974, abs=1e-04)
        assert result["z_statistic"] == pytest.approx(0.24175, abs=1e-04)
        assert result["p_value"] == pytest.approx(0.808976, abs=1e-04)
        assert_allclose(result["ci"], [-0.1824742, 0.2282376], atol=1e-04)

    def test_farrington_less(self) -> None:
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        result = farrington_manning(x, y, delta=0.0, alternative="less")
        assert result["p_value"] == pytest.approx(0.595512, abs=1e-04)
        assert_allclose(result["ci"], [-0.1497990, 0.1972266], atol=1e-04)

    def test_invalid_alternative(self) -> None:
        x = [True] * 20 + [False] * 15
        y = [True] * 30 + [False] * 25
        with pytest.raises(ValueError, match="alternative must be one of"):
            farrington_manning(x, y, alternative="invalid")

    def test_degenerate_all_zeros(self) -> None:
        with pytest.raises(ValueError, match="null-constrained variance is zero"):
            farrington_manning([0] * 10, [0] * 10, delta=0.0)

    def test_degenerate_all_ones(self) -> None:
        with pytest.raises(ValueError, match="null-constrained variance is zero"):
            farrington_manning([1] * 10, [1] * 10, delta=0.0)

    def test_identical_proportions(self) -> None:
        result = farrington_manning([1, 0] * 10, [1, 0] * 10, delta=0.0)
        assert result["p_value"] == pytest.approx(1.0, abs=1e-06)
        assert result["rate_difference"] == pytest.approx(0.0, abs=1e-06)
