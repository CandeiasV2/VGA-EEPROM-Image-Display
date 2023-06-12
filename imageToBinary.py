from PIL import Image

# Convert pixel colour to 2 bit representation
def TwoPixelConv(pixel):
  if pixel<64:
    return format(0, '02b')
  elif pixel<128:
    return format(1, '02b')
  elif pixel<192:
    return format(2, '02b')
  elif pixel<256:
    return format(3, '02b')

# Convert pixel colour to 3 bit representation
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


file_path = 'bird.png'
output_file_path = 'out.bin'

image = Image.open(file_path)
pixels = image.load()

# Checking correct image resolution 
if image.size[0]!=100 or image.size[1]!=75:
  print(f"ERROR: '{file_path}' does not have an image resolution of 100x75!")
  exit()

# Create the output file and save it in binary
out_file = open(output_file_path, "wb")
# For the range of the EEPROM
for y in range(256):
  for x in range(128):
    try:
      # Save the pixel value as bytes to the output file
      hex_value = int(TwoPixelConv(pixels[x,y][2]) + ThreePixelConv(pixels[x,y][1]) + ThreePixelConv(pixels[x,y][0]), 2)
      out_file.write(hex_value.to_bytes(1, byteorder='big'))
    except IndexError:
      # If the pixel value does not exist, save as byte 0
      out_file.write(bytes([0]))

print("Successfully converted image to binary file!")
out_file.close()
