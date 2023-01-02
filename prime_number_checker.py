def prime_checker(number):
    is_prime = True
    for i in range(2, number): # the idea is to check if the number can be devided to any of the numbers up to but not equal to the number
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's NOT a prime number.")

n = int(input("Please write down the number you'd like to check out: "))
prime_checker(number=n)