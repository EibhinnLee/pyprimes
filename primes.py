# Eibhinn Lee
# Computing to primes.

# My list of primes - TBD
P = []

# Loop through all of the numbers we.re checking for primality.
for i in range(2, 1000):
    # Assume that i is a prime
    isprime = True
    # Loop through all values from 2 up to but not including i
    for j in range(2, i):
        # See if j divides i
        if i % j == 0:
            #If it does, i isn't prime so exit the loop and indicate it's not prime
            isprime = False
            break
    # If i is prime, then append to P.    
    if isprime:
        P.append(i)

# Print out our list
print(P)        
