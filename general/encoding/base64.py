import base64


def hex_to_base64(hex_str):
    byte_data = bytes.fromhex(hex_str)
    return base64.b64encode(byte_data).decode("utf-8")


print(hex_to_base64("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"))
