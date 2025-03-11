# Guess_Number
print("Hello Players Welcome to Guess The Right Number")
print("You have 10 attempts for guessing the Number")
print("So Good Luck Players\n")
n=19
j=1
i = 1
ng = 9
while j==1:
  while i<=9:
    g=int(input("Guess the Number: "))
    if g==n:
      print("You are absolutely right you won it")
      break
    else:
      ng -=1
      if ng==0:
        print("No. of guesses are left: ", ng)
        print("Your guessing number is over, you have lost.")
      else:
        if g > 20:
          print("Try with smaller numbers")
        elif g > n and g <= 20:
          print("You are very close, try with a smaller number")
        elif g >=15 and g < n:
          print("You are very close, try with a slightly higher number")
        elif g < 15:
          print("Try with bigger numbers")
      
        print("No. of guesses are left: ", ng)
      print('')
      i +=1
      continue
    i +=1
  j=int(input("If you want to continue press 1 to close 0 to expand: "))
  print("")
