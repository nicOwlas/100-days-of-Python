import pandas


def main():
    # Split Character
    name = "Nicolas"
    letters_list = [letter for letter in name]
    print(letters_list)

    # Multiply list by 2
    print([2 * n for n in range(1, 5)])

    # Filter even
    numbers = [1, 1, 2, 3, 6, 89, 124]
    even_numbers = [number for number in numbers if number % 2 == 0]
    print(even_numbers)

    # Find duplicates
    with open("./file1.txt") as file:
        list1 = file.readlines()

    with open("./file2.txt") as file:
        list2 = file.readlines()

    duplicates = [int(number) for number in list2 if number in list1]
    print(sorted(duplicates))


if __name__ == main():
    main()
