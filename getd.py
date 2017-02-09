p = input('Factor 1: ')
q = input('Factor 2: ')
e = input('e Value: ')
d = 0
found = False
i = 1

# your code starts here
PhiN = (p-1) * (q-1)
while(found != True):
    d = ((i*PhiN+1) / (e))
    if(((e * d) % PhiN) == 1):
        found = True
    i = i + 1
# your code ends here
print "Your Private key is:",d