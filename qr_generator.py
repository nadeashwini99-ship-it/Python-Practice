
import qrcode

print("===== QR CODE GENERATOR =====")

text = input("Enter text or website URL: ").strip()
filename = input("Enter image filename (without extension): ").strip()

if not text:
    print("Please enter some text or a URL.")

elif not filename:
    print("Please enter a filename.")

else:
    try:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr.add_data(text)
        qr.make(fit=True)

        image = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        image.save(filename + ".png")

        print("\nQR code generated successfully!")
        print("Saved as:", filename + ".png")

    except Exception as error:
        print("Error:", error)
