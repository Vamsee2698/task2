def counters(s):
    counter_dic = {}
    result = ''
    for char in s:
        if char==' ':
            result+=char
        elif char not in counter_dic :
            result += char
            counter_dic[char] = 1
        else:
            counter_dic[char] += 1
            char = chr(ord(char) + (counter_dic[char] - 1))
            result += char

    print(result)
counters("My name is Hemavamsee Ramineni")