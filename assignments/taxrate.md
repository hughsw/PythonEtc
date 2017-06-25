
## Tax Calculators

### Problem 1: `tax2017(income)`

In module `taxes.py`, write a function `tax2017(income)` that takes taxable income and returns the amount of Federal tax.
Use the U.S. Federal Tax Brackets for 2017 (from: https://taxfoundation.org/2017-tax-brackets/):

Rate    |Taxable Income Bracket  |Tax Owed
:---    |:---------------------  |:--------
10%     |$0 to $9,325            |10% of Taxable Income
15%     |$9,325 to $37,950       |$932.50 plus 15% of the excess over $9325
25%     |$37,950 to $91,900      |$5,226.25 plus 25% of the excess over $37,950
28%     |$91,900 to $191,650     |$18,713.75 plus 28% of the excess over $91,900
33%     |$191,650 to $416,700    |$46,643.75 plus 33% of the excess over $191,650
35%     |$416,700 to $418,400    |$120,910.25 plus 35% of the excess over $416,700
39.60%  |$418,400+               |$121,505.25 plus 39.6% of the excess over $418,400

E.g.
```
>>> import taxes

>>> taxes.tax2017(5000)
500.0

>>> taxes.tax2017(25000)
3283.75

>>> taxes.tax2017(50000)
8238.75
```
