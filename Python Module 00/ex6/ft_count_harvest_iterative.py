def ft_count_harvest_iterative():
    starting_date = int(input("Days until harvest: "))
    day = 0
    for day in range(1, starting_date):
        print(f"Day {day}")
    print(f"Day {day + 1}")
    print("Harvest time!")


# if __name__ == "__main__":
#     ft_count_harvest_iterative()
