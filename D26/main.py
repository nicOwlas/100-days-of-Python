import random


def main():
    # Split Character
    name = "Nicolas"
    letters_list = [letter for letter in name]
    # print(letters_list)

    # Multiply list by 2
    # print([2 * n for n in range(1, 5)])

    # Filter even
    numbers = [1, 1, 2, 3, 6, 89, 124]
    even_numbers = [number for number in numbers if number % 2 == 0]
    # print(even_numbers)

    # 1 List comprehensions
    with open("./file1.txt") as file:
        list1 = file.readlines()

    with open("./file2.txt") as file:
        list2 = file.readlines()

    duplicates = [int(number) for number in list2 if number in list1]
    # print(sorted(duplicates))

    # 2 Dic comprehensions
    students = ["mark", "jacob", "nicolas", "anton", "elodie", "julia"]
    students_scores = {student: random.randint(0, 100) for student in students}
    students_passed = {
        student: score for (student, score) in students_scores.items() if score > 50
    }
    # print(students_scores)
    # print(students_passed)

    # 3 Dic comprehensions bis
    sentence = "The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, while sorted() doesn't change the list and returns the sorted list."
    letters_count = {word: len(word) for word in sentence.split(" ")}
    # print(letters_count)

    # 4 Dic comprehension ter
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    weather_f = {day: temp_c * 9 / 5 + 32 for (day, temp_c) in weather_c.items()}
    print(weather_f)


if __name__ == "__main__":
    main()
