def intersection(arrays):
    hashtable = {}
    result = []

    for array in arrays:
        for el in array:
            if el not in hashtable:
                hashtable[el] = 1
            else:
                hashtable[el] += 1
    
    for val in hashtable:
        if hashtable[val] == len(arrays):
            result.append(val)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
