
# Pyramid Pattern Generator
This repository contains a collection of Python scripts, each implementing a unique pyramid or triangular pattern using stars (`*`) or numbers. Each script is standalone, making it easy to run, modify, or integrate into other projects. These patterns are great for learning Python loops, pattern printing, or creating visual outputs.
## Features
The repository includes the following individual scripts:
1. `half_pyramid_of_stars.py` - Generates a right-aligned half pyramid of stars.
2. `full_pyramid_of_stars.py` - Generates a centered full pyramid of stars.
3. `inverted_half_pyramid_of_stars.py` - Generates an inverted right-aligned half pyramid of stars.
4. `inverted_full_pyramid_of_stars.py` - Generates an inverted centered full pyramid of stars.
5. `pattern_of_numbers.py` - Generates a triangular pattern with incrementing numbers.
6. `pattern_1_12_123.py` - Generates a pattern of numbers like 1, 12, 123, etc.
7. `pattern_12345_1234_123_12_1.py` - Generates a reverse triangular pattern of numbers.
8. `right_half_pyramid_of_numbers.py` - Generates a right-aligned half pyramid with numbers.
## Prerequisites
- Python 3.x installed on your system.
## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
```
2. Navigate to the project directory:
```bash
cd your-repo-name
```
## Usage
Each script can be executed independently:
1. Open a terminal in the repository folder.
2. Run the desired script:
```bash
python script_name.py
```
Replace script_name.py with the file you want (e.g., half_pyramid_of_stars.py).
3. Enter a number when prompted to define the number of rows for the pattern.
## Example Outputs
For an input of 5, here’s what each script outputs:
`half_pyramid_of_stars.py`
```
Half pyramid of stars!
* 
* * 
* * * 
* * * * 
* * * * * 
```
`full_pyramid_of_stars.py`
```

Full pyramid of stars!
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
```
`inverted_half_pyramid_of_stars.py`
```

Inverted half pyramid of stars!
* * * * * 
* * * * 
* * * 
* * 
* 
```
`inverted_full_pyramid_of_stars.py`
```

Inverted full pyramid of stars!
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
```
`pattern_of_numbers.py`
```

Print pattern of numbers!
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
```
`pattern_1_12_123.py`
```

Print pattern 1 12 123 1234 12345...!
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```
`pattern_12345_1234_123_12_1.py`
```

Print pattern ...12345 1234 123 12 1!
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1
```
`right_half_pyramid_of_numbers.py`
```
Right half pyramid of numbers!
    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5
```
## Project Structure
The repository contains the following files:
- half_pyramid_of_stars.py: Half pyramid of stars.
- full_pyramid_of_stars.py: Full pyramid of stars.
- inverted_half_pyramid_of_stars.py: Inverted half pyramid of stars.
- inverted_full_pyramid_of_stars.py: Inverted full pyramid of stars.
- pattern_of_numbers.py: Incremental number pattern.
- pattern_1_12_123.py: Sequential number pattern (1, 12, 123...).
- pattern_12345_1234_123_12_1.py: Reverse sequential number pattern.
- right_half_pyramid_of_numbers.py: Right-aligned number pyramid.
## Script Structure
Each file follows this format:
```python
def function_name(r):
    print("Pattern description!")
    # Loop logic for the pattern
    for i in range(r):
        # Inner loops for spacing and printing
        print()

if __name__ == "__main__":
    r = int(input("Enter the number: "))
    function_name(r)
```
The function name matches the file name (e.g., `half_pyramid_of_stars` in `half_pyramid_of_stars.py`).
## Customization
- Modify the end parameter in print() to change the separator between elements (e.g., from " " to "").
- Adjust the spacing or loop logic to alter the pattern’s appearance.
## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Add new patterns or improve existing ones.
3. Submit a pull request with your changes.
Suggestions for new patterns or bug fixes can be submitted via GitHub issues.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
## Contact
For questions or feedback, create an issue on GitHub or email [mangadivine.in@gmail.com(mailto:mangadivine.in@gmail.com)].
## Implementation Steps:
To align with this `README.md`, you need to:
1. Create eight separate `.py` files, each containing one function from your original code along with its `if __name__ == "__main__":` block. For example:
    - `half_pyramid_of_stars.py`:
```python
def half_pyramid_of_stars(r):
    print("Half pyramid of stars!")
    for i in range(r):
        for j in range(i + 1):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    r = int(input("Enter the number: "))
    half_pyramid_of_stars(r)
```
    - Repeat this for each function in its own file.
2. Replace [your-username/your-repo-name](https://github.com/vishawas058/Python_Project) with your actual GitHub repository URL.
Optionally, add a LICENSE file (e.g., MIT License).
3. If you need the full code for each file or further assistance, let me know!
