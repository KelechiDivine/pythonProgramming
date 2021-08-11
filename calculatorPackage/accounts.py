import csv

with open('accounts.csv', mode= 'r', newline= '') as accounts:
    print(f'{"Account": <10}{"Balance":>10}')
    Reader_reader = csv.reader(accounts)
    
    for records in Reader_reader:
        print(f"{accounts:<10}{name:<10}{balance:>10}")
