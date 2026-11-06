'''
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1

factorial(n) = n * n-1 * n-2...2 x 1
or
factorial(n) = n * factorial(n-1)

'''


def factorial(n):
  if(n==1 or n==0): #base condition so the factorial(1) is taken as 1 aand then the recursion stops calling itself.
    return 1
  return n * factorial(n - 1) #The defined function factorial Sees that it needs the factorial of n - 1, which is 4, so it pauses the function there and goes to retrieve the factorial of n - 1, which is 4. Then it realizes that it needs the factorial of 4 * n - 1, which is 3. It continues on until it gets the factorial of 1. Then the numbers add up, which is factorial of 2 * factorial(1), then 3 * factorial(2), up to 5 * factorial(4). 

n = int(input("Enter the number to find the factorial: "))
print(f"Factorial of {n} is {factorial(n)}")
