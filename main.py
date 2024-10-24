def encode(code):
  encoded_code = ""
  for digit in code:
    digit = str(int(digit+3))
    encoded_code += digit
  return int(encoded_code)
