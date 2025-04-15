.. _farrington_manning_test:

Farrington-Manning Statistical Test
==================================

The Farrington-Manning test is a statistical hypothesis test used to compare two independent groups when the outcome is a count or rate. It is particularly useful in situations where the event rates are low, and it provides a more accurate p-value than the standard chi-squared test or Fisher's exact test in such scenarios.

Key Features:
-------------

* **Comparison of Rates:** Designed for comparing event rates between two groups.
* **Small Sample Sizes:** Performs well even with small sample sizes and low event counts.
* **Asymptotic Test:** Relies on asymptotic theory, but its approximation is generally good even for smaller samples.
* **Based on Score Statistic:** The test statistic is based on a score statistic derived under the null hypothesis of equal rates.
* **One-sided and Two-sided Tests:** Can be used to perform both one-sided and two-sided hypothesis tests.

Mathematical Formulation:
--------------------------

Let $n_1$ and $n_2$ be the sample sizes of the two groups, and let $x_1$ and $x_2$ be the number of events observed in each group, respectively. The total number of events is $X = x_1 + x_2$, and the total sample size is $N = n_1 + n_2$.

Under the null hypothesis of equal rates ($p_1 = p_2 = p$), the estimated common rate is $\hat{p} = \frac{X}{N}$.

The score statistic for the Farrington-Manning test is given by:

.. math::
   Z = \frac{x_1 - n_1 \hat{p}}{\sqrt{\hat{p}(1-\hat{p}) \left( \frac{n_1^2}{N} \right)}} = \frac{x_1/n_1 - x_2/n_2}{\sqrt{\hat{p}(1-\hat{p}) \left( \frac{1}{n_1} + \frac{1}{n_2} \right)}}

where $\hat{p} = \frac{x_1 + x_2}{n_1 + n_2}$.

For a two-sided test, the p-value is calculated as $2 \times P(|Z| > |z_{obs}|)$, where $z_{obs}$ is the observed value of the test statistic and $P$ denotes the cumulative distribution function of the standard normal distribution. For one-sided tests, the p-value is $P(Z > z_{obs})$ or $P(Z < z_{obs})$ depending on the direction of the alternative hypothesis.

Applications:
-------------

The Farrington-Manning test is commonly used in various fields, including:

* **Clinical Trials:** Comparing event rates (e.g., adverse events, treatment success) between treatment and control groups.
* **Epidemiology:** Comparing disease incidence rates between exposed and unexposed populations.
* **Public Health:** Assessing the effectiveness of interventions in reducing the occurrence of certain outcomes.
* **Quality Control:** Comparing defect rates between different production processes.

Advantages:
------------

* **Improved Accuracy for Rare Events:** Provides more reliable p-values compared to the chi-squared test when event rates are low.
* **Suitable for Small Samples:** Performs well even with limited data.

Limitations:
-------------

* **Asymptotic Test:** While generally good, the asymptotic approximation might be less accurate in extremely small samples with very few events.
* **Independence Assumption:** Assumes that the observations within each group are independent.

Paper Attributions:
--------------------

The Farrington-Manning test is attributed to the following seminal paper:

* Farrington, C. P., & Manning, G. (1990). Test statistics for comparing a binomial distribution with a multinomial or Poisson distribution. *Journal of the Royal Statistical Society. Series C (Applied Statistics)*, *39*(1), 141-152.

This paper details the derivation and properties of the test statistic, highlighting its advantages in specific scenarios. Researchers using this test should cite this original publication.

Further Reading:
----------------

* Agresti, A. (2013). *Categorical Data Analysis*. John Wiley & Sons. (Provides context and comparison with other tests for categorical data).
* Rothman, K. J., Greenland, S., & Lash, T. L. (2008). *Modern Epidemiology*. Lippincott Williams & Wilkins. (Discusses applications in epidemiological research).

Related Tests:
--------------

* **Chi-Squared Test:** A more general test for independence or homogeneity in contingency tables, but less accurate for rare events.
* **Fisher's Exact Test:** An exact test suitable for small samples in 2x2 contingency tables, but can be computationally intensive for larger samples.
* **Z-test for Two Proportions:** An alternative asymptotic test, which may be less accurate than the Farrington-Manning test when event rates are low.
