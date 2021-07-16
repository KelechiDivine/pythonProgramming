import InvestmentReturn

userInput = int(input("Enter investment here: "))

print(f"Investment after ten years: "
      f"{InvestmentReturn.invest_after_ten_years(userInput)}")
print(f"Investment after twenty years: "
      f"{InvestmentReturn.invest_after_twenty_years(userInput)}")
print(f"Investment after thirty years: "
      f"{InvestmentReturn.investment_after_thirty_years(userInput)}")
