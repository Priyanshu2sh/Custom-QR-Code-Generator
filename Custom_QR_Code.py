import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=5,border=3)
qr.add_data("https://youtu.be/n40hS9tQmcY?si=OYPV6pBqKgdgC32F")
qr.make(fit=True)
img=qr.make_image(fill_color="grey",back_color="white")
img.save("custom_qr.png")