def tax2017(income):
	if income <= 9325:
		taxes_owed = 0.1 * income
	elif income > 9325 and income <= 37950:
		taxes_owed = (income - 9325) * 0.15 + 932.5
	elif income > 37950 and income <= 91900:
		taxes_owed = (income - 37950) * 0.25 + 5226.25
	elif income > 91900 and income <= 191650:
		taxes_owed = (income - 91900) * 0.28 + 18713.75 
	elif income > 191650 and income <= 416700:
		taxes_owed = (income - 191650) * 0.33 + 46643.75 
	elif income > 416700 and income <= 418400:
		taxes_owed = (income - 416700) * 0.35 + 120910.25 
	else:
		taxes_owed = (income - 418400) * 0.396 + 121505.25
	return taxes_owed