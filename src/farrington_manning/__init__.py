"""Farrington-Manning test for rate differences.

This package implements the Farrington-Manning test for comparing rate differences
between two groups. The test uses an explicit formula for the standard deviation
of the test statistic under the null hypothesis.
"""

from farrington_manning._core import farrington_manning

__version__ = "1.0.0"
__all__ = ["farrington_manning"]
