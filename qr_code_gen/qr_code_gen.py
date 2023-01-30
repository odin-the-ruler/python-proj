import qrcode as qr
from PIL import Image


# take the text that you want to convert into qrcode
imp = input('Enter your msg: ')


'''
# Simple way to generate qr code

## make qr code
img = qr.make(imp)
## save it
img.save('qr_code_gen/qr.png')

'''

# Custom QR code generator

# for error correcton in qr and chainging some property like box size & border
qrc = qr.QRCode(
    version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4)
# added the msg into qrc to convort into qr code
qrc.add_data(imp)
# just to call the func as we already got our img in qrc
qrc.make(fit=True)
# making customization like fill and back color etc.
im = qrc.make_image(fill_color="purple", back_color='white',)
# saving the img
im.save('qr_code_gen/qr2.png')
