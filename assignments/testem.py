"""
From: https://taxfoundation.org/2017-tax-brackets/

Rate    |Taxable Income Bracket  |Tax Owed
:---    |:---------------------  |:--------
10%     |$0 to $9,325            |10% of Taxable Income
15%     |$9,325 to $37,950       |$932.50 plus 15% of the excess over $9325
25%     |$37,950 to $91,900      |$5,226.25 plus 25% of the excess over $37,950
28%     |$91,900 to $191,650     |$18,713.75 plus 28% of the excess over $91,900
33%     |$191,650 to $416,700    |$46,643.75 plus 33% of the excess over $191,650
35%     |$416,700 to $418,400    |$120,910.25 plus 35% of the excess over $416,700
39.60%  |$418,400+               |$121,505.25 plus 39.6% of the excess over $418,400
"""


def _tax2017_1():
    """
    Test the examples from the assignment

    >>> import taxes

    >>> taxes.tax2017(5000)
    500.0

    >>> taxes.tax2017(25000)
    3283.75

    >>> taxes.tax2017(50000)
    8238.75
    """

def _tax2017_2(income):
    """
    Test values near the breakpoints

    >>> _tax2017_2(0)
    0
    0.1

    >>> _tax2017_2(9325)
    932.4
    932.5
    932.65

    >>> _tax2017_2(37950)
    5226.1
    5226.25
    5226.5

    >>> _tax2017_2(91900)
    18713.5
    18713.75
    18714.03

    >>> _tax2017_2(191650)
    46643.47
    46643.75
    46644.08

    >>> _tax2017_2(416700)
    120909.92
    120910.25
    120910.6

    >>> _tax2017_2(418400)
    121504.9
    121505.25
    121505.65
    """

    import taxes
    if income >= 1:
        print(round(taxes.tax2017(income - 1), 2))
    print(round(taxes.tax2017(income), 2))
    print(round(taxes.tax2017(income + 1), 2))
