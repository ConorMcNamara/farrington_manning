Farrington-Manning Test
=======================

The Farrington-Manning test is a statistical test used to compare incidence rates between two groups, particularly in the context of surveillance data. It is commonly employed in epidemiology to detect disease outbreaks or assess the effectiveness of interventions.  It is an alternative to the Poisson exact test.

Key Concepts
------------

* **Incidence Rate:** The incidence rate measures the frequency of new cases of a disease or event occurring in a population over a specific period. It is typically expressed as the number of new cases per person-time at risk.

* **Surveillance Data:** Surveillance data refers to the systematic collection, analysis, and interpretation of health-related data necessary for the planning, implementation, and evaluation of public health practice.

* **Rate Ratio:** The Farrington-Manning test focuses on comparing the rate ratio, which is the ratio of the incidence rate in the exposed or intervention group to the incidence rate in the unexposed or control group.

Assumptions
-----------

The Farrington-Manning test makes the following key assumptions:

* **Poisson Distribution:** It assumes that the number of events (e.g., disease cases) in each group follows a Poisson distribution. This is often a reasonable assumption for count data, especially when the events are rare.
* **Independence:** It assumes that the events in the two groups are independent of each other.

Methodology
-----------

The Farrington-Manning test is a score test.  Here's a simplified overview:

1.  **Data Setup:**
    * Two groups: Exposed (or intervention) and Unexposed (or control).
    * For each group, we have:
        * Number of events (cases): *x<sub>1</sub>* and *x<sub>2</sub>*
        * Person-time at risk: *t<sub>1</sub>* and *t<sub>2</sub>*

2.  **Incidence Rates:**
    * Calculate the incidence rates: *r<sub>1</sub>* = *x<sub>1</sub>*/ *t<sub>1</sub>* and  *r<sub>2</sub>* = *x<sub>2</sub>*/ *t<sub>2</sub>*

3.  **Null Hypothesis:** The null hypothesis (H<sub>0</sub>) is that the rate ratio is equal to a specified value, often 1 (i.e., the incidence rates are equal in the two groups).  H<sub>0</sub>: *r<sub>1</sub>* / *r<sub>2</sub>* = 1

4.  **Test Statistic:** The Farrington-Manning test statistic is a score statistic that compares the observed number of events in the exposed group to the number expected under the null hypothesis.  The formula involves the total number of events, the person-time at risk in each group, and the hypothesized rate ratio.

5.  **P-value:** The p-value is calculated by comparing the test statistic to a standard normal distribution (or a chi-squared distribution with one degree of freedom, as the square of a standard normal).  A small p-value provides evidence against the null hypothesis.

Advantages
----------

* **Flexibility:** It can be used to test for rate ratios other than 1, allowing for the assessment of specific hypotheses about the magnitude of the difference between the groups.
* **Commonly Used:** It is a widely accepted and used test in epidemiology and public health.
* **Computational Efficiency:** It is computationally straightforward.

Limitations
----------

* **Poisson Assumption:** The validity of the test relies on the assumption that the event counts follow a Poisson distribution.  If this assumption is violated (e.g., due to overdispersion), the test results may be unreliable.
* **Large Sample Size:** Like many statistical tests, the Farrington-Manning test performs best with reasonably large sample sizes.

Paper Attribution
-----------------

The Farrington-Manning test was developed by C.P. Farrington and G. Manning. The key publication is:

* **Farrington, C. P., & Manning, G. (1990). Test statistics for comparing a count observed during a fixed study period to its expected value. *Statistics in Medicine*, *9*(12), 1447-1454.**

This paper provides the detailed methodology and mathematical formulation of the test.
