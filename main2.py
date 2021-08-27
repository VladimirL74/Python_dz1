percent = 1
while percent <= 100:
    if (percent % 10) == 1 and percent != 11:
        print('{} процент'.format(percent))
    elif percent == 11 or percent == 12 or percent == 13 or percent == 14:
        print('{} процентов'.format(percent))
    elif (percent % 10) == 2 or (percent % 10) == 3 or (percent % 10) == 4:
        print('{} процента'.format(percent))
    else:
        print('{} процентов'.format(percent))
    percent += 1
