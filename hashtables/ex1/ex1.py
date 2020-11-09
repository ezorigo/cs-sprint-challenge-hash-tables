def get_indices_of_item_weights(weights, length, limit):
    
    cache = {}

    for i in range(0, length):
        current = weights[i]

        if current in cache:
            cache_index = cache[current]
            return (i, cache_index)
        
        cache[limit - current] = i

    return None
