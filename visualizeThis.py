import binascii
import Image
import math
import sys

def GetHexStringFromFile(binary_file='./hello'):
  # Open test binary file:
  binfile = open(binary_file,'rb')
  hexString = ''
  try:
    byte = binfile.read(1)
    byte = binascii.hexlify(byte)
    hexString += byte
    while byte != "":
      byte = binfile.read(1)
      byte = binascii.hexlify(byte)
      if byte == "00": continue # Remove Padding Spaces
      hexString += byte
  finally:
    return hexString, binfile


def SplitToHexArray(hexString):
  hexArray = []
  while hexString:
    hexArray.append(hexString[0:6])
    hexString = hexString[6:]
  # Add some Zero Padding to the last element if it's short of 6 characters.
  if (len(hexArray[-1]) < 6): hexArray[-1] += (abs(len(hexArray[-1])-6))*'0'
  return hexArray


def getRGBTuple(hexVal):
  # Taken from:
  #   http://code.activestate.com/recipes/266466-html-colors-tofrom-rgb-tuples/
  #if (hexVal == "000000"):
  #  hexVal = "00EEFF"
  r, g, b = hexVal[:2], hexVal[2:4], hexVal[4:]
  r, g, b = [int(n, 16) for n in (r, g, b)]
  return (r, g, b)


###############################################################################

def main():

  #binary_file = "./hello"
  binary_file = "./ls"
  hexString, binfile = GetHexStringFromFile(binary_file)
  hexArray = SplitToHexArray(hexString)
  print hexArray
  SIZE = int(math.sqrt(len(hexArray))) + 2

  img = Image.new( 'RGB', (SIZE, SIZE), "black") # create a new black image
  pixels = img.load() # create the pixel map

  i, j = 0,0
  for hexVal in hexArray:
    i+=1
    if (i % img.size[0] == 0):
      i = 0
      j += 1
    pixels[i,j] = getRGBTuple(hexVal)

  img.show()

  # Close the file:
  binfile.close()


if __name__ == '__main__':
  main()
