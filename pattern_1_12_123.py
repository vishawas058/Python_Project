#pattern 1 12 123..
def pattern_1_12_123(r):
  print("Print pattern 1 12 123 1234 12345...!")
  for i in range(1,r + 1):
    for j in range(1,i + 1):
      print(j, end = " ")
    print()
r = int(input(Enter the number))
pattern_1_12_123(r)
