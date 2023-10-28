def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Find the minimum and maximum values in the input array
    min_val = min(arr)
    max_val = max(arr)

    # Create empty buckets
    num_buckets = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        index = num - min_val
        buckets[index].append(num)

    # Sort each bucket (you can use any sorting algorithm)
    sorted_buckets = []
    for bucket in buckets:
        sorted_buckets.extend(sorted(bucket))

    return sorted_buckets

# Example usage
arr = [3, 6, 1, 8, 2, 4]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
