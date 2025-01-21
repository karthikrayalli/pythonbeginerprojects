import qrcode


question1 = input("Enter the URL for the QR Code:")
question2 = input("Enter the filename:")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(question1)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(f'{question2}.png')
print(f'QR code saved as {question2}.png')
