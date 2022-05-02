def count_substring(string, sub_string):
    noOfOc = 0
    a,b,c = ".",".","."
    arr = []
    length = len(sub_string) -1
    for i in range(len(string)):
        if i < len(string)-length:
            arr.insert(i, [])
            for j in range(len(sub_string)):
                arr[i].append(string[i+j])
    i = 0
    while i != len(arr):
        if "".join(arr[i]) == sub_string:
            noOfOc += 1
        i+=1
    return noOfOc

def minion_game(string):
    cons = "BCDFGHJKLMNPQRSTVWXYZ"
    vowels = "AEIOU"
    comb = []
    for i in range(1, len(string)+2):
        comb.append(string[:i])
        for j in range(0, len(string)+2):
            if string[j:i] != "" and string[j:i] not in comb:
                comb.append(string[j:i])
    Stuart, Kevin = 0,0
    for x in comb[:-1]:
        if x[0] in cons:
            score = count_substring(string, x)
            Stuart+=score
        else:
            score = count_substring(string, x)
            Kevin+=score
    if Stuart > Kevin:
        print("Stuart", Stuart)
    elif Stuart == Kevin:
        print("Draw")
    else:
        print("Kevin", Kevin)
