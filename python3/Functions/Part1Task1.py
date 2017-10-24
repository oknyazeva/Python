text1 = raw_input("Enter string1: ")
text2 = raw_input("Enter string2: ")


def remove_symbol(text1,text2):
    list1_text = list(text1)
    list2_text = list(text2)
    for i in range(len(list2_text)):
        j = 0
        while j < len(list1_text):
            if list2_text[i] == list1_text[j]:
                list1_text.remove(list1_text[j])
            else:
                j = j+1
    text1 = ''.join(list1_text)
    return text1
print remove_symbol(text1, text2)

# def remove_pasha(text1, text2):
#     print ''.join([i for i in set(text1) if i not in text2])
#
# remove_pasha(text1, text2)

