class fraction:
    def __init__(self,s,m):
        self.sorat=s
        self.makhraj=m
    def mul(self,f):
        res=fraction(None,None)    
        res.sorat=self.sorat*f.sorat
        res.makhraj=self.makhraj*f.makhraj
        return res
    def sum(self,f):
        res=fraction(None,None)
        res.sorat=self.sorat*f.makhraj+self.makhraj*f.sorat
        res.makhraj=self.makhraj*f.makhraj
        return res
    def sub(self,f):
        res=fraction(None,None)
        res.sorat=self.sorat*f.makhraj-self.makhraj*f.sorat
        res.makhraj=self.makhraj*f.makhraj
        return res
    def div(self,f):
        res=fraction(None,None)
        res.sorat=self.sorat*f.makhraj
        res.makhraj=self.makhraj*f.sorat
        return res
    def show(self,s):
        print(s,'->',self.sorat,'/',self.makhraj)
     
    
s=int(input('sorat1: '))
m=int(input('makhraj1: '))
f1=fraction(s,m)
s=int(input('\nsorat2: '))
m=int(input('makhraj2: '))
f2=fraction(s,m)

r=f1.mul(f2)
r.show('\nmul')

r=f1.sum(f2)
r.show('sum')

r=f1.sub(f2)
r.show('sub')

r=f1.div(f2)
r.show('div')

         


