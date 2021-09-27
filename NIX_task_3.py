"""
 TASK_3: Format price
Напишите функцию, которая будет преобразовывать цену к формату,
отображающему до двух знаков после точки, например:
22.32131 -> 22.32
58.60125 -> 58.6
34.0 -> 34
"""


def get_formate_price(price):
	format_price = 0

	if type(price) == float:  # if there are no numbers after zero, then remove zero after the comma and the comma
		if str(price)[-1] == '0' and str(price)[-2] == '.':
			format_price = int(str(price)[0:-2:])
	else:
		format_price = round(price, 2)
	return format_price


print(get_formate_price(22.32131))  # 22.32131 -> 22.32
print(get_formate_price(58.60125))  # 58.60125 -> 58.6
print(get_formate_price(34.0))  # 34.0 -> 34
