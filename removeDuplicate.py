# Remove Duplicates
array = [1, 9, 9, 8, 8, 7, 1, 1, 1, 5, 6]
no_duplicates_array = []

for x in array:
    if x not in no_duplicates_array:
        no_duplicates_array.append(x)
print(len(array))
print(no_duplicates_array)