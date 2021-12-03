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
    if itcounter == 0 or itcounter == 2000 or itcounter == 1999 or itcounter == 1998: #if it's the first element, do nothing
        pass
    else:
        x = int(int(cleanlines[itcounter]) + int(cleanlines[itcounter+1]) + int(cleanlines[itcounter +2]))
        y = int(int(cleanlines[itcounter-1]) + int(cleanlines[itcounter]) + int(cleanlines[itcounter +1]))

        if x > y:
            answer = answer + 1
            #print('yes')
        else:
            pass
            #print('no')


    itcounter = itcounter + 1
print(answer)
#print(answer) #print the answer
