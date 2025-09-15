from pwnlib.util.fiddling import xor


def find_flag(key):
    for b in range(256):
        key2 = xor(key, b)
        try:
            decoded = key2.decode("utf-8")
            if "crypto{" in decoded:
                return decoded
        except UnicodeDecodeError:
            continue
    return None


key = bytes.fromhex(
    "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
)
print(find_flag(key))
