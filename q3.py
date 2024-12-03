n=int(input("Enter the end file no."))
d={}
import random
for j in range(n):
    unq,tot,sent,sentt,cons,rt,d,F5,poi,oi,c=0,0,0,0,0,0,{},0,[],[],0
    f=open('File'+str(j),'r')
    erp=len(f.readlines())
    f.seek(0,0)
    for k in range(erp):
        ap=f.readline().split()
        # print(ap,type(ap))
        for i in ap:
            if (i.isalpha() and i.lower() not in d):
                unq+=1
                tot+=1
                c+=1
                d[i.lower()]=1
            elif (i.isalpha() and i.lower() in d):
                tot+=1
                c+=1
                d[i.lower()]+=1
        if c>35 or c<5:
            print(ap)
            print(c)
            sent+=1
        sentt+=1
        c=0
    f.seek(0,0)
    sp=f.read()
    flag=True
    for i in range(len(sp)-1):
        if sp[i] in list(',.;:-') and sp[i+1] in list(',.;:-') and flag:
            cons+=1
            flag=False
        elif sp[i].isalpha() or sp[i]==' ' or sp[i]=='\n':flag=True
    sp=[i for i in sp if i.isalpha and i!='\n']
    sp=' '.join(sp)
    d=sorted(d.items(),key=lambda x:x[1],reverse=True)
    F1=(unq/tot)
    for l in range(5):
        oi.append(d[l][0])
        rt+=d[l][1]
    for ty in range(5):
        s=random.randint(0,len(d)-1)
        poi.append(d[s][0])
    F2=(rt/tot)
    F3=(sent/sentt)
    F4=(cons/tot)
    if tot>750:F5=1
    if tot<=750:F5=0
    print(F1,F2,F3,F4,F5)
    Net_score=4 + F1*6 + F2*6 -F3 - F4 - F5
    print(Net_score)
    lp=open('files_score.txt','a')
    lp.write('File'+str(j)+'\n')
    lp.write(str(Net_score)+'\n')
    lp.write(str([op for op in oi])+'\n')
    lp.write(str([po for po in poi])+'\n')
    f.close()

