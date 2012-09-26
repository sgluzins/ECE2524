import sys
import argparse

parser = argparse.ArgumentParser(description='Process some numbers.')
parser.parse_args()

result = 1
try:
	while 1:
		value = raw_input()
		if value == ' ':
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
