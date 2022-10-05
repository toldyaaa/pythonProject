s = input()
if s.isdigit():
    if len(s) != 16:
        print("error")
    else:
        sum_1 = 0
        for i in range(0, len(s), 2):
            n = int(s[i])
            if n * 2 > 9:
                sum_1 = sum_1 + (n * 2 - 9)
            else:
                sum_1 = sum_1 + n * 2
        sum_2 = 0
        for i in range(1, len(s), 2):
            n = int(s[i])
            sum_2 = sum_2 + n * 2

        if (sum_1 + sum_2 ) % 10 == 0:
            print("correct")
        else:
            print("error")
else:
    print("error")


