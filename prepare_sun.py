import csv
from datetime import datetime
from itertools import izip

DATA = "wind_dataset.csv"

data = csv.reader(open(DATA, "rb"), delimiter = ';')
transposed = izip(*raw)

for row in transposed:
	max_item = 0.0
	for item in row:
		a = abs(float(item))
		if a > max_item:
			max_item = a
	print max_item
	for i, item in enumerate(row):
		row[i] = float(item) / max_item  


normalized = izip(*transposed)

csv.writer(open(DATA, "wb"), delimiter = ';').writerows(normalized)

DATA = "solar_dataset.csv"

data = csv.reader(open(DATA, "rb"), delimiter = ';')
transposed = izip(*raw)

for row in transposed:
	max_item = 0.0
	for item in row:
		a = abs(float(item))
		if a > max_item:
			max_item = a
	print max_item
	for i, item in enumerate(row):
		row[i] = float(item) / max_item  

normalized = izip(*transposed)

csv.writer(open('normalized_' + DATA, "wb"), delimiter = ';').writerows(normalized)