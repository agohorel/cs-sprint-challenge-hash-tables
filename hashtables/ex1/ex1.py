def get_indices_of_item_weights(weights, length, limit):
    hashtable = {}

    # edge case if there aren't enough packages
    if length < 2:
        return None

    for idx,weight in enumerate(weights):
        if weight not in hashtable:
            hashtable[weight] = [idx]
        else:
            hashtable[weight].append(idx)

    for weight in hashtable:
        diff = limit - weight
        
        # edge case if weights are identical
        if diff == weight:
            if hashtable[weight][0] > hashtable[weight][1]:
                return (hashtable[weight][0], hashtable[weight][1])
            else:
                return (hashtable[weight][1], hashtable[weight][0])

        if diff in hashtable:
            second_item = hashtable[diff]

            if hashtable[weight][0] > second_item[0]:
                return (hashtable[weight][0], second_item[0])
            else:
                return (second_item[0], hashtable[weight][0])
    

    return None