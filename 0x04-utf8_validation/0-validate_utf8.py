#!/usr/bin/python3
""" Midule definition """
import codecs


def validUTF8(data):
    """
        Determines if a given dataset represents a valid UTF8 encoding
        Args:
            data: a list of integers, each integer represents 1 byte of data
    """

    # convert array elements to a single bytes strig
    converted_bytes = b''

    for i in data:
        # compute number of bytes(in bits) needed to represent each
        # ..integer value in big endian notation
        bytes_data = i.to_bytes((i.bit_length() + 7) // 8, 'big')
        converted_bytes += bytes_data

    try:
        decoded_val = codecs.decode(converted_bytes, 'utf-8')
        return True
    except UnicodeDecodeError:
        return False
