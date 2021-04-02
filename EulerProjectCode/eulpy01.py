# Project Euler Problem 1 or more commonly known as
# FizzBuzz - adding multiples of 3 and 5 up to 1000

def compute():
    result = sum(i for i in range(10000) 
        if (i % 3 == 0 or i % 5 ==0))

    return str(result)

if __name__ == "__main__":
    print(compute())
    