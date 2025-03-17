#inverted full pyramid of stars
def inverted_full_pyramid_of_stars(r):
  print("Inverted full pyramid of stars!")
  for i in range(r):
    for j in range(i):
      print(" ", end = "")
    for j in range(i, r):
      print("*", end = " ")
    print()
r = int(input(Enter the number))
inverted_full_pyramid_of_stars(r)
