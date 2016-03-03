import os
import sys
import binascii

def xor(x, y):
    return binascii.hexlify(bytearray(map(lambda (xx, yy): chr(ord(xx) ^ ord(yy)), zip(x, y))))

def main(args):
    x = "1c0111001f010100061a024b53535009181c".decode("hex")
    y = "686974207468652062756c6c277320657965".decode("hex")
    print xor(x, y)

    x = "ETAOINSHRDLU"
    y = "XXXXXXXXXXXX"
    print x, y, xor(x, y)

if __name__ == "__main__":
    main(sys.argv[1:])
