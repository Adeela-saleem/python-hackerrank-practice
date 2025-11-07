if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # remove duplicates using set
    unique_scores = list(set(arr))
    # sort the list
    unique_scores.sort()
    # print the second last number (runner-up)
    print(unique_scores[-2])
