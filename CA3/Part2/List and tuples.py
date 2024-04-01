import timeit

# Function to measure time for different operations on a list
def measure_list_operations(N):
    setup_code = f"my_list = list(range({N}))"

    # Time for deleting last element using pop()
    delete_last_time = timeit.timeit("my_list.pop()", setup=setup_code, number=1000)

    # Time for deleting first element using pop(0)
    delete_first_time = timeit.timeit("my_list.pop(0)", setup=setup_code, number=1000)

    # Time for appending 1 at the end of the list
    append_time = timeit.timeit("my_list.append(1)", setup=setup_code, number=1000)

    # Time for inserting 1 at the beginning of the list
    insert_time = timeit.timeit("my_list.insert(0, 1)", setup=setup_code, number=1000)

    return delete_last_time, delete_first_time, append_time, insert_time

# List of different sizes
sizes = [10000, 20000, 30000]

# Measure time for each operation for each size
results = {}
for size in sizes:
    results[size] = measure_list_operations(size)

# Print the results in a table format
print("N\tDelete Last\tDelete First\tAppend\tInsert")
for size in sizes:
    delete_last_time, delete_first_time, append_time, insert_time = results[size]
    print(f"{size}\t{delete_last_time:.6f}\t{delete_first_time:.6f}\t{append_time:.6f}\t{insert_time:.6f}")

####################################################
    
