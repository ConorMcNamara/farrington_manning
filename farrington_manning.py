from math import pi, acos, cos, sqrt
from typing import Union

import numpy as np

from scipy.stats import norm
from scipy.optimize import brentq


def _get_sd_diff_ML_null(
    n1: int, n2: int, p1_ml: float, p2_ml: float, delta: float
) -> float:
    """Gets the standard deviation of the rate difference under the null hypothesis (risk difference = -delta)

    Parameters
    ----------
    n1 : int
        Number of users in Group 1
    n2 : int
        Number of users in Group 2
    p1_ml : float
        The probability of success in Group 1
    p2_ml : float
        The probability of success in Group 2
    delta : float
        The rate difference under the null hypothesis

    Returns
    -------
    The standard deviation of the rate difference under the null hypothesis
    """
    theta = n2 / n1
    d = -p1_ml * delta * (1 + delta)
    c = pow(delta, 2) + delta * (2 * p1_ml + theta + 1) + p1_ml + theta * p2_ml
    b = -(1 + theta + p1_ml + theta * p2_ml + delta * (theta + 2))
    a = 1 + theta
    v = pow(b, 3) / (27 * pow(a, 3)) - b * c / (6 * pow(a, 2)) + d / (2 * a)
    u = np.sign(v) * sqrt(pow(b, 2) / (9 * pow(a, 2)) - c / (3 * a))
    w = (pi + acos(v / pow(u, 3))) / 3
    p1_ML_null = 2 * u * cos(w) - b / (3 * a)
    p2_ML_null = p1_ML_null - delta
    sd_diff_ML_null = sqrt(
        p1_ML_null * (1 - p1_ML_null) / n1 + p2_ML_null * (1 - p2_ML_null) / n2
    )
    return sd_diff_ML_null


def _get_z(diff_ml: float, delta: float, sd_diff: float) -> float:
    """Gets the z-statistic for our test

    Parameters
    ----------
    diff_ml : float
        The standard deviation of the rate difference under the null hypothesis
    delta : float
        The rate difference under the null hypothesis
    sd_diff : float
        The standard deviation of the rate difference under the null hypothesis

    Returns
    -------
    Our z-statistic for our test
    """
    return (diff_ml - delta) / sd_diff


def _get_ci(delta: float, diff_ml: float, sd_diff: float, alpha_mod: float) -> float:
    """Used to get the upper and lower bounds of the confidence interval

    Parameters
    ----------
    delta : float
        The rate difference under the null hypothesis
    diff_ml : float
        The standard deviation of the rate difference under the null hypothesis
    sd_diff : float
        The standard deviation of the rate difference under the null hypothesis
    alpha_mod : float
        The value of our alpha level.

    Returns
    -------
    The confidence interval of our test
    """
    z = _get_z(diff_ml, delta, sd_diff)
    return 2 * min(norm.sf(z), norm.cdf(z)) - alpha_mod


def farrington_manning(
    group1: Union[list, tuple, np.array],
    group2: Union[list, tuple, np.array],
    delta: float = 0.0,
    alternative: str = "two-sided",
    alpha: float = 0.05,
) -> dict:
    """The Farrington-Manning test for rate differences can be used to compare the rate difference of successes
     between two groups to a preset value. It uses an explicit formula for the standard deviation of the test
     statistic under the null hypothesis [1].

    Parameters
    ----------
    group1 : list, tuple or numpy array
        A logical vector of data from Group 1, where True indicates a success
    group2 : list, tuple or numpy array
        A logical vector of data from Group 2, where True indicates a success
    delta : float, default=0.0
        The rate difference under the null hypothesis
    alternative : {'two-sided', 'less', 'greater'}
        Character string indicating the alternative to use, either of "two-sided", "less", "greater"
    alpha : float, default=0.05
        The significance level (acceptable error of the first kind), a two-sided confidence interval is returned
        with confidence level 1 - 2*alpha, such that the lower bound is a valid one-sided confidence interval at
        the confidence level 1 - alpha.

    Returns
    -------
    The p-value and the Confidence Interval of our test

    Notes
    -----
    The Farrington-Maning test for rate differences test the null hypothesis
    of \\deqn{H_{0}: p_{1} - p_{2} = \\delta}{H[0]: p[1] - p[2] = \\delta} for the "two.sided" alternative
    (or \\eqn{\\geq}{\\ge} for the "greater" respectively \\eqn{\\leq}{\\le} for the "less" alternative).
    This formulation allows to specify non-inferiority and superiority test in a consistent manner:
    \\describe{
        \\item{non-inferiority}{for delta < 0 and alternative == "greater" the null hypothesis
        reads \\eqn{H_{0}: p_{1} - p_{2} \\geq \\delta}{H[0]: p[1] - p[2] \\ge \\delta} and
        consequently rejection allows concluding that \\eqn{p_1 \\geq p_2 + \\delta}{p[1] \\ge p[2] + \\delta}
        i.e. that the rate of success in group one is at least the
        success rate in group two plus delta - as delta is negagtive this is equivalent to the success rate of group 1
        being at worst |delta| smaller than that of group 2.}
        \\item{superiority}{for delta >= 0 and alternative == "greater" the null hypothesis
        reads \\eqn{H_{0}: p_{1} - p_{2} \\geq \\delta}{H[0]: p[1] - p[2] \\ge \\delta} and
        consequently rejection allows concluding that \\eqn{p_1 \\geq p_2 + \\delta}{p[1] \\ge p[2] + \\delta}
        i.e. that the rate of success in group one is at least delta greater than the
        success rate in group two.}
    }
    The confidence interval is always computed as two-sided, but with 1-2\\eqn{\alpha} confidence level
    in case of a one-sided hypthesis. This means that the lower or upper vound are valid one-sided
    confidence bounds at level \\eqn{\alpha} in this case.
    The confidence interval is constructed by inverting the two-sided test directly.
    """
    if alternative.casefold() not in ["two-sided", "greater", "less"]:
        raise ValueError("alternative must be one of `two-sided`, `greater` or `less`")
    n1, n2 = len(group1), len(group2)
    group1, group2 = [int(val) for val in group1], [int(val) for val in group2]
    p1_ml, p2_ml = np.mean(group1), np.mean(group2)
    diff_ml = p1_ml - p2_ml
    sd_diff_ml_null = _get_sd_diff_ML_null(n1, n2, p1_ml, p2_ml, delta)
    z = _get_z(diff_ml, delta, sd_diff_ml_null)
    if alternative.casefold() == "two-sided":
        p_value = 2 * min(norm.sf(z), norm.cdf(z))
    elif alternative.casefold() == "greater":
        p_value = norm.sf(z)
    else:
        p_value = norm.cdf(z)
    alpha_mod = alpha if alternative.casefold() == "two-sided" else 2 * alpha
    ci_lower = brentq(
        _get_ci, -1 + 1e-6, diff_ml, args=(diff_ml, sd_diff_ml_null, alpha_mod)
    )
    ci_upper = brentq(
        _get_ci, diff_ml, 1 - 1e-06, args=(diff_ml, sd_diff_ml_null, alpha_mod)
    )
    return_dict = {
        "rate_difference": diff_ml,
        "z_statistic": z,
        "p_value": p_value,
        "ci": [ci_lower, ci_upper],
    }
    return return_dict
