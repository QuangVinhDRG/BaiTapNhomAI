text = input()
k = int(input()) #Key

str_result = ""

for char in text:
  if ord(char) >= 97 and ord(char) <= 122:
    str_result = str_result + chr((ord(char) - 97 + k) % 26 + 97)
  elif ord(char) >= 65 and ord(char) <= 90:
    str_result = str_result + chr((ord(char) - 65 + k) % 26 + 65)
  else:
    str_result = str_result + char

print(str_result)