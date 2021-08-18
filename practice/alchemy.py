io = open("alchemy_input.txt").read().splitlines()
f = open("output.txt", 'w')

for x in range(int(io[0])):
    f.write(f"Case #{x + 1}: {'Y' if abs(io[x * 2 + 2].count('A') - io[x * 2 + 2].count('B')) == 1 else 'N'}\n")
f.close()
