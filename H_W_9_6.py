crypt = {
    'a' : 123, 'b' : 456, 'c' : 789, 'd' : 101, 'e' : 102, 'f' : 103, 'g' : 104,
    'h' : 105, 'i' : 106, 'j' : 107, 'k' : 108, 'l' : 109, 'm' : 110, 'n' : 111,
    'o' : 112, 'p' : 113, 'q' : 114, 'r' : 115, 's' : 116, 't' : 117, 'u' : 118,
    'v' : 120, 'w' : 121, 'x' : 122, 'y' : 124, 'z' : 125
    }

del_a = '%'
del_w = '&'
phrase = input('Введите фразу: ')
code_phr = ''
for _p in phrase:
    code_phr += str(crypt.get(_p, '')) + (del_w if _p == ' ' else del_a)
print('Кодированная фраза : ', code_phr)

decode_phr = ''
tmp_str = ''
for i in range(len(code_phr)):
    if (code_phr[i] != del_a and code_phr[i] != del_w):
        tmp_str += code_phr[i]
    else:
        if code_phr[i] == del_a:
            for k,v in crypt.items():
                if tmp_str == str(v):
                    decode_phr += k
        else:
            decode_phr += ' '
        tmp_str = ''
print('Лекодированная фраза : ', decode_phr)
