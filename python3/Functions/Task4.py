text1 = raw_input("Enter string1: ")
text2 = raw_input("Enter string2: ")


def remove_symbol(text1, text2):
    new_list = []
    for i in text1:
        if i not in text2:
            new_list.append(i)
    return ''.join(new_list)

print remove_symbol(text1, text2)
