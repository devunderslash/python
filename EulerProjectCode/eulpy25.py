# # Project Euler Problem 25 - https://projecteuler.net/problem=25

def compute():
# Since we know that the first two terms are going to be  1, 1 we can set the start points as follows
    term = 2 # term of two 
    seq = [1,1] # which contains [1,1] as beginning of the sequence

    # While the length of the second position number as a string is less than 1000 then continue loop
    while len(str(seq[1])) < 1000:
        term +=1 #Increase term (index) by 1

        # Replace sequence with the latest number in the first position and the sum of the two numbers
        # in the second position as the newest number 
        seq = [seq[1], seq[0] + seq[1]] 

    return (str(term))
    # print(seq)

if __name__ == "__main__":
	print(compute())