from time import sleep
try:
    import winsound
except ModuleNotFoundError:
    print("No_moudle_named_winsound")
    sleep(1)
else:
    pass
def Do(a):
    winsound.Beep(261,a)
def Re(b):
    winsound.Beep(283,b)
def Mi(c):
    winsound.Beep(329,c)
def Fa(d):
    winsound.Beep(349,d)
def So(e):
    windound.Beep(392,e)
def La(f):
    winsound.Beep(440,f)
def Ti(g):
    winsound.Beep(493,g)
def Dol(h):
    windound.Beep(523,h)
def Rel(i):
    windound.Beep(587,i)
def Mil(j):
    winsound.Beep(659,j)
def Fal(k):
    winsound.Beep(698,k)
def Sol(l):
    winsound.Beep(783,l)
def Lal(m):
    winsound.Beep(880,m)
def Til(n):
    winsound.Beep(987,n)
