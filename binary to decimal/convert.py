def converter(number):
    pos = -1
    multi = 1
    total = 0

    while pos >= -len(number):
        try:
            a = int(number[pos])
        except:
            total = "PLEASE ENTER A BINARY NUMBER"
            break
        if int(number[pos]) == 0:
            pass
        elif int(number[pos]) == 1:
            pass
        else:
            total = "PLEASE ENTER A BINARY NUMBER"
            break
        rightNow = int(number[pos]) * multi
        total += rightNow
        pos -= 1
        multi *= 2

    print(f"Number in decimal: {total}")
