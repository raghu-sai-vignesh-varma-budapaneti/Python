s=eval(input("Enter a list:"))
ss=sorted(s)
esl=[]
osl=[]
rsl=[]
e=0
o=0
for i in ss:
    if i%2==0:
        esl.append(i)
    elif(i%2==1):
        osl.append(i)
print(esl,osl)
if len(esl)<len(osl):
    k=len(osl)-len(esl)+len(s)
elif len(esl)>len(osl):
    k=len(esl)-len(osl)+len(s)-1
for i in range(1,k+1):
    rsl.append(0)
for l in range(k):
    if l%2==0 and e<len(esl):
        rsl[l]=esl[e]
        e+=1
    elif l%2==1 and o<len(osl):
        rsl[l]=osl[o]
        o+=1
print(rsl)