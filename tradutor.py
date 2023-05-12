s = input("Qual o numero a ser traduzido: ")
i = len(s) - 1
resultado = 0
number = 0
prev = 0

for x in s[::-1]:
  if x == 'M':
    number = 1000
  elif x == 'D':
    number = 500
  elif x == 'C':
    number = 100
  elif x == 'L':
    number = 50
  elif x == 'X':
    number = 10
  elif x == 'V':
    number = 5
  elif x == 'I':
    number = 1

  if number < prev:
    resultado = resultado - number
  else:
    resultado = resultado + number
  prev = number

print(f"O algarismo romano {s} é equivalente ao {resultado} nos naturais.")
