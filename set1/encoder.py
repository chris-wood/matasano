import sys
import os

def init():
	table = {}
	tableString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	for i,v in enumerate(tableString):
		table[i] = v
	return table

def encode(hs, table):
	pass

def main(args, table):
	for line in sys.stdin:
		b64 = encode(line, table)
		print b64

if __name__ == "__main__":
	base64table = init()
	main(sys.argv[1:], base64table)
