import sys
import os
import io
import math

def init():
	table = {}
	tableString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	for i,v in enumerate(tableString):
		table[i] = v
	return table

def encode(hs, table):
	# walk string in 6 bit chunks, converting each one to the b64 equivalent symbol
    limit = int(math.floor(len(hs) / 3))
    b64val = ""
    for i in range(limit):
        triple = map(lambda n : ord(n), hs[i * 3:(i * 3) + 3])
        
        # abc
        # 01100001 01100010 01100011
        # 011000 010110 001001 100011

        word1 = (triple[0] >> 2) & 63
        word2 = ((triple[0] & 3) << 4) | ((triple[1] >> 4) & 31)
        word3 = ((triple[1] & 31) << 2) | ((triple[2] >> 6) & 3)
        word4 = triple[2] & 63

        print triple, word1, word2, word3, word4

        b64val += table[word1] + table[word2] + table[word3] + table[word4]

    if (len(hs) % 3 == 1):
        word1 = (hs[-1] >> 2) & 63
        word2 = hs[-1] & 3
        b64val += table[word1] + table[word2]
    elif (len(hs) % 3 == 2):
        word1 = (hs[-2] >> 2) & 63
        word2 = ((hs[-2] & 3) << 4) | ((hs[-1] >> 4) & 31)
        word3 = (hs[-1] & 31) << 2
        b64val += table[word1] + table[word2] + table[word3]
    else:
        pass # evenly divisible by 3

	return b64val

def main(args, table):
	stream = sys.stdin
	for line in stream:
		b64 = encode(line.strip(), table)
		print b64

if __name__ == "__main__":
	base64table = init()
	main(sys.argv[1:], base64table)
