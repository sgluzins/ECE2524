import sys
import argparse
import fileinput
from sys import argv
import getopt, sys

parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='*', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('--ignore-blank')
parser.add_argument('--ignore-non-numeric')
parser.parse_args()

"""
if len(sys.argv) > 1:
	num = len(sys.argv) - 1
try: 
	if sys.argv[1:num] == '--ignore-blank':
		print 'YES'
	elif sys.argv[1:num] == '--ignore-non-numeric':
		print 'THIS TOO'		
	else:
"""
try:
	file_result = 1
	for line in fileinput.input():
		num = line
		if num.isspace():
			print float(file_result)
			file_result = 1
		else:
			num = float(num)
			file_result = file_result * num
	print file_result
except EOFError:
	print file_result
except ValueError:
	print 'Could not convert string to float: ' + num
	sys.exit(1)
"""
else:
	result = 1
	try:
		while 1:
			value = raw_input()
			if value.isspace():
				print int(result)
				result = 1
			else:
				try:
					value = float(value)
					result = result * value

				except ValueError:
					print 'Could not convert string to float: ' + value
					sys.exit(1)
	except EOFError:
		print '^D'
		print int(result)
"""
