def has_negatives(a):
    result = []
    hashtable = {}

    for num in a:
        hashtable[num] = None

    for num in a:
        if num*-1 in hashtable and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
