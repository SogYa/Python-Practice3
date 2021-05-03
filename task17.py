def lucky(ticket):
    global lastTicket
    while ticket < 100000:
        ticket *= 10
    if (sum(map(int, str(lastTicket)[0:3])) == sum(map(int, str(lastTicket)[3:6])) and
            sum(map(int, str(ticket)[0:3])) == sum(map(int, str(ticket)[3:6]))):
        return 'Счастливый'
    else:
        return 'Несчастливый'


lastTicket = 123321
print(lucky(100001))