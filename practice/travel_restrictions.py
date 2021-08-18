io = open("travel_restrictions_input.txt").read().splitlines()
f = open("output.txt", 'w')

for x in range(int(io[0])):
    countries = int(io[x * 3 + 1])
    inbound = io[x * 3 + 2]
    outbound = io[x * 3 + 3]
    travel = []
    travel.append([0, 1, 1 if outbound[0] == 'Y' and inbound[1] == 'Y' else 0])
    for y in range(1, countries - 1):
        if outbound[y] == "Y":
            answer = []
            if inbound[y - 1] == "Y":
                answer.append(1)
            else:
                answer.append(0)
            answer.append(1)
            if inbound[y + 1] == "Y":
                answer.append(1)
            else:
                answer.append(0)
            travel.append(answer)
        else:
            travel.append([0, 1, 0])
    travel.append([1 if outbound[-1] == 'Y' and inbound[-2] == 'Y' else 0, 1, 0])
    final_output = []
    output = ["N"] * countries
    output[0] = "Y"
    i = 0
    while travel[i][-1] == 1:
        output[i + 1] = "Y"
        i += 1
        if i == len(travel) - 1:
            break
    final_output.append("".join(output))
    for z in range(1, countries - 1):
        output = ["N"] * countries
        i = z
        while travel[i][0] == 1:
            output[i - 1] = "Y"
            i -= 1
            if i == -1:
                break
        output[z] = "Y"
        while travel[z][-1] == 1:
            output[z + 1] = "Y"
            z += 1
            if z == len(travel):
                break
        final_output.append("".join(output))
    output = ["N"] * countries
    output[-1] = "Y"
    i = countries - 1
    while travel[i][0] == 1:
        output[i - 1] = "Y"
        i -= 1
        if i == -1:
            break
    final_output.append("".join(output))
    f.write(f"Case #{x + 1}:\n" + "\n".join(final_output) + "\n")
f.close()
