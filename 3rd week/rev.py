word = "aajuaappaaa"
# {aa : 2, pp : 1}

res = {}
i = 0
while i < range(len(word)):
    if word[i] == word[i+1]:
        if f'{word[i]}{word[i]}' not in res:
            res[f'{word[i]}{word[i]}'] = 1
        else:
            res[f'{word[i]}{word[i]}'] += 1
            