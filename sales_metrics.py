# sales_metrics.py
def calculate_daily_sales(sales):
"""
Calculates the total sales for the day.
:param sales: list of numerical sales values
:return: total sales sum
"""
return sum(sales)
if __name__ == "__main__":
sample_sales = [100, 200, 300]
discounted_sales = apply_discount(sample_sales, discou
nt=0.2)
print("Discounted Sales:", discounted_sales)
print("Total Discounted Sales:", calculate_daily_sales
(discounted_sales))

def filter_sales(sales, threshold=100):
"""
Filters out sales below a given threshold.
:param sales: list of numerical sales values
:param threshold: minimum sale value to keep
:return: filtered list of sales
"""
return [sale for sale in sales if sale >= threshold]

def apply_discount(sales, discount=0.1):
"""
Applies a discount to each sale item.
:param sales: list of numerical sales values
:param discount: discount rate (e.g., 0.1 = 10%)
:return: list of discounted sales
"""
return [round(sale * (1 - discount), 2) for sale in sa
les]
