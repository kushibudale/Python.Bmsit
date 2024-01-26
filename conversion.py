#Develop a python program to convert binary to decimal, octal to hexadecimal using functions. 
def binary_to_decimal(binary):
      decimal = int(binary, 2)
      return decimal
def octal_to_hexadecimal(octal):
       decimal = int(octal, 8)
       hexadecimal = hex(decimal)
       return hexadecimal
binary_input = input("Enter a binary number: ")
octal_input = input("Enter an octal number: ")
decimal_result = binary_to_decimal(binary_input)
print("Decimal representation:",decimal_result)
hexadecimal_result=octal_to_hexadecimal(octal_input)
print("Hexadecimal representation:",hexadecimal_result)
