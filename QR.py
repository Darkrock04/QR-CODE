import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="blue")
    img.save(filename)


data = input("'Enter anything to generate QR :")
filename = "QRcode.png"
generate_qr_code(data, filename)
print(f"QR code generated and saved as {filename}")
