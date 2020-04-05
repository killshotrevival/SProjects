def val(di,s):
    s1= [i for i in s.split('-')]
    if len(s1)>1:
        return (di[s1[0]]+di[s1[1]])
    else:
        return (di[s1[0]])

def hund(di,l):
    i=0
    while(i<len(l)):
        if l[i]=='hundred':
            if i==len(l)-1:
                return di[l[i-1]]*100
            else:
                return di[l[i-1]]*100+val(di,l[i+1])
        i+=1
    return val(di,l[0])

def parse_int(string):
    di = {'zero':0,
          'one':1,
          'two':2,
          'three':3,
          'four':4,
          'five':5,
          'six':6,
          'seven':7,
          'eight':8,
          'nine':9,
          'ten':10,
          'eleven':11,
          'twelve':12,
          'thirteen':13,
          'fourteen':14,
          'fifteen':15,
          'sixteen':16,
          'seventeen':17,
          'eighteen':18,
          'nineteen':19,
          'twenty':20,
          'thirty':30,
          'forty':40,
          'fifty':50,
          'sixty':60,
          'seventy':70,
          'eighty':80,
          'ninety':90,
          'hundred':100,
          'thousand':1000}
    if string=='one million':
        return 1000000
    l = [i for i in string.split()]
    i=0
    fi = ''
    while('and' in l):
        l.remove('and')
    if 'thousand' in l:
        while(i<len(l)):
            if l[i]=='thousand':
                break
            i+=1
        l1 = l[:i]
        l2 = l[i+1:]
        if l2:
            return hund(di,l1)*1000+hund(di,l2)
        else:
            return hund(di,l1)*1000
    elif 'hundred' in l:
        return hund(di,l)
    else:
        return val(di,l[0])
        
      