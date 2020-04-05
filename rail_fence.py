def encode_rail_fence_cipher(string, n):
    spaces = 0
    i =0
    dire = 'v'
    matrix = []
    for i in range(n):
        matrix.append([])

    for j in string:
        if not matrix[i]:
            for k in range(spaces):
                matrix[i].append('*')
            matrix[i].append(j)
            spaces+=1
        else:
            for k in range(spaces):
                matrix[i].append('*')
            spaces+=2
            matrix[i].append(j)
        if dire=='^':
            i-=1
            if i<0:
                i=1
                spaces=1
                dire='v'
        elif dire=='v':
            i+=1
            if i>=n:
                i-=2
                dire='^'
                spaces=1
    final_str=''
    for i in matrix[::-1]:
        for j in i:
            if j!='_':
                final_str+=j
    for i in matrix[::-1]:
        print(i)
    return final_str
print(encode_rail_fence_cipher("Hello, World!", 4))
print('')

def decode_rail_fence_cipher(string, n):
    if string:
        spaces = ((n-1)*2)-1
        row=0
        matrix=[]
        for i in range(n):
            matrix.append([])
        k=0
        while k<len(string):
            dire = 'v'
            if row==n-1:
                matrix[row].append(string[k])
                k+=1
            else:
                i=row
                while i<len(string):
                    matrix[row].append(string[k])    
                    if k>=len(string):
                        break   
                    if row!=0:            
                        if dire=='v':
                            dire='^'
                            spaces=((n-row-1)*2)-1
                        elif dire=='^':
                            dire = 'v'
                            spaces=(row*2)-1
                    print('k',string[k])
                    print('spaces',spaces)
                    k+=1
                    i+=spaces+1
                spaces-=2
                row+=1
            i+=1

        for i in matrix:
            if not i:
                matrix.remove(i)
            print(i)
        i=0
        dire ='v'
        final_str = ''
        while(True):
            temp = matrix[i][0]
            matrix[i]=matrix[i][1:]
            final_str+=temp
            if dire=='v':
                i+=1
                if i>=len(matrix):
                    dire='^'
                    i=n-2
            elif dire=='^':
                i-=1
                if i<0:
                    dire='v'
                    i=1
            if not matrix[i]:
                break

        return final_str
    else:
        return ''
print(decode_rail_fence_cipher("H !e,Wdloollr", 4))