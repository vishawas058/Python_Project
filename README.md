# Python Project
---
## Some Pattern whit python

- half pyramid of stars (*)

```Python
def half_pyramid_of_stars(r):
  print("Half pryamid of stars!")
  for i in range(r):
    for j in range(i+1):
      print("*", end = " ")
    print()
```
###### Output
![Output](https://www.dropbox.com/scl/fi/5m2n0hy01nnvqugscyt8a/1.jpg?rlkey=86imvglm9ir6wkopt76zi1874&st=msj9d1mw&raw=1)
---
- full pyramid of stars (*)
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
###### Output
![Output](https://www.dropbox.com/scl/fi/psaq4ntp542n8xzczfi2d/2.jpg?rlkey=1sl79o70thqu9smwhs3l74rvj&st=51ntwi00&raw=1)
---
- inverted half pyramid of stars
```python
def inverted_half_pyramid_of_stars(r):
  print("Inverted half pyramid of stars!")
  for i in range(r):
    for j in range(i, r):
      print("*", end = " ")
    print()
```
###### Output
![Output](https://www.dropbox.com/scl/fi/oqqxi4k7a3dfq2jz0j3un/3.jpg?rlkey=nlbgghu52iog4v6t9phzekjtx&st=ro0ryrmz&raw=1)
---
- inverted full pyramid of stars
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
###### Output
![Output](https://www.dropbox.com/scl/fi/oh3x04y70kka68gw0kavb/4.jpg?rlkey=0ky60q915nkxu68qdxagv6n27&st=x03dgk9u&raw=1)
---
- print pattern of numbers
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
###### Output
![Output](https://www.dropbox.com/scl/fi/vk5tnnugxvknhsdxvdgqt/5.jpg?rlkey=ry2t5rkhvvhnsgvez3u3bpt7e&st=3zc969am&raw=1)
---
- pattern 1 12 123...
```python
def pattern_1_12_123(r):
  print("Print pattern 1 12 123 1234 12345...!")
  for i in range(1,r + 1):
    for j in range(1,i + 1):
      print(j, end = " ")
    print()
```
###### Output
![Output](https://www.dropbox.com/scl/fi/zg011qw6qoom45viyn1c3/6.jpg?rlkey=kbldd4hv6axhnz5spt12u7014&st=kcjjr4wg&raw=1)
---
- pattern ...12345 1234 123 12 1
```python

def pattern_12345_1234_123_12_1(r):
  print("Print pattern ...12345 1234 123 12 1!")
  for i in range(r+1,0,-1):
    for j in range(1,i):
      print(j, end = " ")
    print()
```
###### Output 
![Output](https://www.dropbox.com/scl/fi/4r95apurgvt4l66gudb1i/7.jpg?rlkey=pmx7v4wjhz8xjn9oujm7g22ih&st=ank9tneb&raw=1)
---
- right half pyramid of numbers
```python

def right_half_pyramid_of_numbers(r):
  print("Right half pyramid of numbers!")
  for i in range(1, r + 1):
      print(" " * (r - i), end=" ")
      for j in range(1, i + 1):
        print(j, end=" ")
      print()

```
###### Output 
![Output](https://www.dropbox.com/scl/fi/wkl3z8eg1w4xd0iad1az6/8.jpg?rlkey=xhb6gkahp2oez9d4e59c88qmy&st=nr403jqu&raw=1)

- calling functions
```python
---
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
---
## Decimal To Binary

```python
# Get input from user
try:
    decimal = int(input("Enter a decimal number: "))

    # Handle zero case
    if decimal == 0:
        print("Binary representation: 0")
    else:
        # Store original number for final output
        original_num = decimal
        binary = ""
        num = abs(decimal)  # Handle negative numbers

        # Conversion loop
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2

        # Add negative sign if original number was negative
        if original_num < 0:
            binary = "-" + binary

        print(f"Binary representation of {original_num} is: {binary}")

except ValueError:
    print("Please enter a valid integer")
```
###### Output 
![Output](https://www.dropbox.com/scl/fi/ynxunl77rgeyelyyu0l0e/Decimal-To-Binary.jpg?rlkey=w3gu0t2a431yzs6hhglnsg4kk&st=6lqc3v9j&raw=1)