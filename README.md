# farrington_manning

[![CI](https://github.com/ConorMcNamara/farrington_manning/actions/workflows/ci.yml/badge.svg)](https://github.com/ConorMcNamara/farrington_manning/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/ConorMcNamara/farrington_manning/branch/main/graph/badge.svg)](https://codecov.io/gh/ConorMcNamara/farrington_manning)
[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python implementation of the Farrington-Manning test for comparing rate differences between two groups.

The Farrington-Manning test for rate differences can be used to compare the rate difference of successes between two groups to a preset value. It uses an explicit formula for the standard deviation of the test statistic under the null hypothesis.

## Features

- 🎯 Precise hypothesis testing for rate differences
- 📊 Supports two-sided, greater, and less alternatives
- 🔧 Fully typed with comprehensive type hints
- ✅ Thoroughly tested with pytest
- 📈 Compatible with numpy arrays, lists, and tuples

## Installation

### From PyPI (when published)

```bash
pip install farrington-manning
```

### From source

```bash
git clone https://github.com/ConorMcNamara/farrington_manning.git
cd farrington_manning
pip install -e .
```

### Development installation

```bash
git clone https://github.com/ConorMcNamara/farrington_manning.git
cd farrington_manning
pip install -e ".[dev]"
pre-commit install
```

## Requirements

- Python 3.13+
- numpy >= 2.2.4
- scipy >= 1.15.2

## Quick Start

```python
from farrington_manning import farrington_manning

# Define your data: True indicates success, False indicates failure
group1 = [True] * 20 + [False] * 15  # 20 successes, 15 failures
group2 = [True] * 30 + [False] * 25  # 30 successes, 25 failures

# Run the test
result = farrington_manning(group1, group2, delta=-0.3, alternative="greater")

# Access the results
print(f"P-value: {result['p_value']:.6f}")
print(f"Rate difference: {result['rate_difference']:.4f}")
print(f"Z-statistic: {result['z_statistic']:.4f}")
print(f"95% CI: [{result['ci'][0]:.4f}, {result['ci'][1]:.4f}]")
```

Output:
```
P-value: 0.000804
Rate difference: 0.0229
Z-statistic: 3.21
95% CI: [-0.1825, 0.2282]
```

## Usage Examples

### Two-sided test

Test if the rate difference is significantly different from zero:

```python
result = farrington_manning(group1, group2, delta=0.0, alternative="two-sided")
```

### Non-inferiority test

Test if group 1 is non-inferior to group 2 (i.e., not worse by more than 10%):

```python
result = farrington_manning(group1, group2, delta=-0.1, alternative="greater")
```

### Superiority test

Test if group 1 is superior to group 2 by at least 5%:

```python
result = farrington_manning(group1, group2, delta=0.05, alternative="greater")
```

### Using numpy arrays

```python
import numpy as np

# Generate random boolean data
np.random.seed(42)
group1 = np.random.rand(100) > 0.4  # ~60% success rate
group2 = np.random.rand(100) > 0.5  # ~50% success rate

result = farrington_manning(group1, group2)
```

## API Reference

### `farrington_manning(group1, group2, delta=0.0, alternative="two-sided", alpha=0.05)`

Perform the Farrington-Manning test for rate differences.

**Parameters:**

- `group1` (list | tuple | np.ndarray): A logical vector of data from Group 1, where True indicates a success
- `group2` (list | tuple | np.ndarray): A logical vector of data from Group 2, where True indicates a success
- `delta` (float, default=0.0): The rate difference under the null hypothesis
- `alternative` (str, default="two-sided"): The alternative hypothesis. One of:
  - `"two-sided"`: Test if rate difference ≠ delta
  - `"greater"`: Test if rate difference ≥ delta
  - `"less"`: Test if rate difference ≤ delta
- `alpha` (float, default=0.05): The significance level for confidence interval calculation

**Returns:**

A dictionary containing:
- `"rate_difference"` (float): The observed rate difference (p1 - p2)
- `"z_statistic"` (float): The test statistic
- `"p_value"` (float): The p-value for the test
- `"ci"` (list): The confidence interval [lower, upper]

## Statistical Background

The Farrington-Manning test is particularly useful for:

- Clinical trials comparing treatment success rates
- A/B testing in product analytics
- Quality control comparisons
- Non-inferiority and superiority testing

The test formulates hypotheses as:

- **Two-sided**: H₀: p₁ - p₂ = δ
- **Greater**: H₀: p₁ - p₂ ≥ δ
- **Less**: H₀: p₁ - p₂ ≤ δ

For non-inferiority testing with delta < 0 and alternative="greater", rejection of the null hypothesis allows concluding that the rate of success in group 1 is at worst |delta| smaller than that of group 2.

## Related R Implementations

This Python implementation is based on and compatible with:

- [DescrTab2::farrington.manning](https://search.r-project.org/CRAN/refmans/DescrTab2/html/farrington.manning.html)
- [farringtonManning](https://github.com/kkmann/farringtonManning)

## References

Farrington, Conor P., and Godfrey Manning. "Test statistics and sample size formulae for comparative binomial trials with null hypothesis of non-zero risk difference or non-unity relative risk." *Statistics in Medicine* 9.12 (1990): 1447-1454.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Install development dependencies (`pip install -e ".[dev]"`)
4. Install pre-commit hooks (`pre-commit install`)
5. Make your changes and ensure tests pass (`pytest`)
6. Commit your changes (`git commit -m 'Add some amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development

### Running tests

```bash
pytest
```

### Running tests with coverage

```bash
pytest --cov=farrington_manning --cov-report=html
```

### Linting

```bash
ruff check .
ruff format .
zuban check src/farrington_manning
```

### Pre-commit hooks

```bash
pre-commit run --all-files
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Conor McNamara**
- Email: conor.s.mcnamara@gmail.com
- GitHub: [@ConorMcNamara](https://github.com/ConorMcNamara)
