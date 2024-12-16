import qrcode
import time
import os

url = str(input("Enter a URL to connect to: "))

img = qrcode.make(url)
os.system('cls')
for i in range(3):
    print("Loading QR Code.")
    time.sleep(0.4)
    print("Loading QR Code..")
    time.sleep(0.4)
    print("Loading QR Code...")
    time.sleep(0.4)
    os.system('cls')
print("Done loading QR Code")
img.save("qrcode.png")