# farrington_manning
Performs the Farrington-Manning Test in Python. Examples of Farrington-Manning can be found in [DescrTab2](https://search.r-project.org/CRAN/refmans/DescrTab2/html/farrington.manning.html) and [FarringtonManning](https://github.com/kkmann/farringtonManning/tree/master) in R. 

The Farrington-Manning test for rate differences can be used to compare the rate difference of successes between two groups to a preset value. It uses an explicit formula for the standard deviation of the test statistic under the null hypothesis

## Quick Example
```
from farrington_manning import farrington_manning
x = [True] * 20 + [False] * 15
y = [True] * 30 + [False] * 25
result = farrington_manning(x, y, delta=-.3, alternative="greater")
print(result["p_value"])
0.0008037
```

## Notes
Whenever possible, I tried to follow the R naming and code-style to ensure as much 1-1 comparison as possible; however, some liberties were taken to ensure the code follows PEP-8 and scipy guidelines. 

## References
Farrington, Conor P., and Godfrey Manning. "Test statistics and sample size formulae for comparative binomial trials with null hypothesis of non-zero risk difference or non-unity relative risk." Statistics in medicine 9.12 (1990): 1447-1454.
