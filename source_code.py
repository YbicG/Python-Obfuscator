import codecs
import __main__ as m
print("\033[0;32mMade by A&C Development: YbicG#1258 on Discord\033[0m'\n")
x = input("Enter the code: ")
#encode
def obfuscate(input):
  byte = bytes(input, "utf-8")
  hexEn = byte.hex()
  return hexEn
#test
#decode
def bajesk(input):
  binary_string = codecs.decode(input, "hex")
  res = str(binary_string, 'utf-8')
  return res

file = open(m.__file__+".txt", "a+")
file.write(obfuscate(x))
file.close()
      
exec(bajesk(obfuscate(x)))
print("\nResult: "+obfuscate(x))