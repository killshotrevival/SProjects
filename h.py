def equ_solver(tuple1,tuple2):
    x = (tuple2[1]-tuple1[1])/(tuple1[0]-tuple2[0])
    y = (tuple1[0]*x)+tuple1[1]
    return (x,y)


def satisfy(line_cord1, line_cord2, tuple1, line_cord11, line_cord12):
    print('line_cord1',line_cord1)
    print('line_cord2',line_cord2)
    print('tuple1',tuple1)

    if min(line_cord1[0],line_cord2[0])<=tuple1[0]<=max(line_cord2[0],line_cord1[0]) and min(line_cord1[1],line_cord2[1])<=tuple1[1]<=max(line_cord2[1],line_cord1[1]):
        if min(line_cord11[0],line_cord12[0])<=tuple1[0]<=max(line_cord12[0],line_cord11[0]) and min(line_cord11[1],line_cord12[1])<=tuple1[1]<=max(line_cord12[1],line_cord11[1]):
            return True
    else:
        return False


def fight(move,all_moves):
    crossed = []
    print('in fight')
    for w_move in all_moves:
        m1 = (w_move[1][1]-w_move[0][1])/(w_move[1][0]-w_move[0][0])
        m2 = (move[1][1]-move[0][1])/(move[1][0]-move[0][0])
        if m1!=m2:
            print('Not Equal')
            a1 = m1
            b1 = w_move[0][1]-(w_move[0][0]*m1)

            a2 = m2
            b2 = move[0][1]-(move[0][0]*m2)

            #equ_solver(tuple1,tuple2)
            tuple1 = equ_solver((a1,b1),(a2,b2))
            print('tuple1',tuple1)

            if satisfy(w_move[0], w_move[1], tuple1,move[0], move[1]):
                print('Cut')
                crossed.append(w_move[0])
                crossed.append(w_move[1])
    print('crossed',crossed)
    for cro in all_moves:
        if cro[0] in crossed or cro[1] in crossed:
            all_moves.remove(cro)
    return all_moves


print(fight(((10, 0),(0, 10)),[[(0, 0),(10, 10)]]))