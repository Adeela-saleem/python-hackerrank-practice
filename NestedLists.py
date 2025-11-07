if __name__ == '__main__':
    students = []

    # Input number of students
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Extract all scores and find the second lowest
    scores = sorted(set([s[1] for s in students]))
    second_lowest = scores[1]

    # Print all names with the second lowest score
    result = sorted([s[0] for s in students if s[1] == second_lowest])

    for name in result:
        print(name)
