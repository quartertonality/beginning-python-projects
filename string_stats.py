def string_stats(s):
    upper_count = 0
    lower_count = 0
    chars_count = 0
    space_count = 0
    
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '<', '>', '?']
    space = [' ']
    
    for i in s:
        if i in upper:
            upper_count += 1
        elif i in lower:
            lower_count += 1
        elif i in chars:
            chars_count += 1
        elif i in space:
            space_count += 1
            
    print("Number of upper case letters is: ", upper_count) 
    print("Number of lower case letters is: ", lower_count)
    print("Number of special characters is: ", chars_count)
    print("Number of spaces is: ", space_count)
