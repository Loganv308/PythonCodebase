values = []

with open('Day1.txt', 'r') as f:
    
    lines = f.readlines()

sum = 0

print("Instance #1 of sum variable: " + str(sum))

for line in lines:
    
    if line == '\n':
        
        print(sum)
        
        values.append(sum)
        
        sum = 0
    
    else:

        numbers = line.split()

        for number in numbers:

            sum += int(number)

values.append(sum)

values.sort()

for i in range(0,3):
    
    sum = 0
    
    values[i] +=sum

    print(sum)

print(values)