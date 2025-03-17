#half pyramid of stars (*)
def half_pyramid_of_stars(r):
  print("Half pryamid of stars!")
  for i in range(r):
    for j in range(i+1):
      print("*", end = " ")
    print()
r = int(input(Enter the number))
half_pyramid_of_stars(r)
