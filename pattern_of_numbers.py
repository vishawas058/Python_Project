#print pattern of numbers
def pattern_of_numbers(r):
  print("Print pattern of numbers!")
  num = 1
  for i in range(r):
    for j in range(i + 1):
      print(num, end = " ")
      num += 1
    print()
pattern_of_numbers(r)
