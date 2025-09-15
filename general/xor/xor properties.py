from pwnlib.util.fiddling import xor

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_xor_key1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_xor_key3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_xor_key1_xor_key3_xor_key2 = bytes.fromhex(
    "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
)

key2 = xor(key2_xor_key1, key1)
key3 = xor(key2_xor_key3, key2)
flag = xor(flag_xor_key1_xor_key3_xor_key2, key1, key2, key3)

print(flag.decode("utf-8"))
