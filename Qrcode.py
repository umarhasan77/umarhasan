# Importing the qrcode library to generate QR codes
import qrcode

# Taking user input for the text or URL to be converted into a QR code
data = input("Enter the text or URL: ").strip()

# Taking user input for the filename to save the generated QR code image
filename = input("Enter the file name: ").strip()

# Creating a QRCode object with specified box size and border size
qr = qrcode.QRCode(
    box_size=10,  # Size of each box in the QR code grid
    border=4      # Thickness of the border around the QR code
)

# Adding the user-provided data (URL or text) to the QR code
qr.add_data(data)

# Generating the image of the QR code with the specified colors for the QR code and background
image = qr.make_image(fill_color='black', back_color='white')

# Saving the generated QR code image with the specified filename
image.save(filename)

# Printing a message to indicate that the QR code has been successfully saved
print(f"QR Code is saved as {filename}")
