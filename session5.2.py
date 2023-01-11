class time:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
    def sum(self,t):
        res=time(None,None,None)
        res.hour=self.hour+t.hour
        res.minute=self.minute+t.minute
        res.second=self.second+t.second
        if res.minute>60:
            res.minute=res.minute-60
            res.hour=res.hour+1
        if res.second>60:
            res.second=res.second-60
            res.minute=res.minute+1
        return res
    def sub(self,t):
        res=time(None,None,None)
        res.hour=self.hour-t.hour
        res.minute=self.minute-t.minute
        res.second=self.second-t.second
        if res.minute<0:
            res.minute=60+res.minute
            res.hour-=1
        if res.second<0:
            res.second=60+res.second
            res.minute-=1
        return res   

    def ttos(self):
        t=self.hour*3600+self.minute*60+self.second
        return t
    def stot(second):
        res=time(None,None,None)
        res.hour=second//3600
        res.minute=(second%3600)//60
        res.second=(second%3600)%60
        return res
    def show(self,s):
        print(s,self.hour,':',self.minute,':',self.second)


h=int(input('hour1: '))
m=int(input('minute1: '))
s=int(input('second1: '))
t1=time(h,m,s)
h=int(input('\nhour2: '))
m=int(input('minute2: '))
s=int(input('second2: '))
t2=time(h,m,s)

r=t1.sum(t2)
r.show('\nsum->')

if t1.hour>=t2.hour:
    r=t1.sub(t2)
else:
    r=t2.sub(t1)
r.show('sub->')

print('\n--time to second--')
h=int(input('hour: '))
m=int(input('minute: '))
s=int(input('second: '))
t=time(h,m,s)
print('second->',t.ttos())

sec=int(input("\n--second to time--\nsecond: "))
r=time.stot(sec)
r.show('time->')


