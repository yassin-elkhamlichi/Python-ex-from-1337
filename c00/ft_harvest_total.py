def ft_harvest_total():
    total = 0
    for i in range(3):
        harvest_by_day = int(input(f"DAY {i+1} harvest: "))
        total += harvest_by_day
    print(f"Total harvest : {total}")

