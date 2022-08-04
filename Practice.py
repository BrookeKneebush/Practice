c0 = int(input("Enter any integer that is non-negative and non-zero: "))
loops = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        print(int(c0))
        loops += 1
    else:
        if c0 % 2 != 0:
            c0 = (3 * c0) + 1
            print(int(c0))
            loops += 1

print("loops = " + str(loops))

