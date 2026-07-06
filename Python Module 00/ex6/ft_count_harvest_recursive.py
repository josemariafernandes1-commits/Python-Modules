def ft_count_harvest_recursive():
    starting_date = int(input("Days until harvest: "))
    harvest_count_report(starting_date)


def harvest_count_report(days_to_harvest, day=1):
    if day < days_to_harvest:
        print(f"Day {day}")
        return harvest_count_report(days_to_harvest, day + 1)
    print(f"Day {day}")
    return print("Harvest time!")


# if __name__ == "__main__":
#     insert_days()
