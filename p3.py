def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n = n // i
        else:
            i += 1
    return n
    
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(largest_prime_factor(number))
    