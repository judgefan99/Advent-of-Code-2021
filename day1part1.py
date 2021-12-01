#Makes a empty list and reads the file into it
lines = []
with open('day1.txt') as f:
    lines = f.readlines()

#makes a new list with newline characters stripped from each element
cleanlines = []

for element in lines:
    cleanlines.append(element.strip())


itcounter = 0 #iteration counter
answer = 0 #answer counter
for element in cleanlines:
    if itcounter == 0: #if it's the first element, do nothing
        pass
    else:
        if int(cleanlines[itcounter]) > int(cleanlines[itcounter - 1]): #check and see if it's bigger than the last element 
            answer = answer + 1 #if so, increment the counter

    itcounter = itcounter + 1 #increment the iteration counter
    
print(answer) #print the answer
