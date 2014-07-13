def nilakantha(end): 
    op = '+'
    x = 3.0
    for n in range(2, end, 2):
        if (op == '-'):
            x -= ( 4.0 / float((n * (n+1) * (n+2))) )
            op = '+'
        elif (op == '+'):
            x += ( 4.0 / float((n * (n+1) * (n+2))) )
            op = '-'
    return x