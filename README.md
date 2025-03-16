# Python Project
## Some Pattern whit python

### 1. half pyramid of stars (*)
```Python
def half_pyramid_of_stars(r):
  print("Half pryamid of stars!")
  for i in range(r):
    for j in range(i+1):
      print("*", end = " ")
    print()
```
### 2. full pyramid of stars (*)
```python
def full_pyramid_of_stars(r):
  print("full pryamid of stars!")
  for i in range(r):
    for j in range(- r - 1, - i):
      print(" ", end = "")
    for j in range(i + 1):
      print("*", end = " ")
    print()
```

### 3. inverted half pyramid of stars
```python
def inverted_half_pyramid_of_stars(r):
  print("Inverted half pyramid of stars!")
  for i in range(r):
    for j in range(i, r):
      print("*", end = " ")
    print()
```

### 4. inverted full pyramid of stars
```python
def inverted_full_pyramid_of_stars(r):
  print("Inverted full pyramid of stars!")
  for i in range(r):
    for j in range(i):
      print(" ", end = "")
    for j in range(i, r):
      print("*", end = " ")
    print()
```

### 5. print pattern of numbers
```python
def pattern_of_numbers(r):
  print("Print pattern of numbers!")
  num = 1
  for i in range(r):
    for j in range(i + 1):
      print(num, end = " ")
      num += 1
    print()
```

### 6. pattern 1 12 123...
```python
def pattern_1_12_123(r):
  print("Print pattern 1 12 123 1234 12345...!")
  for i in range(1,r + 1):
    for j in range(1,i + 1):
      print(j, end = " ")
    print()
```

### 7. pattern ...12345 1234 123 12 1
```python

def pattern_12345_1234_123_12_1(r):
  print("Print pattern ...12345 1234 123 12 1!")
  for i in range(r+1,0,-1):
    for j in range(1,i):
      print(j, end = " ")
    print()
    
```
### 8. right half pyramid of numbers
```python

def right_half_pyramid_of_numbers(r):
  print("Right half pyramid of numbers!")
  for i in range(1, r + 1):
      print(" " * (r - i), end=" ")
      for j in range(1, i + 1):
        print(j, end=" ")
      print()

```
### calling functions
```python

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
```
