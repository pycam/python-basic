#Possible advanced exercise for end of section 2
#### Text to past in the notebook:
'''
__Advanced exercise__
Determine how many iterations it takes to calculate $\pi$ to 8 decimal places using the Nilakintha series:
$$3+\sum_{n=1}\frac{4(-1)^{n+1}}{2n(2n+1)(2n+2)}$$
'''

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