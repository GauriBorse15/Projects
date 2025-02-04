import qrcode
img = qrcode.make("https://ghotekarsarvesh.wixsite.com/sarveshghotekar")
print(type(img))
img.save("qr1.png")