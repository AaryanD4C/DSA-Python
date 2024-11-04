a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a>=b and a>=c :
   highest_number = a
elif b>=a and b>=c:
   highest_number = b
else:
   highest_number = c

print(f"The highest number is {highest_number}")