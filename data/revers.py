import csv
from datetime import datetime
from itertools import izip

file = 'weather.csv'

data = (csv.reader(open(file, "rb"), delimiter = ';'))
reversed_data = []

for row in enumerate(reversed(list(data))):
	reversed_data.append(row)

csv.writer(open('reversed_' + file, "wb"), delimiter = ';').writerows(reversed_