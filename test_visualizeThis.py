from nose import tools
import visualizeThis

def test_module_imports():
  print visualizeThis

def test_hex_split():
  hexString = "000000666666888888"
  hexArray = visualizeThis.SplitToHexArray(hexString)
  assert hexArray == ['000000', '666666', '888888']

def test_rgb_tuple():
  hexVal = 'FFFFFF'
  rgbVal = visualizeThis.getRGBTuple(hexVal)
  assert rgbVal == (255, 255, 255)

def test_file_loads():
  hexString, binfile = visualizeThis.GetHexStringFromFile()
  assert hexString
  assert binfile
