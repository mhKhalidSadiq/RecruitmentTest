## Add code below with answer clearly stated
## Add code below with answer clearly stated

#Written By: Khalid Sadiq (AI Engineer)
#Dated : 27/09/2022

def find_factorial(n):
  """
   input : Takes an integer as input
   output: Return factrial of the given nummber if its positive integer
  """

  if n<0:
    print("Sorry, Factorial does not exists for -ve numbers")
    return None   
  elif n==0:
    return 1 # Factorial of 0 is 1 
  else:
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact    

def find_digits_sum(digits):
   """
    input: Takes a number 
    output: return sum of all digits present in the nummber
   """
   if isinstance(digits, int): # Validation Check if input is not a number
    digits_string = str(digits) # converion to string to iterate over it
    sum = 0
    for digit in digits_string:
        sum += int(digit)
    print("Sum of digits   is {}".format(sum))
   else:
    print("Given input is not an integer")  

n=10 #Given number
factorial = find_factorial(n)
if factorial:
 print("Factorail of {0} is {1}".format(n,factorial))
 digits_sum = find_digits_sum(factorial)

##Output:
#Factorail of 10 is 3628800
#Sum of digits   is 27
