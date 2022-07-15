from PIL import Image, ImageDraw, ImageFont
#import qrcode as QR
import qrcode
from font_fredoka_one import FredokaOne
import time

# Setup epaper detail..
#epaper_resolution = 212,104
epaper_resolution = 250,212
img = Image.new(mode = 'P',
                size=(epaper_resolution[0], epaper_resolution[1]))
#img.show()

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
#img.show()

# WIFI ..
#fnt = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf",15)
fnt = ImageFont.truetype(FredokaOne,15)
# Create a transparent image for text.
#txt = Image.new("RGB", img.size,(255,255,255))
#
#txt = Image.new("RGBA",(epaper_resolution[0],epaper_resolution[1]), (255,255,255,0))
#d = ImageDraw.Draw(img)
#d.text((80,80), "WiFi", font=fnt, fill = (255,255,255))
#img = Image.alpha_composite(txt,img)

# Combine..
#img.show()
#img.save('epapr.png')
#epapr = Image.open('epapr.png')
#epapr.resize((250,122))

from inky import InkyPHAT_SSD1608
inky_display = InkyPHAT_SSD1608("black")
#inky_display.set_border

fnt = ImageFont.truetype(FredokaOne,220)
d = ImageDraw.Draw(img)
d.text((60,60), "WiFi", colour = 'black', font=fnt)
time.sleep(1)
img.save('epapr.png')
epapr = Image.open('epapr.png')
#epapr.resize(250,122)


inky_display.set_image(epapr)
inky_display.show()
 


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

