d,e,h,main,main2,c,pop={},{},[],[],[],0,0
from datetime import datetime as dp
with open('q2_1.txt') as f:
    a=f.readlines()
    f.seek(0,0)
    for i in range(len(a)):
        b=f.readline().split(',')
        d['preset'],d['gate']=b[1][1::],b[2][1::]
        d['gate']=b[2][1::]
        l=dp.strptime(b[3][1:-1:],'%H:%M:%S').time()
        d['time']=l
        e[b[0]]=d
        h.append(e)
        e,d={},{}
while True:
    print('''CHOCES 1 for name\n 2 for start and end time\n 3 for gate number ''')
    t=int(input("enter choice"))
    try:
        if t==1:
            f=open("output.txt",'w')
            nm=input('enter name')
            km=dp.strptime(input('enter time in HH:MM:SS'),('%H:%M:%S')).time()
            for i in range(len(h)):
                if nm in h[i]:main.append(h[i])
            for i in range(len(main)+1):
                tp=f.tell()
                if main[i][nm]['preset']=="ENTER" and main[i+1][nm]['preset']=="ENTER":
                    f.seek(tp,0)
                    f.write(str(main[i])+'\n')
                elif main[i][nm]['preset']=="EXIT" and main[i+1][nm]['preset']=="EXIT":
                    f.seek(tp,0)
                    f.write(str(main[i+1])+'\n')
                else:
                    f.write(str(main[i])+'\n')
    except IndexError:
        main2=list(main)
        for i in range(len(main)):
            if i==0 and main2[i][nm]['time']>=km:
                print("IN THE CAMPUS RIGHT NOW")if main[0][nm]['preset']=="ENTER" else print("NOT IN THE CAMPUS")
                break
            elif main2[i][nm]['time']>=km:
                print("IN THE CAMPUS RIGHT NOW")if main[i-1][nm]['preset']=="ENTER" else print("NOT IN THE CAMPUS")
                break

    if t==2:
        op=dp.strptime(input('enter starting time in HH:MM:SS'),('%H:%M:%S')).time()
        p=dp.strptime(input('enter ending time in HH:MM:SS'),('%H:%M:%S')).time()
        for i in h:
            for j,k in i.items():
                if op<=k['time']<=p:print(i)
    if t==3:
        ohi=(input("Enter Gate number"))
        for i in h:
            for j,k in i.items():
                if k['gate']==ohi and k['preset']=="ENTER":c+=1
                if k['gate']==ohi and k['preset']=="EXIT":pop+=1
        print(f'number of students entered from this gate {c} \n number of students exited from this gate {pop}')
    else:break
