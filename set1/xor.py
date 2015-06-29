import os
import sys
import binascii

def xor(x, y):
    z = "".join(map(lambda (xx, yy): chr(ord(xx) ^ ord(yy)), zip(x, y)))
    return z.encode("hex")

def main(args):
    x = "1c0111001f010100061a024b53535009181c".decode("hex")
    y = "686974207468652062756c6c277320657965".decode("hex")
    print xor(x, y)

if __name__ == "__main__":
    main(sys.argv[1:])
