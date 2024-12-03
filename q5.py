import operator
from datetime import datetime as yoyo
b={'cname':'ip','assesments':(('quiz',30),('j',40),('e',30)),'policy':[81, 65, 50, 40]}
c={'cname':'M1','assesments':(('quiz',30),('j',40),('e',30)),'policy':[81, 65, 50, 40]}
def pol(x,policy):
        ratta={}
        with open('q4 add couse file.txt','r') as f:
            a=len(f.readlines())
            f.seek(0,0)
            for i in range(a):
                b=f.readline().split()
                ratta[b[0]]=sum([int(b[1]),int(b[2]),int(b[3]),int(b[4])])
        for i in range(4):
            s=list(ratta.values())
            f=policy[i]
            uoi=[]
            rags={}
            for  k in s:
                if int(k) in range(f-2,f+2) or int(k) in [range(f-2,f+2+1)]:
                    uoi.append(int(k))
                    # print(uoi)
            for l in range(len(uoi)-1):
                rags[(uoi[l],uoi[l+1])]=uoi[l]-uoi[l+1]
            rags = list(dict(sorted(rags.items(), key=operator.itemgetter(1),reverse=True)).keys())
            # print(rags)
            if rags!=[]:x['policy'][i]=sum(rags[0])/2
        return x
def rt(x):
    policy=x['policy']
    lolipop=p=c=iopp=up=0
    with open('q4 add couse file.txt','r') as rt:
            yu=len(rt.readlines())
            rt.seek(0,0)
            for i in range(0,yu):
                sp=rt.readline().split()
                try:
                    if sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>policy[0]:
                        lolipop+=1
                    elif sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>policy[1]:
                        p+=1
                    elif sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>policy[2]:
                        c+=1
                    elif sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>policy[3]:
                        iopp+=1
                    else:
                        up+=1
                except IndexError:
                    break
    print(f"A---->{lolipop} \nB---->{p} \nC---->{c} \nD---->{iopp} \nF---->{up}")
def check(roll,policy,x={'policy':[81, 65, 50, 40]}):
    global parrot
    global d
    x=pol(x,policy)
    policy=x['policy']
    poli={0:policy[0],1:policy[1],2:policy[2],3:policy[3]}
    with open('q4 add couse file.txt','r') as rope:
            lp=len(rope.readlines())
            rope.seek(0,0)
            grades = {0:'A', 1:'B', 2:'C', 3:'D'}
            # sp=rope.readline().split()
            for k in range(0,lp):
                sp=rope.readline().split()
                d=k
                try:
                    if sp[0]==str(roll):
                        very=sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])
                        for gh in range(4):
                            if very>poli[gh]:
                                parrot=str((very,grades[gh]))
                                break
                            elif very<poli[3]:
                                parrot=str((very,'F'))
                                break
                        break
                except IndexError:
                    break
    
parrot=()
d=0
b=pol(b,b['policy'])
c=pol(c,c['policy'])
while True:
    print(''' Choices \n 1> for summary \n 2> for grading \n 3> for searching''')
    ch=int(input("Enter the choice"))
    if ch==1:
        print(b)
        rt(b)
        print(c)
        rt(c)
    elif ch==2:
        a=yoyo.utcnow()
        f=open('studat3.txt','w')
        # hi=open('q4 add couse file.txt','r')
        for i in range(1,997):
            if len(str(i))<3:j='0'*(3-(len(str(i))))+str(i)
            else:j=str(i)
            check(int(str(2022)+j),[81, 65, 50, 40])
            # ty=hi.readline().split()
            # print(f"{str(int(str(2022)+j))},{str(parrot)}")
            f.write(str('2022'+str(j)+' '+str(parrot))+'\n')
        b=yoyo.utcnow()
        f.close()
    elif ch==3:
        rl=int(input("Enter the roll number"))
        a=yoyo.utcnow()
        check(rl,[81, 65, 50, 40])
        ram=open("q4 add couse file.txt",'r')
        if d==0:srt=ram.readline().split()
        for i in range(d+1):
            srt=ram.readline().split()
        print(parrot)
        print(f"{rl},{parrot[1:4]},assesments---->{srt[1]},{srt[2]},{srt[3]},{srt[4]},{parrot[6]}")
        b=yoyo.utcnow()
        ram.close()