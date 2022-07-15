from PIL import Image, ImageDraw, ImageFont
#import qrcode as QR
import qrcode
from font_fredoka_one import FredokaOne

# Setup epaper detail..
#epaper_resolution = 212,104
epaper_resolution = 250,212
img = Image.new(mode = 'RGB',
                size=(epaper_resolution[0], epaper_resolution[1]),
                color = 'white')
img.show()

# Create QR code
qr = qrcode.QRCode(
    version=1,
    box_size=2,
    border = 0
)
qr.add_data('WIFI:S:FieldEP;T:')
wifi_qr = qr.make_image()
wifi_qr.save('wifi_test.png')
wifi_qr.height

img.paste(wifi_qr,(0,0))
img.show()

qr = qrcode.QRCode(
    version=1,
    box_size=2
)

# WIFI ..
fnt = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf",15)
fnt = ImageFont.truetype(FredokaOne,15)
# Create a transparent image for text.
txt = Image.new("RGB", img.size,(255,255,255))
#
d = ImageDraw.Draw(img)
d.text((10,50), "WiFi", font=fnt, fill=(0,0,0))
# Combine..
img.show()

from inky import InkyPHAT
inky_display = InkyPHAT("black")
inky_display.set_border

 


#out = Image.alpha_composite(img, txt)
#out.show()





##URL..
#qr.add_data('http://192.168.0.10:8000')
#im = qr.make_image()
#im.save('stream_IP.png')
#im.height


####

#import pyqrcode
#url = pyqrcode.create('http://uca.edu')
#url.svg('uca-url.svg', scale=2)
#print(url.terminal(quiet_zone=1))

#big_code = pyqrcode.create('0987654321', error='L', version=27, mode='binary')
#big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])

#import wifi_qrcode_generator as qr

#qr.wifi_qrcode('FieldEP', False, 'None', '')

