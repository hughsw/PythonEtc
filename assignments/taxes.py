TAX_BRACKETS_2017 = (
    (0.10,   0),
    (0.15,   9325),
    (0.25,   37950),
    (0.28,   91900),
    (0.33,   191650),
    (0.35,   416700),
    (0.3960, 418400),
    )

def tax2017(income):
	assert income >= 0, str(income)
	
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


def bracket_bases(tax_table):
	tax_table_list = []
	tax = 0
	prev_thres = 0
	prev_rate = 0
	for rate, threshold in tax_table:
		tax += prev_rate * (threshold - prev_thres)
		prev_thres = threshold
		prev_rate = rate
		tax_table_list.append((rate, tax))
	return tax_table_list