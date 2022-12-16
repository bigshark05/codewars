


#solution

def solution(s):
    if len(s) == 0:
        return []
    splitted_list = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(splitted_list[-1]) != 2:
        last_element = s[-1] + "_"
        splitted_list.remove(s[-1])
        splitted_list.insert(int(len(s)),last_element)
        return splitted_list
    else:
        return splitted_list