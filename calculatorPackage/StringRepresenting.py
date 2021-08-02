import re as newRequest

result= newRequest.search(r"(\d+) ([-+*/]) (\d+)"
                          ,"10 + 5")
group_result= result.groups()
firstnum_grouping= result.group(1)
addition_grouping= result.group(2)
secondnum_grouping= result.group(3)

print(secondnum_grouping)
print(group_result)
print(firstnum_grouping)
print(addition_grouping)

