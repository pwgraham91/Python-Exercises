def reverse(string):
    list_string = list(string)
    len_string = len(string)
    counter = 0
    while counter * 2 < len_string:
        left = list_string[counter]
        right_index = len_string - counter - 1
        right = list_string[right_index]
        list_string[counter] = right
        list_string[right_index] = left
        counter += 1
    return "".join(list_string)

print(reverse("abcd"))
print(reverse("antonio"))
