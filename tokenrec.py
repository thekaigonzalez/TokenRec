
toks = '! @ # $ % ^ & * ( ) < > ? . , ` / { } ; : - _ + \' "'

def dict_toks(tolex):
    di = {}
    buf  =""
    for i in range(len(tolex)):
        if (tolex[i] in toks.split()):
            di[tolex[i]] = 'TOKEN'
            di[buf.strip()] = tolex[i] + '_subtext'
            buf = ""
        else:
            buf += tolex[i]
    return di

print(dict_toks("hello * world /"))