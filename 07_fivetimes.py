# for loops used to loop a specific number of times.
# the range function can be called with 1, 2, or 3 arguments
# break and continue statments can be used in for loops
print('My name is')
for i in range(5): # starting at 0 and ending at 4
    print('Jimmy Five Times '+str(i))

# how gauss added all the numbers from 1-100. 50 pairs of 100=5000, plus the final 50=5050
total=0
for num in range(101):
    total=total+num
    print(total)

#while loop equivalent of a for loop
print('my name is')
i=0
while i<5:
    print('jimmy five times '+str(i))
    i=i+1

# range can be called with multiple(3) arguments. seperated by commas. goes from 12, up to but not including 16.
print('my name is')
for i in range(12,16):
    print('jimmy five times '+str(i))

# range can be called with three arguments.
# the first argument is where the for loop starts
# the second, is where the for loop stops,(up to but not including)
# the third, is the step argument (how much the variable increases after each iteration)
print('my name is')
for i in range(0,10,2):
    print('jimmy five times '+str(i))

# can use a negative step argument to count down instead of up
print('my name is')
for i in range(5,-1,-1):
    print('jimmy five times '+str(i))