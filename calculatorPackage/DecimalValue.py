from decimal import Decimal

variable= f'{Decimal("10000000000000000000000000.0"): .3f}'
print(variable)

new_variable= f'{Decimal("10000000000000000000000000.0"): .3E}'
print(new_variable)