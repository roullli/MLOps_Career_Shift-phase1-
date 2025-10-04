from random import randint, seed

def main() -> None:
    seed(23)

    my_list = [randint(1, 100) for _ in range(15)]

    print(sum(my_list))
    print(max(my_list))
    print(min(my_list))

    ages = {"Ali": 25, "Reza": 35, "Negar": 28}
    oldest = max(ages, key=ages.get)
    youngest = min(ages, key=ages.get)
    print(f"Oldest person is named {oldest} and He/She is {ages[oldest]}")
    print(f"Youngest person is named {youngest} and He/She is {ages[youngest]}")

    ## Tuple unpacking

    persons = (("Dan", 23), ("Jukka", 32), ("Rouhollah", 36))

    for name, age in persons:
        print(f"{name} is {age} years old!")

    ## Set Operations (Union, Intersection, Difference, Symmetric Difference)

    set_a = {1, 2, 3, 3, 4, 2}
    set_b = {3, 3, 4, 5, 6, 6, 6}

    print(sorted(set_a))
    print(set_b)

    set_a_b_union = set_a | set_b  # OR set_a.union(set_b)
    set_a_b_intersect = set_a & set_b  # OR set_a.intersection(set_b)
    set_a_b_diff = set_a - set_b  # OR set_b.difference(set_a) !!!Here the order matters!!!
    set_a_b_symdiff = set_a ^ set_b  # OR set_a.symmetric_difference(set_b)

    print(set_a_b_union)
    print(set_a_b_intersect)
    print(set_a_b_diff)
    print(set_a_b_symdiff)

if __name__ == '__main__':
    main()