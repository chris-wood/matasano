import sys
import binascii
import math
import base64

from xor import *
from byte_cipher import *

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

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:(i + n)]

def transpose(blocks, size):
    # TODO: ugh. this is ugly.
    t = []
    for i in range(size):
        block = []
        for b in blocks:
            block.append(b[i])
        t.append("".join(block))
    return t

# sanity check
print hamming_distance("this is a test", "wokka wokka!!!")

with open(sys.argv[1], 'r') as fh:
    data = fh.read()

    # Find the right key size
    sizes = []
    for size in range(KEYSIZE_MIN, KEYSIZE_MAX + 1):
        cut1 = data[0:size]
        cut2 = data[size:2 * size]
        distance = (hamming_distance(cut1, cut2)) / float(size)

        inserted = False
        for i in range(len(sizes)):
            if distance < sizes[i][1]:
                sizes.insert(i, (size, distance))
                inserted = True
                break
        if not inserted:
            sizes.append((size, distance))

    # Break the ciphertext into KEYSIZE blocks
    print sizes
    for size, _ in sizes:
        data_chunks = [chunk for chunk in chunks(data, size)]
        transposed_blocks = transpose(data_chunks, size)
        keys = []
        for block in transposed_blocks:
            print block
            candidates = crack(block)
            print candidates
            #keys.append(k)

        key = "".join(keys)

        print key 
        # TODO: decrypt
            
        
            


#with open(sys.argv[1], 'r') as fh:
#    data = base64.b64decode(fh.read())
#
#    keypad = key * int(math.ceil(len(data) / float(3)))
#    ct = xor(data, keypad)
#    print ct
