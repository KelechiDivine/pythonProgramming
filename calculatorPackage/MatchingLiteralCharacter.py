import re

pattern= '02215'
is_match= 'Match' if re.fullmatch(pattern, '02215')\
    else 'No match'

is_not_match= 'Match' if re.fullmatch(pattern, '51220')\
    else 'No match'

print(is_match)
print(is_not_match)