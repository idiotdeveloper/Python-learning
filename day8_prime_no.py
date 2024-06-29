def prime_no(num):
    counter = 0 
    for i in range(1, num+1):
        if (num % 1 == 0 and num % i == 0):
            print("prime number", i)
            counter += 1
        
    
    if counter > 2:
        print("not a prime number")
    
    else: 
        print("prime number")


n = int(input("your number :: "))
prime_no(num=n)