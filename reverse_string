def reverse(string):
    str_list=list(string)
    length = len(string)
    half = int(length/2)
    
    
    for i, char in enumerate(str_list):
        last_char = str_list[length-1]
        str_list[length-1] = char
        str_list[i] = last_char
        length = length-1
        if i >= half-1:
            break;
    
        
    return ''.join(str_list)


print(reverse('Hi, my name is Pavel!'))
