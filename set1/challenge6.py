import sys
import binascii
import math
import base64

from xor import *

key = "ICE"

KEYSIZE_MIN = 2
KEYSIZE_MAX = 40

def support(b):
    total = 0
    bp = int(b, 16)
    for i in range(8):
        total += ((bp & (1 << i))) >> i
    return total

def hamming_distance(x, y):
    diff = xor(x, y)
    return reduce(lambda acc, b : acc + support(b), diff, 0)

print hamming_distance("this is a test", "wokka wokka!!!")

with open(sys.argv[1], 'r') as fh:
    data = fh.read()
    for size in range(KEYSIZE_MIN, KESIZE_MAX + 1):
        cut1 = data[0:size]
        cut2 = data[size:2 * size]
        distance = (hamming_distance(cut1, cut2)) / float(size)


#with open(sys.argv[1], 'r') as fh:
#    data = base64.b64decode(fh.read())
#
#    keypad = key * int(math.ceil(len(data) / float(3)))
#    ct = xor(data, keypad)
#    print ct
