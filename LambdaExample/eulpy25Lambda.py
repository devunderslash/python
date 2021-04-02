def lambda_handler(event, context):
    term = 2 
    seq = [1,1] 
    while len(str(seq[1])) < 1000:
        term +=1 
        seq = [seq[1], seq[0] + seq[1]] 

    print(seq)