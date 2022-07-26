import csv

"""table_data = [
    ['a', 'b', 'c'],
    ['ABC', 'b', 'c'],
    ['a', 'XYZ', 'c']
]
for row in table_data:
    print("{: >5} {: >5} {: >5}".format(*row))


header = ['X Coordinate', 'Y Coordinate', 'Result']
row = ['100', '200', '300']
rows = [header, row, row, row]
print('\n'.join([''.join(['{:16}'.format(x) for x in r]) for r in rows]))

Nome = ["Allen", "Araujo", "Santos"]
Nomes = ["PrimeiroNome", "SegundoNome", "TerceiroNome"]

print("\n".join([' '.join(['{:16}'.format(x) for x in Nomes]) for y in Nome]))"""

with open('data.csv', 'w') as csvfile:
        filewrite = csv.writer(csvfile, delimiter=',')
        filewrite.writerow(['Ola', 'Comovai'])
