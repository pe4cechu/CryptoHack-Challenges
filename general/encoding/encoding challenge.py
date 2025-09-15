import codecs
from pwn import *
import json

r = remote("socket.cryptohack.org", 13377, level="debug")


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decode_value(enc_type, value):
    if enc_type == "rot13":
        return codecs.decode(value, "rot_13")
    elif enc_type == "hex":
        return bytes.fromhex(value).decode("utf-8")
    elif enc_type == "utf-8":
        return "".join([chr(b) for b in value])
    elif enc_type == "bigint":
        hex_str = value[2:] if value.startswith("0x") else value
        return bytes.fromhex(hex_str).decode("utf-8")
    elif enc_type == "base64":
        return base64.b64decode(value).decode("utf-8")
    else:
        return value


while True:
    received = json_recv()
    if "type" in received and "encoded" in received:
        decoded = decode_value(received["type"], received["encoded"])
        print(f"Decoded: {decoded}")
        if "crypto{" in decoded:
            break
        to_send = {"decoded": decoded}
        json_send(to_send)
    else:
        print("Final message:", received)
        break
