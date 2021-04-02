# # Project Euler Problem 25 - https://projecteuler.net/problem=25
# 
# The Fibonacci sequence runs as follows:
# The numbers increase by adding the latest 2 numbers in the sequence to get the next number.
# For example the sequence of 1, 1, 2, 3, 5, 8, 13 is produced like so in a simplified view:
#             1
#             1
#     1 + 1 = 2
#     1 + 2 = 3
#     2 + 3 = 5
#     3 + 5 = 8
#     5 + 8 = 13
#
# For this solution the index (term) of the first number to contain 1000 digits will be printed out

def compute():
# Since we know that the first two terms are going to be  1, 1 we can set the start points as follows
    term = 2 # term of two 
    seq = [1,1] # which contains [1,1] as beginning of the sequence

    # While the length of the second position is less than 1000 then continue loop
    while len(str(seq[1])) < 1000:
        term +=1 #Increase term (index) by 1

        #Replace sequence with the newest number in the first position and the sum of the two numbers in the second position
        seq = [seq[1], seq[0] + seq[1]] 

    return (str(term))
    # print(seq)

if __name__ == "__main__":
	print(compute())