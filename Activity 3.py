def sum(n1,n2):
  return n1+n2

def diff(n1,n2):
  return n1-n2

def product(n1,n2):
  return n1*n2

def quo(n1,n2):
  return n2/n1

num1=int(input("Enter the First Number"))
num2=int(input("Enter the Second Number"))

print("Sum of {} and {} is {}".format(num1,num2,sum(num1,num2)))
print("Difference of {} and {} is {}".format(num1,num2,diff(num1,num2)))
print("Product of {} and {} is {}".format(num1,num2,product(num1,num2)))
print("Quotient of {} and {} is {}".format(num1,num2,quo(num1,num2)))
