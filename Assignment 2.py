## Task 1
a=int(input("Enter a number : "))
if a % 2==0 :
    print(f"{a} is an even number")
else :
    print(f"{a} is an odd number")


## Task 2
sum = 0
for i in range(1, 51):
    sum += i
print(f"The sum of integers from 1 to 50 is: {sum}")
