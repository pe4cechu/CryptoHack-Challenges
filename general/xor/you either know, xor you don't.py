from pwnlib.util.fiddling import xor


def find_possible_key(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


ciphertext = bytes.fromhex(
    "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
)

a = bytes.fromhex("0e0b213f26041e" + "04")
b = "crypto{}".encode("utf-8")
key = find_possible_key(a, b)

flag = xor(ciphertext, key).decode("utf-8")
print(flag)
