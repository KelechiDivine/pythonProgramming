MLB_team = dict(
    
    Colorado= "Rockies",
    Boston= "Red Sox",
    Minnesota= "Twins",
    Milwaukee= "Brewers",
    Seattle= "Mariners"
)

# print(type(MLB_team))
# print(MLB_team)
# print(MLB_team["Boston"])
MLB_team["What the fuck"] = "Nigeria"
# print(MLB_team["Kankas City"])
del MLB_team["What the fuck"]
print(MLB_team)