n,k=int(input()),-2
l=2*n-2
def starup(a):
    global k
    if a==0:return ''
    if a==1:return "* "+'  '*(2*n-2)+'* '
    else:
        k+=2
        return '* '*a+'  '*(k)+'* '*a+'\n'+starup(a-1)
def stardwn(a):
    global l
    if a>n:return ''
    if a==n:return "* "*2*n
    else:
        l-=2
        return '* '*a+'  '*(l)+'* '*a+'\n'+stardwn(a+1)
print(starup(n))
print(stardwn(2))
