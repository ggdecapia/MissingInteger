A = [1, 3, 6, 4, 1, 2]
#A = [1, 2, 3]

# sort the given array
# eliminate duplicates
nodupe_array = sorted(set(A))
    
# set 1 as default small int
smallest_int = 1
    
len_array = len(nodupe_array)
    
# iterate within the array
for n in range (len_array):
    # if negative, skip
    if nodupe_array[n] > 0:
        # else if A[n] = smallest_int
        if nodupe_array[n] == smallest_int:
            # smallest_int += 1
            smallest_int += 1
        # else if A[n] > smallest_int
        else:
            # return smallest_int
            print(smallest_int)
            break
                
print(smallest_int)