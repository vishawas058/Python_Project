#pattern ...12345 1234 123 12 1
def pattern_12345_1234_123_12_1(r):
  print("Print pattern ...12345 1234 123 12 1!")
  for i in range(r+1,0,-1):
    for j in range(1,i):
      print(j, end = " ")
    print()
r = int(input(Enter the number))
pattern_12345_1234_123_12_1(r)
