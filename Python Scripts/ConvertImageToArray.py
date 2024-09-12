from PIL import Image

# Configuring file name
image_path = 'bird.png'
output_file_path = 'bird.txt'

# Convert pixel colour to 2-bit representation
def TwoPixelConv(pixel):
  if pixel<64:
    return format(0, '02b')
  elif pixel<128:
    return format(1, '02b')
  elif pixel<192:
    return format(2, '02b')
  elif pixel<256:
    return format(3, '02b')

# Convert pixel colour to 3-bit representation
def ThreePixelConv(pixel):
  if pixel<32:
    return format(0, '03b')
  elif pixel<64:
    return format(1, '03b')
  elif pixel<96:
    return format(2, '03b')
  elif pixel<128:
    return format(3, '03b')
  elif pixel<160:
    return format(4, '03b')
  elif pixel<192:
    return format(5, '03b')
  elif pixel<224:
    return format(6, '03b')
  elif pixel<256:
    return format(7, '03b')

# Opening image
image = Image.open(image_path).convert('RGB')  # Ensure the image is in RGB mode
pixels = image.load()

# Checking correct image resolutions
if image.size[0]!=100 or image.size[1]!=75:
  print(f"ERROR: '{image_path}' does not have an image resolution of 100x75!")
  exit()

# Create the output file and save it as a text file
out_file = open(output_file_path, "w")
out_file.write("byte imgPixels[] = {")

# For the range of the image
first_pixel = True  # To track the first pixel and avoid comma
for y in range(75):
  for x in range(100):
    # If it's not the first pixel, add a comma
    if not first_pixel:
      out_file.write(",")
    first_pixel = False  # After the first pixel, set this flag to False

    # Save the pixel value as HEX values
    hex_value = int(TwoPixelConv(pixels[x, y][2]) + ThreePixelConv(pixels[x, y][1]) + ThreePixelConv(pixels[x, y][0]), 2)
    out_file.write("0x" + format(hex_value, '02x'))

out_file.write("};")

# Print closing statement
print("Successfully converted the image to a text file ready for the array to be copied to the Arduino IDE!")
out_file.close()