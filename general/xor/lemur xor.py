from PIL import Image
from pwnlib.util.fiddling import xor

img1 = Image.open("input/flag.png").convert("RGB")
img2 = Image.open("input/lemur.png").convert("RGB")
img1 = img1.resize(img2.size)

bytes1 = img1.tobytes()
bytes2 = img2.tobytes()

xor_bytes = xor(bytes1, bytes2)

xor_img = Image.frombytes("RGB", img1.size, xor_bytes)
xor_img.save("output/lemur xor.png")
