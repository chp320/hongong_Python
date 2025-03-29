output = ""

for i in range(9):
    for j in range(0, (i+1)):
        output += "*"
    output += "\n"

print(output.strip())
