#User @Hack9_MrNoX
#install QR Code Modual "pip install qrcode[pil]"

from cgitb import text
import qrcode
Data = input("\033[1;32;40mEnter the Link & Text for QR \t \n -=>")
print("\033[1;32;40m Bright Green  \n")
img = qrcode.make(Data)
img.save("QR.jpg")