# The following solution extracts all numbers (as single digits) 
# from the sample.txt file and sums them
xtract = open('sample.txt', 'r')
  
content = xtract.readlines()
  
sum = 0

for line in content: 
    for i in line:   
        if i.isdigit() == True:
              
            sum += int(i)
  
print("The sum is:", sum)