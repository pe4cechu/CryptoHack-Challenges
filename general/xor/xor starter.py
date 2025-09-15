def char_to_ascii(char):
    return chr(ord(char) + 1)


def xor(str, b):
    a = ""
    for c in str:
        a += chr(ord(c) ^ b)
    return a


print("crypto{" + xor("label", 13) + "}")
