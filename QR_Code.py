#User @Hack9_MrNoX
#install QR Code Modual "pip install qrcode[pil]"

from cgitb import text
import qrcode
Data = input("Enter the Link & Text for QR \t \n -=>")

img = qrcode.make(Data)
img.save("QR.jpg")
