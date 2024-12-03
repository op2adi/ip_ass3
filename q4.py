import json
import operator
from datetime import datetime as yoyo
class course:
    ratta={}
    # uoi=[]
    def __init__(self,cname,assesments,policy):
        self.cname,self.assesments,self.policy,self.stu,self.p,self.c,self.e,self.d,self.focus,self.nm,self.ratta=cname,assesments,policy,{},[],0,0,0,{},'',{}
    # def add(self):
        with open('q4 add couse file.txt','r') as f:
            a=len(f.readlines())
            f.seek(0,0)
            for i in range(a):
                b=f.readline().split()
                self.ratta[b[0]]=sum([int(b[1]),int(b[2]),int(b[3]),int(b[4])])
    def pol(self):
        for i in range(4):
            s=list(self.ratta.values())
            f=self.policy[i]
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
            if rags!=[]:self.policy[i]=sum(rags[0])/2
    def popl(self):
        return self.policy
    def add(self):
        with open('q4 add course file.txt','r') as f:
            a=len(f.readlines())
            f.seek(0,0)
            for j in range(a):
                for i in f.readline().split():
                    if i!=',' and i!=' ' and i!='\n':
                        self.c+=(int(i)*((self.assesments[self.d])[1])/(self.assesments[self.d])[1])
                        self.d+=1
                self.d=0
                self.p.append("A") if self.c>=self.policy[0] else self.p.append('B') if self.c>self.policy[1] else self.p.append("C") if self.c>self.policy[2] else self.p.append("D") if self.c>self.policy[3] else self.p.append("F")
                self.stu[self.e]=self.p
                self.e+=1 
    def __repr__(self):
        lolipop=p=c=iopp=up=0
        with open('q4 add couse file.txt','r') as rt:
            yu=len(rt.readlines())
            rt.seek(0,0)
            for i in range(0,yu):
                sp=rt.readline().split()
                try:
                    if sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>self.policy[0]:
                        lolipop+=1
                    elif sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>self.policy[1]:
                        p+=1
                    elif sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>self.policy[2]:
                        c+=1
                    elif sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>self.policy[3]:
                        iopp+=1
                    else:
                        up+=1
                except IndexError:
                    break
                        
        return str(str({self.cname:[self.assesments,self.policy,self.p]})+'\n'+f"A---->{lolipop} \nB---->{p} \nC---->{c} \nD---->{iopp} \nF---->{up}")
    # add()
    def addcourse(self,roll,name,cname,assesments,policy):
        self.cname=cname
        self.name=name
        self.roll1=-1
        self.roll=roll
        self.assesments=assesments
        self.policy,self.stu,self.p,self.c,self.e,self.d,self.focus,self.nm=policy,{},[],0,0,0,{},''
        for i in range(4):
            s=list(self.ratta.values())
            f=self.policy[i]
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
            if rags!=[]:self.policy[i]=sum(rags[0])/2
        with open('q4 add couse file.txt','r') as f:
            a=len(f.readlines())
            f.seek(0,0)
            # print(self.ratta)
            for j in range(a):
                for i in f.readline().split():
                    if len(str(i))>3:self.roll1=int(i)
                    if self.roll1==self.roll:
                           self.c=int(self.ratta[str(self.roll1)])
                           self.p.append("A") if self.c>=self.policy[0] else self.p.append('B') if self.c>self.policy[1] else self.p.append("C") if self.c>self.policy[2] else self.p.append("D") if self.c>self.policy[3] else self.p.append("F")
                           break
                self.d=0  
                self.stu[self.e]=self.p
                self.e+=1
        with open('stu.txt','r+') as gh:
            fty=len(gh.readlines())
            # print(fty)
            gh.seek(0,0)

            for hjd in range(fty):
                # print(self.focus)
                pot=gh.tell()
                u=gh.readline()
                self.focus=eval(u)
                # print(self.focus)
                if (self.roll,self.name) in self.focus:self.focus[(self.roll,self.name)]=self.focus[(self.roll,self.name)]+[self.cname, self.assesments, self.ratta[str(self.roll)],self.policy,self.p]
                gh.seek(pot,0)
                gh.write(str(self.focus)+'\n')

class student(course):
    def __init__(self,roll,name,cname, assesments, policy):
        super().__init__(cname, assesments, policy)
        self.name=name
        self.d={}
        self.roll=roll
        self.man={}
        for i in range(4):
            s=list(self.ratta.values())
            f=self.policy[i]
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
            if rags!=[]:self.policy[i]=sum(rags[0])/2
        with open('q4 add couse file.txt','r') as f:
            a=len(f.readlines())
            f.seek(0,0)
            for i in range(a):
                b=f.readline().split()
                self.man[b[0]]=[int(b[1]),int(b[2]),int(b[3]),int(b[4])]
            for top in self.man:
                if self.roll==int(top):
                    self.p.append("A") if sum(self.man[top])>=self.policy[0] else self.p.append('B') if sum(self.man[top])>self.policy[1] else self.p.append("C") if sum(self.man[top])>self.policy[2] else self.p.append("D") if sum(self.man[top])>self.policy[3] else self.p.append("F")
                    break
        with open('stu.txt','a') as gh:
            # print(self.p)
            self.d[(self.roll,self.name)]=[self.cname, self.assesments, sum(self.man[str(self.roll)]),self.policy,self.p]
            gh.write(str(self.d)+'\n')
            self.focus=self.d
            self.nm=self.name

    def __repr__(self):
        print(f"cname is {self.cname}")
        print(f"assesments to be done{str(self.assesments)}")
        return ''     
                        # self.p.append()
def check(roll,name,courses,assesment,policy):
    global parrot
    q=course(courses,assesment,policy)
    q.pol()
    policy=q.popl()
    with open('q4 add couse file.txt','r') as rope:
            lp=len(rope.readlines())
            rope.seek(0,0)
            # sp=rope.readline().split()
            for k in range(0,lp):
                sp=rope.readline().split()
                try:
                    if sp[0]==str(roll):
                        if sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>policy[0]:
                            parrot=str(((str(sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])),'A')))
                            break
                        elif sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>policy[1]:
                            parrot=str(((str(sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])),'B')))
                            break
                        elif sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>policy[2]:
                            parrot=str(((str(sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])),'C')))
                            break
                        elif sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])>policy[3]:
                            parrot=str(((str(sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])),'D')))
                            break
                        else:
                            parrot=str(((str(sum([int(sp[1]),int(sp[2]),int(sp[3]),int(sp[4])])),'F')))
                            break
                except IndexError:
                    break
    
parrot=()
a=course('ip',(('quiz',30),('j',40),('e',30)),[80, 65, 50, 40])
a.pol()
t=course('M1',(('quiz',30),('j',40),('pop',30)),[80, 65, 50, 40])
t.pol()

b=student(2022040,'adi','ip',(('quiz',30),('j',40),('e',30)),[81, 65, 50, 40])
b.addcourse(2022040,'adi','M1',(('quiz',30),('j',40),('pop',30)),[81, 65, 50, 41])
c=student(2022005,'tyty','ip',(('quiz',30),('j',40),('e',30)),[80, 65, 50, 40])
c.addcourse(2022005,'tyty','M1',(('quiz',30),('j',40),('pop',30)),[80, 65, 50, 40])
b=student(2022008,'rag','M1',(('quiz',30),('j',40),('pop',30)),[80, 65, 50, 40])
b.addcourse(2022008,'rag','M1',(('quiz',5),('j',34),('pop',50),('lo',16)),[80, 65, 50, 40])

while True:
    print(''' Choices \n 1> for summary \n 2> for grading \n 3> for searching''')
    ch=int(input("Enter the choice"))
    if ch==1:
        print(a)
        print(t)
    elif ch==2:
        a=yoyo.utcnow()
        # kri=open('q4 add couse file.txt','r')
        f=open('studat.txt','w')
        for i in range(1,997):
            if len(str(i))<3:j='0'*(3-(len(str(i))))+str(i)
            else:j=str(i)
            check(int('2022'+str(j)),'adi','ip',(('quiz',30),('j',40),('e',30)),[81, 65, 50, 40])
            # print('2022'+str(j))
            # print(parrot)
            f.write(str('2022'+str(j)+' '+str(parrot))+'\n')
        f.close()
        b=yoyo.utcnow()
    elif ch==3:
        roll=int(input("Enter ROll number"))
        a=yoyo.utcnow()
        kiwi=open('q4 add couse file.txt','r')
        with open("studat.txt",'r') as fout :
            yu=len(fout.readlines())
            fout.seek(0,0)
            for i in range(0,yu):
                sp=fout.readline().split()
                ip=kiwi.readline().split()
                if sp!=[] and str(roll)==sp[0]:
                    print(f"{sp[0]},{sp[1][1:-1]},assesments marks:-{ip[1],ip[2],ip[3]},{sp[2]}")
                    break
            else:
                print(f"Grading Not Done")
        kiwi.close()
        b=yoyo.utcnow()
    else:
        break
        
