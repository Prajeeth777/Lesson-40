def fact(num):
  if num==1:
    return num
  else:
    return num*fact(num-1)

number=int(input("Enter a number"))
if number<0:
  print("Cannot find factorials for negative numbers")
elif number==0:
  print("Factorial of 0 is 1")
else:
  print("Factorial of ",number," is "fact(number))
