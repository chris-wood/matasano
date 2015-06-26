import sys
import os
import io

def init():
	table = {}
	tableString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	for i,v in enumerate(tableString):
		table[i] = v
	return table

def encode(hs, table):
	# walk string in 6 bit chunks, converting each one to the b64 equivalent symbol
	pass

def main(args, table):
	stream = sys.stdin
	for line in stream:
		b64 = encode(line, table)
		print b64

if __name__ == "__main__":
	base64table = init()
	main(sys.argv[1:], base64table)
