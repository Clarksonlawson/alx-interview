#!/usr/bin/python3
""" utf8 creation, this script aims to determine if a given data set represents utf-8 encoding """


def validUTF8(data):
    """ doc """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
