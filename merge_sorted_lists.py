def merge_sorted_lists(list_1, list_2):
    merged_list = []
    long_list = []
    short_list = []
    
    if len(list_1) >= len(list_2):
        long_list = list_1
        short_list = list_2
    else:
        long_list = list_2
        short_list = list_1
    
    j = 0
    max_length = len(short_list)-1
        
    for i, item in enumerate(long_list):
        while item >= short_list[j]:
            merged_list.append(short_list[j])
            if j == max_length:
                break;
            else:
                j = j + 1

        merged_list.append(item)
    
    return merged_list


my_list_1 = [0, 3, 4, 31]
my_list_2 = [4, 6, 30]


print(merge_sorted_lists(my_list_1, my_list_2))
