def compound(principle, rate, cycles, add_money=0):
    money_chart = [principle]
    print(money_chart[-1])
    for i in range(cycles):
        last_money = money_chart[-1]
        last_money += add_money
        money_chart.append(last_money * rate)
        print(money_chart[-1])

    own_money = principle + (add_money * cycles)
    print('own money: {}'.format(own_money))
    net_gain = money_chart[-1] - own_money
    print('net gain: {}'.format(net_gain))
    print('total percentage return: {}%'.format(int((net_gain / own_money) * 100)))


compound(0, 1.0122, 24, 1500)
