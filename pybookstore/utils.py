import binascii
import os


def build_secret_key(length):
    return binascii.hexlify(os.urandom(length))
