
#Reverse text in the line but keep order of words

line = input("Stick it in here: ")

line = line.rsplit()
output = []

for i in range(line.__len__()):
    output.append(line[i][::-1])
    output.append(" ")
    print(line[i][::-1])

print("The output: ",str().join(output))

