#right half pyramid of numbers
def right_half_pyramid_of_numbers(r):
  print("Right half pyramid of numbers!")
  for i in range(1, r + 1):
      print(" " * (r - i), end=" ")
      for j in range(1, i + 1):
        print(j, end=" ")
      print()
r = int(input(Enter the number))
right_half_pyramid_of_numbers(r)
