#Python Project
##Some Pattern whit python
```python
#half pyramid of stars (*)
def half_pyramid_of_stars(r):
  print("Half pryamid of stars!")
  for i in range(r):
    for j in range(i+1):
      print("*", end = " ")
    print()

#full pyramid of stars (*)
def full_pyramid_of_stars(r):
  print("full pryamid of stars!")
  for i in range(r):
    for j in range(- r - 1, - i):
      print(" ", end = "")
    for j in range(i + 1):
      print("*", end = " ")
    print()

#inverted half pyramid of stars
def inverted_half_pyramid_of_stars(r):
  print("Inverted half pyramid of stars!")
  for i in range(r):
    for j in range(i, r):
      print("*", end = " ")
    print()

#inverted full pyramid of stars
def inverted_full_pyramid_of_stars(r):
  print("Inverted full pyramid of stars!")
  for i in range(r):
    for j in range(i):
      print(" ", end = "")
    for j in range(i, r):
      print("*", end = " ")
    print()

#print pattern of numbers
def pattern_of_numbers(r):
  print("Print pattern of numbers!")
  num = 1
  for i in range(r):
    for j in range(i + 1):
      print(num, end = " ")
      num += 1
    print()

#pattern 1 12 123..
def pattern_1_12_123(r):
  print("Print pattern 1 12 123 1234 12345...!")
  for i in range(1,r + 1):
    for j in range(1,i + 1):
      print(j, end = " ")
    print()

#pattern ...12345 1234 123 12 1
def pattern_12345_1234_123_12_1(r):
  print("Print pattern ...12345 1234 123 12 1!")
  for i in range(r+1,0,-1):
    for j in range(1,i):
      print(j, end = " ")
    print()
    
#right half pyramid of numbers
def right_half_pyramid_of_numbers(r):
  print("Right half pyramid of numbers!")
  for i in range(1, r + 1):
      print(" " * (r - i), end=" ")
      for j in range(1, i + 1):
        print(j, end=" ")
      print()

if __name__ == "__main__":
  r = int(input("Enter the number: "))
  half_pyramid_of_stars(r) 
  full_pyramid_of_stars(r)
  inverted_half_pyramid_of_stars(r)
  inverted_full_pyramid_of_stars(r)
  pattern_of_numbers(r)
  pattern_1_12_123(r)
  pattern_12345_1234_123_12_1(r)
  right_half_pyramid_of_numbers(r)
