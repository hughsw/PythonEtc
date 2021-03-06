
## Tax Calculators

### Problem 1: `tax2017(income)`

Create a new module, `taxes.py`, in the `assignments` directory and write a function `tax2017(income)` that takes taxable income and returns the amount of Federal tax.
Use the U.S. Federal Tax Brackets for 2017 (from: https://taxfoundation.org/2017-tax-brackets/):

Rate    |Taxable Income Bracket  |Tax Owed
:---    |:---------------------  |:--------
10%     |$0 to $9,325            |$0.00 plus 10% of Taxable Income
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

#### Test your code

To thoroughly test your code, run this command from a shell in the `assignments` directory.
Be sure your `taxes.py` file is saved in the `assignments` directory.

```bash
python3 -m doctest testem.py
```

As with many Unix commands, it should print out nothing if the tests run successfully.
If it prints out any info, something is wrong!

### Extra Credit

A significant fraction of your time doing real-world software work involves reading about software libraries and learning how to use them.
Read about [Python's `doctest` library](https://docs.python.org/3.5/library/doctest.html).
Then explain what the above Unix command and `testem.py` are doing to test your code in `taxes.py`.


### Problem 2: `bracket_bases(tax_table)`

The tax table above does not say where the dollar amounts on the left of the Tax Owed column come from.
These tax-bracket-bases can be derived from the first two columns of values in the table, plus a little knowledge or reasoning about the progressive tax algorithm.

The first two columns of values in the table above can be represented in Python in a static database:
```python
TAX_BRACKETS_2017 = (
    (0.10,   0),
    (0.15,   9325),
    (0.25,   37950),
    (0.28,   91900),
    (0.33,   191650),
    (0.35,   416700),
    (0.3960, 418400),
    )
```

Continuing in `taxes.py`, include this declaration of
TAX_BRACKETS_2017 and write a Python function,
`bracket_bases(tax_table)`, that takes the `TAX_BRACKETS_2017` table
(or any similarly structured progressive tax table), and returns a
list of pairs of the Rate and the corresponding Tax Owed bracket
basis.

E.g.
```
>>> import taxes
>>> taxes.bracket_bases(taxes.TAX_BRACKETS_2017)
[ (0.10, 0.0), (0.15, 932.50), (0.25, 5226.25), (0.28, 18713.75), (0.33, 46643.75), (0.35, 120910.25), (0.3960, 121505.25) ]
```
