#!/usr/bin/python

import time
import csv

with open("/root/tanken/output.txt") as f:
	content = f.read().replace('\n', '')
	
start = content.find("price:")
price = content[start+8:start+13].replace('.', ',')
time = time.strftime("%Y-%m-%d %H:%M:%S")

RESULT = [time,price]
resultFile = open("/root/tanken/output.csv",'a')
wr = csv.writer(resultFile, delimiter=";")
wr.writerow(RESULT)
