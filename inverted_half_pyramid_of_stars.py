#inverted half pyramid of stars
def inverted_half_pyramid_of_stars(r):
  print("Inverted half pyramid of stars!")
  for i in range(r):
    for j in range(i, r):
      print("*", end = " ")
    print()
inverted_half_pyramid_of_stars(r)
