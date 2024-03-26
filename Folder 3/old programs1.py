# Write a function that checks if a number is a prime number.
# The number is passed as a parameter.
# If the number is prime, return True, otherwise False

def is_prime_number(number):
  for i in range(2, int(number/2)):
    if number % i == 0:
      return False
  return True


print(is_prime_number(127))
