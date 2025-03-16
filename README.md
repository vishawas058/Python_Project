# Python Project

## Some Pattern whit python

1. half pyramid of stars (*)

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
2. full pyramid of stars (*)
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
3. inverted half pyramid of stars
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
4. inverted full pyramid of stars
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
5. print pattern of numbers
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
6. pattern 1 12 123...
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
7. pattern ...12345 1234 123 12 1
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
8. right half pyramid of numbers
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
# Decimal to Binary Converter 🚀

## Overview 🌟
This Python script is a simple yet robust tool designed to convert decimal (base-10) integers into their binary (base-2) representations. It supports positive integers, negative integers, and zero, with built-in error handling to ensure a smooth user experience! 😊

## Features ✨
- ✅ Converts positive and negative decimal integers to binary
- 🕸️ Special handling for zero input
- 🚦 Preserves sign for negative numbers
- ⚠️ Input validation with user-friendly error messages
- 📜 Clean, readable output format
- 🪶 Lightweight and easy to use

## Usage 🛠️
1. Ensure you have Python 3.x installed on your system 🐍
2. Save the script as `decimal_to_binary.py` 💾
3. Run the script from the command line:
```bash
python decimal_to_binary.py
```
4. Enter a decimal integer when prompted 

5. View the binary result displayed on the screen 

## Example Inputs and Outputs📋
Enter a decimal number: 13
Binary representation of 13 is: 1101

Enter a decimal number: -5
Binary representation of -5 is: -101

Enter a decimal number: 0
Binary representation: 0

Enter a decimal number: 42
Binary representation of 42 is: 101010

Enter a decimal number: abc
Please enter a valid integer 🚫

###### Output 
![Output](https://www.dropbox.com/scl/fi/ynxunl77rgeyelyyu0l0e/Decimal-To-Binary.jpg?rlkey=w3gu0t2a431yzs6hhglnsg4kk&st=6lqc3v9j&raw=1)
---
## How It Works🔍
The script follows these steps:
1. Input Collection: Uses input() to get a decimal number from the user📥

2. Error Handling: Wrapped in a try-except block to catch ValueError for non-integer inputs🛡

3. Special Case: Checks if the input is 0 and outputs "0" directly⚡️

4. Conversion Process:
    - Stores the original number for display📌

    - Uses abs() to handle negative numbers during conversion🔢

    - Implements the standard division-by-2 algorithm:
        - Repeatedly divides by 2➗️

        - Prepends remainders to build the binary string🧵
     -Adds a negative sign if the original input was negative 
5. Output: Prints the result using an f-string for clean formatting🖨
## Requirements📦
- Python 3.x (tested on Python 3.9+)🐍

- No external dependencies🎉
## Installation
1. Clone or download the script:
```bash
git clone <repository-url>
cd <repository-directory>
```
2. Run the script:

```bash
python decimal_to_binary.py
```
Alternatively, copy-paste the code into a `.py` file and run it directly!✂️📋

## Code Structure 💻

```python 
try:
    decimal = int(input("Enter a decimal number: "))  # User input ✍️
    if decimal == 0:  # Zero case ⚡
        print("Binary representation: 0")
    else:  # Non-zero numbers 🔢
        original_num = decimal
        binary = ""
        num = abs(decimal)
        while num > 0:  # Conversion loop 🔄
            binary = str(num % 2) + binary
            num //= 2
        if original_num < 0:  # Handle negative ➖
            binary = "-" + binary
        print(f"Binary representation of {original_num} is: {binary}")
except ValueError:  # Error handling 🚫
    print("Please enter a valid integer")
```

## Limitations 
- Only processes whole integers (no floating-point numbers) 🔍

- Limited by Python's integer size constraints 📏

- Does not support binary-to-decimal conversion (one-way only) ↔️
## Future Enhancements 🌈
Potential improvements could include:
⭐️ Support for floating-point decimal numbers

🔄 Option to convert binary back to decimal

🎊 Interactive mode with multiple conversions

✅️ Input validation for maximum integer size

🎨 Output formatting options (e.g., padding with zeros)
## Troubleshooting 🛠
- Error: "Please enter a valid integer": Ensure you enter a whole number, not text or decimals 🚫

- No output: Check that Python is installed and the script is running correctly ✅️

- Unexpected results: Verify the input is within reasonable integer bounds 📏
##Contributing 🤝
Feel free to fork this project and submit pull requests with improvements! Suggestions for enhancements or bug fixes are welcome via issues. ⭐️
## License 📝
This project is released under the MIT License (LICENSE). Feel free to use, modify, and distribute it as needed! 🆓️
## Author ✍️
Developed as a demonstration of basic number system conversion in Python. Contact via GitHub for questions or feedback. 🙌
## Acknowledgments ⭐️
- Inspired by classic computer science algorithms 💾

- Built with simplicity and education in mind 🎓


### Emoji Highlights 🎉
- Used 🚀, 🌟, and ✨ for emphasis and excitement
- Added 🐍 for Python references
- Included ✅, 🚫, and ⚠️ for status and warnings
- Used 🔍, 🔢, and ➗ for technical steps
- Sprinkled in 🤝, 🙌, and 🎓 for community and learning vibes

This version keeps all the detailed content while making it more fun and approachable with emojis! Let me know if you'd like adjustments or more emojis in specific places! 😄
---
