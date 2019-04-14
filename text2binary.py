#!/usr/bin/env python
import binascii
a = raw_input("Enter Some Text: ")
print(' '.join(format(ord(x), 'b') for x in a))