class date:
    def __init__(self,y,m,d):
        self.year=y
        self.month=m
        self.day=d

    def show(self,s):
        print(s,'->',self.year,'/',self.month,'/',self.day)
            
    def add(self,d):
        res=date(None,None,None)
        res.year=self.year+d.year
        res.month=self.month+d.month
        res.day=self.day+d.day
        
        if res.month>12:
            res.month=res.month-12
            res.year=res.year+1
        if res.day>30:
            res.day=res.day-30
            res.month=res.month+1
        return res
        
    def sub(self,d):
        res=date(None,None,None)
        res.year=self.year-d.year
        res.month=self.month-d.month
        res.day=self.day-d.day
        if res.month<0:
            res.month=res.month+12
            res.year=res.year-1
        if res.day<0:
            res.day=res.day+30
            res.month=res.month -1
        return res    

    def GetMonthName(self):
        month_list={1:'farvardin',2:'ordibehesht',3:'khordad',4:'tir',5:'mordad',6:'shahrivar',7:'mehr',8:'aban',9:'azar',10:'dey',11:'bahman',12:'esfand'}
        if 1<=self.month<=12:
            return month_list[self.month]
        else:
            return 'out of rang'
        
    def IsValidDate(self):
        if  1<=self.day <=30 and 1<=self.month<=12  and 1<=self.year<=9999:
            return True
        return False
               
y=int(input('year1: '))
m=int(input('month1: '))
d=int(input('day1: '))
d1=date(y,m,d)
y=int(input('\nyear2: '))
m=int(input('month2: '))
d=int(input('day2: '))
d2=date(y,m,d)

r=d1.add(d2)
r.show('\nsum')

if d1.year>=d2.year:
    r=d1.sub(d2)
else:
    r=d2.sub(d1)
r.show('sub')

print('\n--determine the month--')
y=int(input('year: '))
m=int(input('month: '))
d=int(input('day: '))
d1=date(y,m,d)
print('\nmonth->',d1.GetMonthName())

print('\n--determining the validity of the date--')
y=int(input('year: '))
m=int(input('month: '))
d=int(input('day: '))
d1=date(y,m,d)
print('validity->',d1.IsValidDate())
