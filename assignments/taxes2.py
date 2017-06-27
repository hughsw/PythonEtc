#This isn't interesting...

def tax2017(income):
    assert income >= 0, str(income)

    if income >= 418400:
        return (income - 418400) * 0.396 + 121505.25
    if income >= 416700:
        return (income - 416700) * 0.35 + 120910.25
    if income >= 191650:
        return (income - 191650) * 0.33 + 46643.75
    if income >= 91900:
        return (income - 91900) * 0.28 + 18713.75
    if income >= 37950:
        return (income - 37950) * 0.25 + 5226.25
    if income >= 9325:
        return (income - 9325) * 0.15 + 932.5
    if income > 0:
        return 0.1 * income
    return 0