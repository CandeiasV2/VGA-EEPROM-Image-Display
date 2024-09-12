from PIL import Image

# Configure file names
image1_path = 'finch.png'
image2_path = 'bird.png'
output_file_path = 'out.bin'

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

# Opening images
image1 = Image.open(image1_path)
pixels1 = image1.load()
image2 = Image.open(image2_path)
pixels2 = image2.load()

# Checking correct image resolutions
if image1.size[0]!=100 or image1.size[1]!=75:
  print(f"ERROR: '{image1_path}' does not have an image resolution of 100x75!")
  exit()
if image2.size[0]!=100 or image2.size[1]!=75:
  print(f"ERROR: '{image2_path}' does not have an image resolution of 100x75!")
  exit()

# Create the output file and save it as binary
out_file = open(output_file_path, "wb")
# For the range of the EEPROM
for y in range(256):
  for x in range(128):
    try:
      if y<128:   # First half of EEPROM
        # Save the pixel value as bytes to the output file
        hex_value = int(TwoPixelConv(pixels1[x,y][2]) + ThreePixelConv(pixels1[x,y][1]) + ThreePixelConv(pixels1[x,y][0]), 2)
        out_file.write(hex_value.to_bytes(1, byteorder='big'))
      else:       # Second half of EEPROM
        # Save the pixel value as bytes to the output file
        hex_value = int(TwoPixelConv(pixels2[x,y-128][2]) + ThreePixelConv(pixels2[x,y-128][1]) + ThreePixelConv(pixels2[x,y-128][0]), 2)
        out_file.write(hex_value.to_bytes(1, byteorder='big'))
    except IndexError:
      # If the pixel value does not exist, save as byte 0
      out_file.write(bytes([0]))

# Print closing statement
print("Successfully converted images to a binary file ready to be loaded into the EEPROM!")
out_file.close()