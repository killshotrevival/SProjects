def frequencies(s):
    l = []
    s1 = list(set(s))
    s1.sort()
    for i in s1:
        l.append((i,s.count(i)))
    return l

# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(fre, s1):
    if s1:
        if fre:
            final_dic={}
            s = set(s1)
            #fre.sort(key = lambda x: x[1], reverse=True)
            while(len(fre)>2):
                p1 = fre.pop()
                p2 = fre.pop()
                fre.append([p2,p1])
            for i in s:
                strind = ''
                j = fre
                while(True):
                    if j[0][0]==i:
                        strind+='0'
                        final_dic[i]=strind
                        break
                    else:
                        strind+='1'
                        j=j[1]
                        if type(j)!=list:
                            if i==j[0][0]:
                                final_dic[i]=strind
                                break
            final_str = ''
            for i in s1:
                final_str+=final_dic[i]
            print(final_dic)
            return final_str
        else:
            return ''
    else:
        return None


def decode(fre,s1):
    final_dic={}
    fre.sort(key = lambda x: x[1], reverse=True)
    while(len(fre)>2):
        p1 = fre.pop()
        p2 = fre.pop()
        fre.append([p2,p1])
    print(fre)

    final_str=''
    i=0
    while (i<len(s1)):
        j=fre
        while True:
            if s1[i]=='0':
                final_str+=j[0][0]
                i+=1
                break
            else:
                if type(j[1])!=list:
                    final_str+=j[1][0]
                    i+=1
                    break
                else:
                    i+=1
                    j=j[1]
    return (final_str)



print(encode(frequencies('aaaabcc'),'aaaabcc'))
